Purchasing a File Using download21client.py
-----------------------

Here's the full client call for purchasing a file:

```
python3 download21client.py <link-to-video> <method-of-extraction> <format> [optional: specific-host]

example: python3 download21client.py https://www.youtube.com/watch?v=GjO4hp4YxYM download/video  mp4 http://110.244.53.126/5000/
```

![Run The Full Client](http://i.imgur.com/67yoYRI.png) 

Let's go through these options in depth.

**link-to-video** - Any supported video link will work here
**method-of-extraction** - This is either "download/audio" or "download/video"
**format** - common audio/video formats (mp3, mp4, wav, avi...) can be used here
