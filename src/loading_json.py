# sometime we need to load up a JSON file or any local file
# this might contain config values

import json # built in python lib

def loadJSONfile():
    '''load a text file that contains JSON'''
    try:
        # open lets us work with file access objects. 'r' means read
        with open('data/photos.json', 'r') as fin:
            photos = json.load(fin)
            return photos
            # we use 'with' because it will automatically close the file access object
    except Exception as err:
        print(f'Something went horribly wrong! Error: {err}')

if __name__ == '__main__':
    p = loadJSONfile()
    print(type(p))
    print(type(p[2]))