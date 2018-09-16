from flask import Flask, send_file, make_response, send_from_directory
import pandas as pd
import os

from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)

# localhostは変更してください
Host_name = "localhost"

@app.route("/collect")
def collect():

    fileList = os.listdir('./zipfile')

    # ここのPATH指定は，なんとかしてください
    downloadFile = "./zipfile/0915.zip"
    downloadFileName = "0915.zip"

    return send_file(downloadFile, mimetype="application/zip", as_attachment=True, attachment_filename=downloadFileName)

if __name__ == "__main__":
    print(app.url_map)
    app.run(host="localhost", port=3000)
