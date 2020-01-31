from flask import Flask
from flask import request

app = Flask(__name__)


def get_mass_info(hostname):
    return True


def get_ipmi_info(hostname, ip):
    return True


@app.route("/api/alerts", methods=['POST'])
def handle_incoming_alerts():
    print(request.json)
    return ('', 200)


if __name__ == "__main__":
    app.run()
