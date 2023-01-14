FROM python:3.10-slim
WORKDIR /app

COPY requirement.txt .
RUN pip3 install -r requirement.txt

ADD . .

CMD ["python3","/app/main.py"]