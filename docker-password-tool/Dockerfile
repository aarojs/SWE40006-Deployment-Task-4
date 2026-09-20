FROM python:3.12-slim

WORKDIR /app

COPY generate_password.py .

VOLUME /data

ENV PASSWORD_LENGTH=12

CMD ["python", "generate_password.py"]
