FROM python:3.10.6-alpine

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY src/ .

ENTRYPOINT [ "python", "blink-rpc.py" ]

