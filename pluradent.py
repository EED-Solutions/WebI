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

import requests
requests.__file__
import bs4
bs4.__file__
from bs4 import BeautifulSoup
import pandas

#reading website
#cd "C:/Users/ericb/EED-Solutions by Eric Brahmann/Ideal Dental - Code/webI/"

url = 'https://shop.pluradent.de/praxisbedarf.html'
r = requests.get(url)
c = r.content
soup = BeautifulSoup(c,"html.parser")


#exporting website to txt
with open('url.txt','w') as f:
    f.write(str(c))

with open('url_soup.txt','w') as f:
    f.write(str(soup))

#with open('url_soup.txt','r') as f:
#        soup_str = f.read()

        
#category-subnav--content--list--entry--link
#<li class="category-subnav--content--list--entry">
#            <a class="category-subnav--content--list--entry--link " href="https://shop.pluradent.de/praxisbedarf.html">
#                Praxisbedarf            </a>
#                <ol class="category-subnav--content--list">
#        <li class="category-subnav--content--list--entry">
#            <a class="category-subnav--content--list--entry--link category-subnav--content--list--entry--link-active" href="https://shop.pluradent.de/praxisbedarf/pluline-qualitaetsprodukte.html">
#                PluLine Qualitätsprodukte            </a>
#                <ol class="category-subnav--content--list">
#        <li class="category-subnav--content--list--entry">
#            <a class="category-subnav--content--list--entry--link " href="https://shop.pluradent.de/praxisbedarf/pluline-qualitaetsprodukte/praxismaterial.html">
#                Praxismaterial            </a>
#                    </li>
#    </ol>
#        <ol class="category-subnav--content--list">
#        <li class="category-subnav--content--list--entry">
#            <a class="category-subnav--content--list--entry--link " href="https://shop.pluradent.de/praxisbedarf/pluline-qualitaetsprodukte/praxisinstrumente.html">
#                Praxisinstrumente            </a>
#                    </li>
#    </ol>
#        <ol class="category-subnav--content--list">
#        <li class="category-subnav--content--list--entry">
#            <a class="category-subnav--content--list--entry--link " href="https://shop.pluradent.de/praxisbedarf/pluline-qualitaetsprodukte/kleingeraete.html">
#                Kleingeräte            </a>
#                    </li>
#    </ol>
#        <ol class="category-subnav--content--list">
#        <li class="category-subnav--content--list--entry">
#            <a class="category-subnav--content--list--entry--link " href="https://shop.pluradent.de/praxisbedarf/pluline-qualitaetsprodukte/ersatzteile-praxis.html">
#                Ersatzteile Praxis (1)            </a>
#                    </li>
#    </ol>
#            </li>
#    </ol>
#        <ol class="category-subnav--content--list">
#        <li class="category-subnav--content--list--entry">
#            <a class="category-subnav--content--list--entry--link " href="https://shop.pluradent.de/praxisbedarf/praxismaterial.html">
#                Praxismaterial            </a>
#                    </li>
#    </ol>
#        <ol class="category-subnav--content--list">
#        <li class="category-subnav--content--list--entry">
#            <a class="category-subnav--content--list--entry--link " href="https://shop.pluradent.de/praxisbedarf/praxisinstrumente.html">
#                Praxisinstrumente            </a>
#                    </li>
#    </ol>
#        <ol class="category-subnav--content--list">
#        <li class="category-subnav--content--list--entry">
#            <a class="category-subnav--content--list--entry--link " href="https://shop.pluradent.de/praxisbedarf/kleingeraete.html">
#                Kleingeräte            </a>
#                    </li>
#    </ol>
#        <ol class="category-subnav--content--list">
#        <li class="category-subnav--content--list--entry">
#            <a class="category-subnav--content--list--entry--link " href="https://shop.pluradent.de/praxisbedarf/ersatzteile-praxis.html">
#                Ersatzteile Praxis (1851)            </a>
#                    </li>
#    </ol>
#            </li>


all_main_cat = soup.find_all("a",{"class":"level-top"})
print(all_main_cat[1])
l2 = all_main_cat[1].find_all("label")
b = all_main_cat[1].find_all("span",{"class":"label"})
b[0].text
l2[0]

I = 0
for item in all_main_cat:
    I = I +1
    print (I)
    label = item.find_all("span",{"class":"label"})
    try:
        is_cat = 1
        cat = label[0].text
    except:
        is_cat = 0
        cat = ''
    if is_cat == 1:
        print(cat)
        
    
    


all = soup.find_all("div",{"class":"category-subnav--content--list--entry--link"})
all = soup.find_all("div",{"class":"category-subnav--content--list--entry"})






