import requests
import json

apiroot = 'http://ws.audioscrobbler.com/2.0/'

def get_api_key():
    try:
        f = open("apikey.txt")
    except FileNotFoundError:
        print("FAILED: No apikey.txt found in directory")
        return None

    key = f.readline().strip()
    return key

api_key = get_api_key()

def getter(method, params, apikey=api_key, get_json=False):

    assert type(method) == str
    assert type(params) == dict

    url = apiroot + '?'
    url += "method=" + method

    for param in params:
        url += '&' + param + '=' + params[param]

    url += '&api_key=' + apikey

    if get_json:
        url += "&format=json"

    text = requests.get(url).text

    return text

def user_gettoptracks(user, period=None, limit=None, page=None, apikey=api_key,
        get_json=False):

    params = {'user':user}
    if period:
        params['period'] = period
    if limit:
        params['limit'] = limit
    if page:
        params['page'] = page

    return getter("user.gettoptracks", params, apikey, get_json)
