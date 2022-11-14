import requests,re,os
from bs4 import BeautifulSoup as bes
from concurrent.futures import ThreadPoolExecutor
c = (
    "\033[0m", #end colour
    "\033[36m", #cyan
    "\033[91m", #red
    "\033[35m", #magenta
    "\033[33m", #yellow
    "\033[32m", #green
)
def banner():
  print(f'''{c[2]}
  oo                                        
   oo     OOOOOOOO:       OOOOOOOO!       
      oOOOO!!!!;;;;O    OO.......:;!O     
     'OOO!!!;;;;;;;;O  O.......:   ;!O    
     OOO!!!!;;::::::.OO........:    ;!O   
     OO!!!!;;:::::..............:   ;!O   
     OOO!!!;::::::..............:   ;!O   
      OO!!;;::::::.............:   ;!O    
       OO!;;::::::......oo.....::::!O{c[0]}    
         O!!;::::::........oo..:::O       
           !!!;:::::..........ooO         
              !!;:::::.......O   oo       
{c[5]}By Xm4nXp{c[0]}        ;;::::.....O        oo  ,o
  {c[5]}Bokep 2022{c[0]}        :::..O              ooo
                     ::.              oooo
  ''')
class bokep():
  def __init__(self):
    self.hasil = []
    self.url_ = 'https://bokep2022.xyz/{}'
    self.headers = {'user-agent':'Mozilla/5.0 (Linux; Android 10; SM-G996U Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Mobile Safari/537.36'}
    self.result = []
  def main_url(self,param:str,ses:None) -> next:
      wek = ses.get(self.url_.format(param),headers=self.headers)
      return wek
  def by_search(self) -> requests.Response:
    ser = input('judul : ')
    page = int(input('Berapa Page ? '))
    for i in range(page):
      r = self.main_url(f'page/{i}/?s={ser}',requests.Session())
      screp = bes(r.text,'html.parser')
      ow = screp.select('article')
      for ewe in ow:
        koei = ewe.find('a')
        link,judul = koei['href'],koei['title']
        self.result.append('x')
        print(f'{c[5]}{link}{c[0]} | {c[1]}{judul}{c[0]}')
        open(f'{ser}.txt','a').write(link+'   | '+judul+'\n')
    print(f'total {c[4]}%d{c[0]} - %s.txt'%(len(self.result),ser))
  def by_tag(self) -> requests.Response:
    ser = input('tag : ')
    page = int(input('berapa page : '))
    for i in range(1,page):
      r = self.main_url(f'tag/{ser}/page/{i}/',requests.Session())
      if r.status_code == 200:
        screp = bes(r.text,'html.parser')
        ow = screp.select('article')
        for ewe in ow:
            koei = ewe.find('a')
            link,judul = koei['href'],koei['title']
            print(f'{c[5]}{link}{c[0]} | {c[1]}{judul}{c[0]}')
            open(f'{ser}-tag.txt','a').write(link+'   | '+judul+'\n')
            self.result.append('x')
       #     print(link,judul)
      else:
        break
    print(f'total {c[4]}%d{c[0]} - %s.txt'%(len(self.result),ser))
  def tanya(self):
    banner()
    print('1.by search\n2.by tag')
    isek = int(input('\n> '))
    if isek == 1:
      self.by_search()
    elif isek == 2:
      self.by_tag()
if __name__ == '__main__':
  os.system('clear')
  bokep().tanya()
