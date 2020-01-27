import json
import logging

from twilio.rest import Client
from flask import Flask, Response, request
from werkzeug.datastructures import ImmutableMultiDict

logging.basicConfig(level=logging.INFO)

account_sid = "AC7bfa7dbfd372dd3e5a82219c5d37c6e8"
auth_token = "c641a842efaf6a54ecdb1e3ee71bcf80"

client = Client(account_sid, auth_token)

app = Flask(
    __name__,
    template_folder="templates"
)


@app.route("/chat", methods=["POST"])
def chat():
    rawdata = request.form

    data = rawdata.to_dict(flat=False)
    text_from = data["From"]
    text_to = data["To"]
    text_body = data["Body"]

    message = client.messages.create(
        body=text_body,
        from_=text_to,
        to=text_from
    )

    # logging.info(data)
    return Response(status = 200)


if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port='5000',
        threaded=True,
        debug=True
    )
