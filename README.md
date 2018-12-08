# Im2Vid
Im2Vid is a simple script to turn a folder of images into a video. It assumes the images are numbered with a common prefix.

## How to use:

By default, the input folder is `images/`, output folder `videos/` and filename `video.avi`. The default FPS is `15`, and resolution is `1440*1080`.
```
usage: im2vid.py [-h] [-f FPS] [-s SIZE] [-o OUTPUT] [-d DIR] [-i INPUT]
                 [-p FILE_PREFIX]

optional arguments:
  -h, --help            show this help message and exit
  -f FPS, --fps FPS     Output video fps.
  -s SIZE, --size SIZE  Video frame size. Example -s 1920,1080.
  -o OUTPUT, --output OUTPUT
                        Output file name.
  -d DIR, --dir DIR     Output directory.
  -i INPUT, --input INPUT
                        Input directory.
  -p FILE_PREFIX, --file_prefix FILE_PREFIX
                        Input image prefix, for images image1.jpg, image2.jpg
                        do: -p image
```
