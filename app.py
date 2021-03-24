from flask import Flask, render_template
from flask import request
from websocket import create_connection
import json


app = Flask(__name__)


test_key = 'EB221BB3-A67E-4BFF-B96E-1CB082D3EF34'


def json_print(obj):
  text = json.dumps(obj, sort_keys=True, indent=4)
  print(text)


class CoinAPIv1_subscribe(object):
    def __init__(self, apikey):
        self.type = "hello"
        self.apikey = apikey
        self.heartbeat = True
        self.subscribe_data_type = ["quote"]
        self.subscribe_filter_asset_id = ["BTC"]
        self.subscribe_filter_symbol_id = ["COINBASE_SPOT_BTC_USD"]
        # "COINBASE_SPOT_BTC_USDC"


ws = create_connection("ws://ws-sandbox.coinapi.io/v1/")
sub = CoinAPIv1_subscribe(test_key)
ws.send(json.dumps(sub.__dict__))
while True:
    msg = ws.recv()
    # json_print(msg)
    print(msg)

@app.route("/")
def index():
    return render_template('index.html',x=msg)

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8080, debug=True)
