#This programm will read out article numbers from the pluradent webshop


#import libraries
import requests
requests.__file__
import bs4
bs4.__file__
from bs4 import BeautifulSoup

#main function
def main(web = 1):
    #returns 1, if no error
    if web == 1:
        print("web1")
        url = 'https://shop.pluradent.de/praxisbedarf.html'
    else:
        print("web0")
        url = 'n.a.'
    
    print(url)
    print("Importing web site by using requests.get method")
    r = requests.get(url)
    return "1"

L = main(1)
print(L)



#developing area


url = 'https://shop.pluradent.de/praxisbedarf.html'
r = requests.get(url)
c = r.content
print(c)


with open('url.txt','w') as f:
    f.write(str(c))



soup = BeautifulSoup(c,"html.parser")
with open('url_soup.txt','w') as f:
    f.write(str(soup))







