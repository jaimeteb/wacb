import json
import logging
import requests

from twilio.rest import Client
from flask import Flask, Response, request
from werkzeug.datastructures import ImmutableMultiDict

logging.basicConfig(level=logging.INFO)

account_sid = os.environ["TWILIO_ACCOUNT_SID"]
auth_token = os.environ["TWILIO_AUTH_TOKEN"]
rasa_server = "rasa"

client = Client(account_sid, auth_token)

app = Flask(
    __name__,
    template_folder="templates"
)


@app.route("/chat", methods=["POST"])
def chat():
    rawdata = request.form

    logging.info(rawdata)
    data = rawdata.to_dict(flat=False)
    text_from = data["From"][0]
    text_to = data["To"][0]
    text_body = data["Body"][0]


    req = requests.post(
        f"http://{rasa_server}:5005/webhooks/rest/webhook",
        data = json.dumps({
            "sender": text_from.split("+")[1],
            "message": text_body
        }),
        headers = {
            "Content-type": "application/json",
            "Accept": "text/plain"
        }
    )

    res = json.loads(req.text)
    for msg in res:
        logging.info(msg["text"])
        message = client.messages.create(
            body=msg["text"],
            from_=text_to,
            to=text_from
        )

    return Response(status = 200)


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port="5000",
        threaded=True,
        debug=True
    )
