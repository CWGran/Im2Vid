import os
import cv2
import argparse
from tqdm import tqdm


class Im2Vid:
    def __init__(self, fps, size, output_dir, output_name, input_dir, prefix):
        self.fps = fps
        self.size = size
        self.output_dir = output_dir
        self.output_name = output_name
        self.input_dir = input_dir
        self.prefix = prefix

        self._record()

    def _record(self):
        self.video = cv2.VideoWriter(self.output_dir + self.output_name, cv2.VideoWriter_fourcc(*"MJPG"), self.fps, self.size)
        print("Writing video to file {} from source folder {}".format(self.output_dir + self.output_name, self.input_dir))

        for f in tqdm(sorted(os.listdir(self.input_dir), key= lambda x: int(x.split(self.input_common)[1].split(".")[0]) )):
            img = cv2.imread(self.input_dir + f)
            self.video.write(img)

        self.video.release()


def main():
    parser = argparse.ArgumentParser()
    
    parser.add_argument("-f", "--fps", type=int, help="Output video fps.")
    parser.add_argument("-s", "--size", help="Video frame size. Example -s 1920,1080.") 
    parser.add_argument("-o", "--output", help="Output file name.")
    parser.add_argument("-d", "--dir", help="Output directory.")
    parser.add_argument("-i", "--input", help="Input directory.")
    parser.add_argument("-p", "--file_prefix", help="Input image prefix, for images image1.jpg, image2.jpg do: -p image")

    args = parser.parse_args()

    fps = 15
    size = (1440, 1080)
    output_dir = "video/"
    output_name = "video.avi"
    input_dir = "images/"
    prefix = "image"

    if args.fps:
        if args.fps > 0:
            fps = args.fps
        else:
            print("FPS cannot be below 0, using default ({}).".format(fps))

    if args.size:
        try:
            sz = args.size.split(",")
            size = (int(sz[0]), int(sz[1]))
            if size[0] < 0 or size[1] < 0:
                raise ValueError("Values has to be positive")
        except ValueError:
            size = (1440, 1080)
            print("Invalid format, using default: {}".format(size))

    if args.output:
        if len(args.output.split(".")) > 0:
            output_name = args.output.split(".")[0]
        else:
            output_name = args.output

        output_name += ".avi"

    if args.dir:
        if args.dir[-1] != "/":
            output_dir = args.dir + "/"
        else:
            output_dir = args.dir

    if args.input:
        input_dir = args.input

    if args.file_prefix:
        prefix = args.file_prefix

    im2vid = Im2Vid(fps, size, output_dir, output_name, input_dir, prefix)
    
if __name__ == "__main__":
    main()
