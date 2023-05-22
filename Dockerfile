FROM python:3.10-slim

WORKDIR /app

COPY codes codes
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY barcode_bot.py barcode_bot.py
COPY .env .env

CMD [ "python3", "barcode_bot.py"]