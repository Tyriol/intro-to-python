# we can grab public data from internet API sources

import requests

# An API is an Application Programming Interface
# A common format is a REST (RESTful) API
# Often data is presented as JSON

photoData = [] # initialise an empty variable to store the photos we fetch

def getAllPhotos():
    '''grab all the data from a RESTful API for photos'''
    api_url = 'https://jsonplaceholder.typicode.com/photos'
    # things can go wrong when using an external library
    # which includes retrieving data.
    # so we use try / catch blocks
    try:
        response = requests.get(api_url) 
        return response.json()
    except Exception as err:
        print(f'somthing went wrong: {err}')

if __name__ == "__main__":
    '''exercise this module'''

    r = getAllPhotos()
    # we now have a large python structure
    # we can now explore this structure
    print(r[5])
    # print(r)