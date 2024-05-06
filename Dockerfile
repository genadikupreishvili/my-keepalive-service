FROM python:3.9-slim

WORKDIR /app
COPY . .

RUN pip install --no-cache-dir requests

CMD ["python", "keep_alive.py"]