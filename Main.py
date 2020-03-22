import requests
import re

username = 'admin'
password = '71urlkufpsdnlkadsf'
url = 'http://165.227.106.113/post.php'
payload = {'username' : username, 'password': password}
r = requests.post(url, data = payload)
print(r.text)