#! /usr/bin/python3
from PIL import Image
import sys

isLandscape = lambda x: max(x)==x[0]

def getImageFromWeb(url):
    '''
    '''
    
def getImageFromDisk(file):
    try:
        im = Image.open(file)
    except:
        return "Error opening image..."
    else:
        print("Opened image {}".format(file))
    return process(im, file)
    
def process(im, file="output.jpg"):
    if isLandscape(im.size) == False:
        return "Please provide landscape image. Only they are supported as of now"
    else:
        new_im = Image.new(im.mode, (max(im.size), max(im.size)), color=0)
        new_im.paste(im, box=(0, (im.size[0]-im.size[1])//2))
        outfile = '{}_i.jpg'.format(file[:-4])
        new_im.save(outfile)
        return "Image saved as {}".format(outfile)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print ("Please provide input file!")
    else:
        res = getImageFromDisk(sys.argv[1])
        print(res)
    
    