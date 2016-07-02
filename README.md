download21 - Serving files for satoshis using 21
===========================================================

This is a project to allow device to device offline caching of files from
streaming/music sites

Wraps the [youtube_dl](https://github.com/rg3/youtube-dl) library under the
Bitcoin Machine payments protocol for off-chain sales

Supports the [following sites](https://github.com/rg3/youtube-dl/tree/master/youtube_dl/extractor)


Repository Contents
-------------------
* **/server** - Allows for running your own server for providing file downloads
  as a service
* **/client** - Allows for extracting files from someone else's server for
  satoshis

Purchasing a File
-----------------------

Here's the full client call

```
python3 download21client.py <link-to-video> <method-of-extraction> <format>
[optional: specific-host]

example: python3 download21client.py https://www.youtube.com/watch?v=GjO4hp4YxYM
download/video  mp4 http://10.244.53.126:5000/
```

![Run The Full Client](http://i.imgur.com/67yoYRI.png) 

Let's go through these options in depth.

**link-to-video** - Any supported video link will work here
**method-of-extraction** - This is either "download/audio" or "download/video"
**format** - common audio/video formats (mp3, mp4, wav, avi...) can be used here


Getting Started Setting Up a Server
---------------

Ensure you have 21 installed and follow along to get started

The only dependency is youtube_dl which can be downloaded like so



```
sudo pip3 install youtube-dl
```

![Install Dependencies](http://i.imgur.com/bhA3aAv.png) 


Downloading
-----------

```
git clone https://github.com/bitstopco/download21.git
cd download21
```

![Download](http://i.imgur.com/PFx83ZY.png) 

In order, we are cloning a copy of this repository. It will be placed in the
current folder under a new folder called 'download21'

We are then moving to the download21 folder to verify we have a 'client' and
'server' folder


Running A Simple Server
-----------------------

```
cd server
python3 download21.py
```
![Run A Server](http://i.imgur.com/KA6mu64.png) 

In order, we are moving to the server directory and launching the server.

Congrats, you're serving up files, anyone can now use your web server.

Running the Demo Client
-----------------------

In order to simplify the operations, we packaged a demo version of the client
that will extract some sample files

These files will be extracted from your own server.

We are also assuming you are logged in as the account twenty-client and
downloaded the files under the account twenty

```
sudo chmod 777 /home/twenty/download21/client
cd /home/twenty/download21/client
python3 download21client.py sample
```
![Run The Demo Client](http://i.imgur.com/NFPU008.png) 

This will download one youtube video as mp4, one youtube video as mp3 and one
soundcloud file as mp3

Running the Full Client & Purchasing a File
-----------------------

Here's the full client call

```
python3 download21client.py <link-to-video> <method-of-extraction> <format>
[optional: specific-host]

example: python3 download21client.py https://www.youtube.com/watch?v=GjO4hp4YxYM
download/video  mp4 http://110.244.53.126/5000/
```

![Run The Full Client](http://i.imgur.com/67yoYRI.png) 

Let's go through these options in depth.

**link-to-video** - Any supported video link will work here
**method-of-extraction** - This is either "download/audio" or "download/video"
**format** - common audio/video formats (mp3, mp4, wav, avi...) can be used here


Task List (The Missing Features)
--------------------------------
- [x] serve up files
- [x] make satoshis
- [ ] break out pricing to an xml file
- [ ] clean up files after being served
- [ ] expire files after a certain amount of time (12 hours between download and payment for example)
- [ ] hail hydra


License Information
-------------------
This repo is _**open source**_ (CC0 except for youtube_dl segments)! 

Please use, reuse, and modify these files as you see fit.

Distributed as-is; no warranty is given.

Open to pull requests for task list items or additional side features.

- Your friends at Bitstop
