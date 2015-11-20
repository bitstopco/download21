import sys
import json
import os

# import from the 21 Developer Library
from two1.commands.config import Config
from two1.lib.wallet import Wallet
from two1.lib.bitrequests import BitTransferRequests

# set up bitrequest client for BitTransfer requests
wallet = Wallet()
username = Config().username
requests = BitTransferRequests(wallet, username)

# server address
def buy_file(server_url, target_link, processing_method, format):

    # get the file listing from the server
    response = requests.get(url=server_url+processing_method+"/?url="+target_link+"&format="+format)
    order = json.loads(response.text)

    buy_url = server_url+"buy?order={0}&payout_address={1}"
    answer = requests.get(url=buy_url.format(order["order"], wallet.get_payout_address()), stream=True)
    if answer.status_code != 200:
       print("Could not make an offchain payment. Please check that you have sufficient balance.")
       sys.exit()
    filename = "./downloaded_"+order["order"]
    with open(filename,'wb') as fd:
    	for chunk in answer.iter_content(4096):
             fd.write(chunk)
    fd.close()
    print('Your file is now downloaded')
 
if __name__ == '__main__':
    import sys
    if "sample" in sys.argv:
        print('ASSUMING DIRECT CONTROL')
        print('Estimated Cost: 300 satoshis')
        server_url = 'http://localhost:5000/'

        print("Extracting sample souncloud file to wav")
        buy_file(server_url, 'https://soundcloud.com/fabricehmace/apocalypse-blood-chrome-feat','download/audio', 'wav')
        print("Extracting sample youtube to mp3")
        buy_file(server_url, 'http://www.youtube.com/watch?v=KGHA9oO1Ybg', 'download/audio','mp3')
        print("Extracting sample youtube to mp4")
        buy_file(server_url, 'http://www.youtube.com/watch?v=MQ_wFqnUvv8', 'download/video','mp4')
        sys.exit()
 
    if "help" in sys.argv:
        print("Usage: download21client.py path-to-youtube-soundcloud method-of-extraction format [optional: host-to-download-from]")
        print()
        print("method-of-extraction: [download/video, download/audio]")
        print("format: [mp3, mp4, wav]")
        sys.exit()

    if len(sys.argv) > 4:
        server_url = sys.argv[4]
    else:
        server_url = 'http://10.554.81.121:5000/'

    if len(sys.argv) > 1:
        file = sys.argv[1]
    else:
        sys.exit()

    if len(sys.argv) > 2:
        method = sys.argv[2]
    else:
        sys.exit()
   
    if len(sys.argv) > 3:
        format = sys.argv[3]
    else:
        sys.exit()

    buy_file(server_url, file, method, format)
