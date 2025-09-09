import os
import time
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
from sqlalchemy.exc import OperationalError

app = Flask(__name__)

# Konfigurasi upload folder
UPLOAD_FOLDER = "static/uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# Konfigurasi PostgreSQL (pakai service name "db" dari docker-compose)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql+psycopg2://postgres:postgres@db:5432/inventorydb"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

# Model Database
class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    kode = db.Column(db.String(50), nullable=False, unique=True)
    nama = db.Column(db.String(100), nullable=False)
    stock = db.Column(db.Integer, nullable=False)
    supplier = db.Column(db.String(100), nullable=False)
    foto = db.Column(db.String(200), nullable=True)

# Tunggu sampai DB siap
with app.app_context():
    retries = 5
    while retries > 0:
        try:
            db.create_all()
            break
        except OperationalError:
            retries -= 1
            print("⚠️ Database belum siap, coba lagi...")
            time.sleep(3)
    else:
        print("❌ Gagal konek ke database setelah beberapa percobaan.")

@app.route("/")
def index():
    items = Item.query.all()
    return render_template("index.html", items=items)

@app.route("/add", methods=["POST"])
def add_item():
    kode = request.form["kode"]
    nama = request.form["nama"]
    stock = request.form["stock"]
    supplier = request.form["supplier"]
    foto = request.files["foto"]

    filename = None
    if foto:
        filename = secure_filename(foto.filename)
        foto.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))

    new_item = Item(kode=kode, nama=nama, stock=stock, supplier=supplier, foto=filename)
    db.session.add(new_item)
    db.session.commit()
    return redirect(url_for("index"))

@app.route("/edit/<int:id>", methods=["POST"])
def edit_item(id):
    item = Item.query.get_or_404(id)
    item.kode = request.form["kode"]
    item.nama = request.form["nama"]
    item.stock = request.form["stock"]
    item.supplier = request.form["supplier"]

    foto = request.files["foto"]
    if foto:
        filename = secure_filename(foto.filename)
        foto.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))
        item.foto = filename

    db.session.commit()
    return redirect(url_for("index"))

@app.route("/delete/<int:id>", methods=["POST"])
def delete_item(id):
    item = Item.query.get_or_404(id)
    if item.foto:
        try:
            os.remove(os.path.join(app.config["UPLOAD_FOLDER"], item.foto))
        except:
            pass
    db.session.delete(item)
    db.session.commit()
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
