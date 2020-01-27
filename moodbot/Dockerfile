FROM python:3.7

WORKDIR /app

ADD requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
RUN python -m spacy download en_core_web_md
RUN python -m spacy link en_core_web_md en

ADD . /app

RUN rasa train

EXPOSE 5005

CMD ["rasa", "run", "--enable-api"]
