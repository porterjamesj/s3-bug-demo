from flask import Flask, Response
from boto import connect_s3
from boto.s3.connection import OrdinaryCallingFormat

app = Flask(__name__)


@app.route("/test")
def get_test_data():
    conn = connect_s3(
        "fake_access", "fake_secret",
        host="localhost", port=5000,
        is_secure=False,
        calling_format=OrdinaryCallingFormat()
    )
    buck = conn.get_bucket("test")
    obj = buck.get_key("test")
    return Response(obj, 200)


if __name__ == "__main__":
    app.run(port=5001, threaded=True)
