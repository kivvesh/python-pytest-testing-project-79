import logging

import requests
import os
import string


def name_file(url):
    alp_num = string.ascii_lowercase + '0123456789'
    not_http = url.split('//')[1]
    filename = ''
    for sym in not_http:
        if sym in alp_num:
            filename += sym
        else:
            filename += '-'
    filename = f'{filename}.html'
    return filename

def download(url, path):
    if not os.path.isdir(path):
        return False
    try:
        req = requests.get(url)
        file_path = f'{path}/{name_file(url)}'
        try:
            with open(file_path,'w') as file:
                file.write(req.text)
        except PermissionError as error:
            logging.error(error)
            return False
        return file_path
    except requests.exceptions.RequestException as error:
        logging.error((error))
        return False

#print(download('https://habr.com/ru/articles/740376','/home/kivvesh/hexlet'))
if __name__ == '__main__':
    download()