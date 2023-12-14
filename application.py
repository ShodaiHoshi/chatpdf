from flask import Flask, request
import requests

app = Flask(__name__)

@app.route('/fileupload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'ファイルがポストされていません', 400

    file = request.files['file']
    files = [('file', (file.filename, file.stream, 'application/octet-stream'))]
    headers = {
        'x-api-key': 'sec_KdVDx21CNmh59SRVDa8R1CcLKyZXEvLX'
    }

    response = requests.post(
        'https://api.chatpdf.com/v1/sources/add-file', headers=headers, files=files)

    if response.status_code == 200:
        return 'Source ID: ' + response.json()['sourceId']
    else:
        return 'Status: ' + str(response.status_code) + '\nError: ' + response.text

if __name__ == "__main__":
    app.run(debug=True)