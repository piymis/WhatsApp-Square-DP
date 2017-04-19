#! /usr/bin/python3
from PIL import Image
import sys, os
import argparse

isLandscape = lambda x: max(x)==x[0]

def getImageFromWeb(url):
    '''
    TODO
    '''
    return None

def getImageFromDisk(file):
    try:
        im = Image.open(file)
        print("Opened image {}".format(file))
        return process(im, file)
    except IOError:
        return "Error opening image..."

def process(im, file="output.jpg"):
    if not isLandscape(im.size):
        print("Please provide landscape image. Only they are supported as of now")
    else:
        new_im = Image.new(im.mode, (max(im.size), max(im.size)), color=0)
        new_im.paste(im, box=(0, (im.size[0]-im.size[1])//2))
        (filename, fileExtension) = os.path.splitext(file)
        outfile = '{fname}_i{fext}'.format(fname=filename, fext=fileExtension)
        new_im.save(outfile)
        return "Image saved as {}".format(outfile)

def main():
    '''
    Arguments:
        image - Input image file
        [-h | --help] - Usage information
    '''
    parser = argparse.ArgumentParser(description="Convert images to square shape for"
                "use as DP in whatsapp and other social applications")

    # Mandatory source image file
    parser.add_argument("image", help="Input image file to resize")
    args = parser.parse_args()

    # Resize
    res = getImageFromDisk(args.image)
    print(res)

if __name__ == '__main__':
    main()
