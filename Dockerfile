FROM python:3.8-alpine

COPY . .

ENTRYPOINT ["python", "./main.py"]