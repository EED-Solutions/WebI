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
for item in all_subcat:
    I = I +1
    print(I,item.text)
    print(item)
    sublinks = item.find_all("a")
    J = 0
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
                d["Kategorie - Level0"] = "Praxisbedarf"
                d["Kategorie - Level1"] = link.text
                d["Kategorie - Level2"] = ""
                
                l.append(d)
        elif I == 0:
#            d2 = {}
#            d2["index"] = I
#            d2["index2"] = J
#            d2["Kategorie"] = link.text 
#            d2["url"] = ""
#            l2.append(d)
#exporting            
df = pandas.DataFrame(l)
df.to_csv('subcategories.csv') 

#-----------------------------------------------------------------------------


    
#---------------------------------------------------------------------
I = 0
l = []

for index,row in df.iterrows():
    I = I+1
    
    if I == 15:
        print (I)
        print(row["Kategorie"])
        r2 = requests.get(row["url"])
        c2 = r2.content
        soup2 = BeautifulSoup(c2,"html.parser")
        all_subcat2 = soup2.find_all("div",{"class":"category-teasers--wrapper--teaser--image"})
        
        J = 0
        for item in all_subcat2:
            d = {}
            J = J +1
            print("J=",J)
            a = item.find_all("a")
            print(item)
            d["index"] = row["index"]
            d["index2"] = row["index2"]
            d["Kategorie - Level0"] = row["Kategorie - Level0"]
            d["Kategorie - Level1"] = row["Kategorie - Level1"]
            d["Kategorie - Level2"] = a[0].text
            d["url"] = a[0]["href"]
            l.append(d)
print(l)











    
    





    
#exporting website to txt
with open('url2.txt','w') as f:
    f.write(str(c))

with open('url_soup2.txt','w') as f:
    f.write(str(soup2))

    
    
url_test2 = 'https://shop.pluradent.de/praxisbedarf/pluline-qualitaetsprodukte/praxisinstrumente/instrumente-konservierend/mundspiegel-sonden-und-pinzetten.html'

r = requests.get(url_test2)

c = r.content
soup3 = BeautifulSoup(c,"html.parser")  
with open('url_soup3.txt','w') as f:
    f.write(str(soup3))
#---------------------------------TEST

all_subcat2 = soup2.find_all("a",{"class":"category-subnav--content--list--entry--link"})  
l = []
l2 = []
I = 0
J = 0
for item in all_subcat2:
    I = I +1
    print(I,item.text)
#    print(item)

   
     
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






