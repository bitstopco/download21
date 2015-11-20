import os
import json
import random
import youtube_dl

from flask import Flask
from flask import request
from flask import send_from_directory

from two1.lib.wallet import Wallet
from two1.lib.bitserv.flask import Payment

app = Flask(__name__)
wallet = Wallet()
payment = Payment(app, wallet)

files={}
hash=''

#Need the following - format, url
@app.route('/download/audio/', methods=['GET'])
def download_audio():
    hash = random.getrandbits(128)
    filename = str(hash) + "." + str(request.args.get('format'))
    files[filename] = { 'cost': 100, 'file': filename }
    options = {'outtmpl' : filename, 'format' : 'bestaudio/best', 'audioformat': request.args.get('format'),'extractaudio': True, 'noplaylist': True}
    with youtube_dl.YoutubeDL(options) as ydl:
       ydl.download([request.args.get('url')])
    return '{ "order":"' + filename + '" }'

#Need the following - format, url
@app.route('/download/video/', methods=['GET'])
def download_video():
    hash = random.getrandbits(128)
    filename = str(hash) + "." + str(request.args.get('format'))
    files[filename] = { 'cost': 100, 'file': filename }
    options = {'outtmpl' : filename, 'format' : 'bestaudio/best','videoformat' : request.args.get('format'), 'noplaylist': True}
    with youtube_dl.YoutubeDL(options) as ydl:
       ydl.download([request.args.get('url')])
    return '{ "order":"' + filename + '" }'

def charge_amount(request):
    return files[request.args.get('order')]["cost"]

# purchase endpoint
@app.route('/buy')
@payment.required(charge_amount)
def buy_file():
    file = files[request.args.get('order')]

    # check if selection is valid
    if(file):
        return send_from_directory('./', file["file"])

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
