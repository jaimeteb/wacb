FROM python:3.7

WORKDIR /app
ADD requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
ADD . /app

EXPOSE 5000

CMD ["python", "server.py"]
