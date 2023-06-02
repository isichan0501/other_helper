import requests
import json
from typing import Optional, List

def get_kaomoji_list(search_word: str = 'わら') -> str:
    API_URL: str = "https://cloud.simeji.me/py?ol=1&switch=2&section=0&ver=10.7&api_version=2&web=1&py={}".format(search_word)
    data: requests.Response = requests.get(API_URL, timeout=20).json()
    kaomoji_list = [x['word'] for x in data['data'][0]['candidates']]
    return kaomoji_list

def main():
    kaomoji_list: str = get_kaomoji_list()
    print(kaomoji_list)

if __name__ == '__main__':
    # main()
    kaomoji_list = get_kaomoji_list(search_word='おこ')
    
    import pdb;pdb.set_trace()
    print(kaomoji_list)
    

