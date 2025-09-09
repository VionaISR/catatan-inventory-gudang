FROM python:3.10

WORKDIR /app

# copy requirements dari folder app
COPY app/requirements.txt .

RUN pip install -r requirements.txt

# copy semua isi app/
COPY app/ .

CMD ["python", "main.py"]
