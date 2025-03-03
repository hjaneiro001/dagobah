# Usa una imagen base de Python 3.11 slim para reducir el tamaño
FROM python:3.11-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["python3", "app/main.py"]