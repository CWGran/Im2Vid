import os
import cv2
import argparse
from tqdm import tqdm

class Im2Vid:


    def __init__(self, fps, size, output_dir, output_name, input_dir):
        self.fps = fps
        self.size = size
        self.output_dir = output_dir
        self.output_name = output_name
        self.input_dir = input_dir

    def _record(self):
        self.video = cv2.VideoWriter(self.output_name, -1, self.fps, self.size)

        for f in tqdm(os.listdir(self.input_dir)):
            print(f)


def main():
    parser = argparse.ArgumentParser()
    
    parser.add_argument("-f", "--fps", type=int, help="Output video fps.")
    parser.add_argument("-s", "--size", help="Video frame size. Example -s 1920,1080.") 
    parser.add_argument("-o", "--output", help="Output file name.")
    parser.add_argument("-d", "--dir", help="Output directory.")
    parser.add_argument("-i", "--input", help="Input directory.")

    args = parser.parse_args()

    fps = 15
    size = (1440, 1080)
    output_dir = "video/"
    output_name = "video.avi"
    input_dir = "images"

    if args.fps:
        fps = args.fps

    if args.size:
        try:
            sz = args.size.split(",")
            size = (int(sz[0]), int(sz[1]))
            if size[0] < 0 or size[1] < 0:
                raise ValueError("Values has to be positive")
        except ValueError:
            size = (1440, 1080)
            print("Invalid format, using default: {}".format(size))

    print(size)

    if args.output:
        output_name = args.output

    if args.dir:
        output_dir = args.dir

    if args.input:
        input_dir = args.input

    im2vid = Im2Vid(fps, size, output_dir, output_name, input_dir)
    
if __name__ == "__main__":
    main()
