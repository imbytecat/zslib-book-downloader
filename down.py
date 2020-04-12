import json
import requests
import os
import re


def validate_title(title):
    rstr = r"[\/\\\:\*\?\"\<\>\|]"  # 无法作为文件名的符号 '/ \ : * ? " < > |'
    new_title = re.sub(rstr, "_", title)  # 替换为下划线
    return new_title


name = ''
author = ''
url = ''
filename = ''
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/80.0.3987.149 Safari/537.36 '
}

with open('books.json', 'r') as f:
    data = json.load(f)

books = data['msg']['list']

for book in books:
    url = 'http://photoapps.yd.chaoxing.com' + book['path']
    name = validate_title(book['name'])
    if 'author' in book:
        author = validate_title(book['author'])
        filename = name + '.' + author + '.' + os.path.basename(url)
    else:
        filename = name + '.' + os.path.basename(url)
    if not os.path.exists('books/' + filename):
        r = requests.get(url, headers=headers)
        print('Doesn\'s exist, now downloading ' + name)
        with open('books/' + filename, 'wb') as f:
            f.write(r.content)
    else:
        print('Book exited, ignored ' + name)
