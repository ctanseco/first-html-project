from flask import Flask
from flask import request
from websocket import create_connection
import json


app = Flask(__name__)

@app.route("/")
def index():
    return (
        """
        <html>
            <head>
                <title>Bong's Page</title>
            </head>
        <body>

            <h1>This is Bong's Heading</h1>
            <p>This is Bong's paragraph.</p>
            <p title="About Bong's Page">Bong's page is a cool site!</p>
        </body>
        </html>
        """
    )

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8080, debug=True)
