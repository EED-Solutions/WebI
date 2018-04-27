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

#read maincatogeries
all_main_cat = soup.find_all("a",{"class":"level-top"})
#print(all_main_cat[1])
#l2 = all_main_cat[1].find_all("label")
#b = all_main_cat[1].find_all("span",{"class":"label"})


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
        
#read subcatogeries
all_subcat = soup.find_all("div",{"class":"category-teasers--wrapper--teaser--content--subcategories mouse-over"})  

l = []
l2 = []
I = 0
J = 0
for item in all_subcat:
    I = I +1
#    print (I)
    print(I,item.text)
    print(item)
    sublinks = item.find_all("a")

    for  link in sublinks:
        if I >= 1:
            d={}
            J = J +1
            print (J)
            has_link = link.has_attr('href')
            print('Hat link',has_link)
            if link.has_attr('href'):
                print (link.text,link['href'])
                d["index"] = I
                d["index2"] = J
                d["url"] = link['href']
                d["Kategorie"] = link.text
                
                l.append(d)
        elif I == 0:
            d2 = {}
            d2["index"] = I
            d2["index2"] = J
            d2["Kategorie"] = link.text 
            d2["url"] = ""
            l2.append(d)
#exporting            
df = pandas.DataFrame(l)
df.to_csv('subcategories.csv') 
I = 0
for index,row in df.iterrows():
    I = I+1
    print (I)
    print(row["Kategorie"])
    if I == 2:
        
   
     
#df2 = pandas.DataFrame(l2)
#df2.to_csv('categories.csv')         
#f = all_subcat[1].find_all("a")
#f2 = f[1]
#print(f2.has_attr('href'))
#f2['href']
#f3 = f2.find_all(href=True)
#
#href_tags = soup.find_all(href=True)
#f3[0]




#<div class="category-teasers--wrapper--teaser--content--subcategories mouse-over">

all = soup.find_all("div",{"class":"category-subnav--content--list--entry--link"})
all = soup.find_all("div",{"class":"category-subnav--content--list--entry"})






