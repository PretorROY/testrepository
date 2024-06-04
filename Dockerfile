FROM python:3
workdir /app
copy main.py /app/main.py

cmd ["python", "/app/main.py"]