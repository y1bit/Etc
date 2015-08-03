import requests
import urllib
import sys
from bs4 import BeautifulSoup

if len(sys.argv) == 1:
  print('\n[*] input url')
  exit(1)

url = sys.argv[1]
url = url.rsplit('in/')

if len(url) == 3:
    url = url[0]+'in/'+url[1]    
if len(url) == 2:
    url = url[0]

url = url + 'sizes/k/'

re = requests.get(url)
src = re.text
soup = BeautifulSoup(src)
img = soup.find_all('img')
src2 = img[2]['src']

x = urllib.request.urlopen(src2)

saveFile = open('DownloadFile.jpg','wb')
saveFile.write(x.read())
saveFile.close()

print('[*] Done')
