#! /usr/bin/python3

from PIL import Image
from io import BytesIO
import sys, os
import argparse
import requests

isLandscape = lambda x: max(x)==x[0]


def buildImageAndWebFunctions(remote):
    '''
    Creates a function to get images either locally or remote.

    Arguments:
        path - Path to the image file (Either local or a URL)

    Returns:
        A getimage function (Built using closures)
    '''
    def getImage(path):
        (_, filename) = os.path.split(path)
        if remote:
            filedata = BytesIO(requests.get(path).content)
        else:
            filedata = filename
        return process(filedata, filename)
    return getImage

rules = \
    [('getImageFromWeb', True),
     ('getImageFromDisk', False)
    ]

getImageFunctions = {funcName:buildImageAndWebFunctions(remote) for funcName, remote in rules}


def process(filedata, filename):
    '''
    Do the image resize of a valid image.

    Arguments:
        filedata - A valid image file either local or remote
        filename - Source image filename
    Returns:
        True : If success
        False: If failure
    '''
    try:
        im = Image.open(filedata)
        print("Opened image {}".format(filename))
    except IOError:
        print("Error opening image...")
        return False

    if not isLandscape(im.size):
        print("Please provide landscape image. Only they are supported as of now")
        return False
    else:
        new_im = Image.new(im.mode, (max(im.size), max(im.size)), color=0)
        new_im.paste(im, box=(0, (im.size[0]-im.size[1])//2))
        (filename, fileExtension) = os.path.splitext(filename)
        outfile = '{fname}_i{fext}'.format(fname=filename, fext=fileExtension)
        new_im.save(outfile)
        print("Image saved as {}".format(outfile))
        return True

def main():
    '''
    Arguments:
        path - Input image file
        [-h | --help] - Usage information
    '''
    parser = argparse.ArgumentParser(description="Convert images to square shape for"
                "use as DP in whatsapp and other social applications")

    # Mandatory source image file
    parser.add_argument("path", help="Input image file to resize")
    parser.add_argument("-r", "--remote", help="Used for remote fetching of images from web",
            const=True, default=False, nargs='?')
    args = parser.parse_args()

    if args.remote:
        getImageFunctions["getImageFromWeb"](args.path)
    else:
        getImageFunctions["getImageFromDisk"](args.path)


if __name__ == '__main__':
    main()
