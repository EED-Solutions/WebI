##This programm will read out article numbers from the pluradent webshop
#
#
##import libraries
#import requests
#requests.__file__
#import bs4
#bs4.__file__
#from bs4 import BeautifulSoup
#
##main function
#def main(web = 1):
#    #returns 1, if no error
#    if web == 1:
#        print("web1")
#        url = 'https://shop.pluradent.de/praxisbedarf.html'
#    else:
#        print("web0")
#        url = 'n.a.'
#    
#    print(url)
#    print("Importing web site by using requests.get method")
#    r = requests.get(url)
#    return "1"
#
#L = main(1)
#print(L)



#developing area

import requests
requests.__file__
import bs4
bs4.__file__
from bs4 import BeautifulSoup
import pandas
import os

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







#-----------------------------------------------------------------------------
#Kategorie Level 0 (right now only info - is not used yet)
#---------------------------------------------------------------------
all_main_cat = soup.find_all("a",{"class":"level-top"})
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
        
#-----------------------------------------------------------------------------
#Kategorie Level 1
#---------------------------------------------------------------------
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
            print('')
#            d2 = {}
#            d2["index"] = I
#            d2["index2"] = J
#            d2["Kategorie"] = link.text 
#            d2["url"] = ""
#            l2.append(d)
#exporting            
df0 = pandas.DataFrame(l)
df0.to_csv('Kategorie - Level1.csv') 

#-----------------------------------------------------------------------------
#Kategorie Level 2
#---------------------------------------------------------------------


I = 0
l = []

for index,row in df.iterrows():
     I = I+1
     
     if I != 0:
         print ("I=",I," / ", row["Kategorie - Level1"])
         print (row["url"])
         url = row["url"]
         r2 = requests.get(url)
         c2 = r2.content
         soup2 = BeautifulSoup(c2,"html.parser")
#url = 'https://shop.pluradent.de/praxisbedarf/praxisinstrumente/instrumente-konservierend.html'         
#r2 = requests.get(url)
#c2 = r2.content
#soup2 = BeautifulSoup(c2,"html.parser")
         url_nohtml = os.path.splitext(url)[0]
         all_subcat2_name = soup2.find_all("a",{"class":"category-subnav--content--list--entry--link"})
         K = 0
         for item in all_subcat2_name:
            K = K+1
            J = 0
            if item["href"].find(url_nohtml) == 0:
                d = {}
                J = J +1
                d["index"] = row["index"]
                d["index2"] = row["index2"]
                d["Kategorie - Level0"] = row["Kategorie - Level0"]
                d["Kategorie - Level1"] = row["Kategorie - Level1"]
                d["Kategorie - Level2"] = item.text.strip()
                d["url"] = item["href"]
                l.append(d)
#print(l)
df2 = pandas.DataFrame(l)
df2.to_csv('Kategorie - Level2.csv') 


#-----------------------------------------------------------------------------
#Product Level
#---------------------------------------------------------------------













    
    





    






