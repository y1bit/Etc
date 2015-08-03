import requests
import urllib
import sys
from bs4 import BeautifulSoup

if len(sys.argv) == 1:
  print('\n[*] input url')
  exit(1)

url = sys.argv[1];

re = requests.get(url)
src = re.text
soup = BeautifulSoup(src)
iframe = soup.iframe
try:
    src2 = iframe['src']
except KeyError:
    print("\n[*] Can't Find Video File")
    exit(1)

re = requests.get(src2)
src = re.text
soup = BeautifulSoup(src)
iframe = soup.source
src2 = iframe['src']

x = urllib.request.urlopen(src2)

saveFile = open('DownloadFile.mp4','wb')
saveFile.write(x.read())
saveFile.close()

print('[*] Done')
