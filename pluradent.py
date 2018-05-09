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
import re

#reading website
#cd "C:/Users/ericb/EED-Solutions by Eric Brahmann/Ideal Dental - Code/webI/"


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
        
        

cat0 = {'praxisbedarf','laborbedarf'}
cat0 = {'laborbedarf'}
for cat in cat0:
    print('-----------------------------------------------------')
    print(cat)
    print('-----------------------------------------------------')
    url = 'https://shop.pluradent.de/'+cat+'.html'
    print (url)

#    url = 'https://shop.pluradent.de/praxisbedarf.html'
    r = requests.get(url)
    c = r.content
    soup = BeautifulSoup(c,"html.parser")

    sttr = 'url_'+ cat +'.txt'
    print(sttr)
    #exporting website to txt
    with open('url_'+cat+'.txt','w') as f:
        f.write(str(c))
    
    with open('url_soup_'+cat+'.txt','w') as f:
        f.write(str(soup))
    
    current_cat = cat           
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
                    d["Kategorie - Level0"] = current_cat
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
    df1 = pandas.DataFrame(l)
    df1.to_csv('Kategorie - Level1 - ' + cat +'.csv') 

    #labormaterial - kleingeräte labor / ersatzeile labor werden nicht ausgelesen
    #praxismaterial https://shop.pluradent.de/praxisbedarf/ersatzteile-praxis.html
    
    #-----------------------------------------------------------------------------
    #Kategorie Level 2
    #---------------------------------------------------------------------
    
    
    I = 0
    l = []
    
    for index,row in df1.iterrows():
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
             J = 0
             for item in all_subcat2_name:
                K = K+1
                if item["href"].find(url_nohtml) == 0:
                    d = {}
                    J = J +1
                    d["index"] = row["index"]
                    d["index2"] = row["index2"]
                    d["index3"] = J
                    d["Kategorie - Level0"] = row["Kategorie - Level0"]
                    d["Kategorie - Level1"] = row["Kategorie - Level1"]
                    d["Kategorie - Level2"] = item.text.strip()
                    d["url"] = item["href"]
                    l.append(d)
    #print(l)
    df2 = pandas.DataFrame(l)
    df2.to_csv('Kategorie - Level2 - ' + current_cat + '.csv') 



    #-----------------------------------------------------------------------------
    #Product Level 0 - infos auf der Übersichtsseite
    #---------------------------------------------------------------------
    print('---------------------------------------------------------------------')
    print('Produkt Level - 0 wird ausgelesen')
    print('---------------------------------------------------------------------')
    I = 0
    J = 0
    K = 0
    l = []
    for index,row in df2.iterrows():
         I = I+1
         if row["Kategorie - Level1"] != row["Kategorie - Level2"] and (I == 2 or I == 25 or I == 16):
             print ("I=",I,"/", row["Kategorie - Level1"],"/",row["Kategorie - Level2"])
             print (row["url"])
             url = row["url"]
    
    #url = 'https://shop.pluradent.de/praxisbedarf/pluline-qualitaetsprodukte/praxismaterial/abformung.html'
             r3 = requests.get(url)
             c3 = r3.content
             soup3 = BeautifulSoup(c3,"html.parser")
    
             #count pages
             pages = soup3.find_all("div",{"class":"pages"})
             pages2 = pages[0].find_all("a")
             K = 0
             pagecount = 0
             for page in pages2:
                 K= K+1
                 if page.text.isdigit():
                     pagecount = max(int(page.text),pagecount)
             print ("pagecount=", pagecount)
             
              #Elements per page
             elements = soup3.find("div",{"class":"limiter"})
             elements = elements.find_all("option")
             K = 0
             for d_item in elements:
                K = K+1
                if d_item.has_attr('selected'):
                    elements = int(d_item.text)
                    print(elements,"elements per page")
    
             #iterate
    #         for I in range(1,pagecount+1):
             for J in range(1,2):
                 
                 url_page = url+"?p="+str(J)
                 print(url_page)
    
    #read artikelnummer / url image / name / preis
    #url_page = 'https://shop.pluradent.de/praxisbedarf/pluline-qualitaetsprodukte/praxismaterial/abformung.html?p=1'
                 r4 = requests.get(url_page)
                 c4 = r4.content
                 soup4 = BeautifulSoup(c4,"html.parser")
                 #lists all products
                 products = soup4.find_all("div",{"class":"list-product-item"})
                 L=0
                 for product in products:
                     L=L+1
                     if L > elements:
                         break
                     #url to image
                     image = product.find("div",{"class":"list-product-item--image"})
                     url_image=image.find("img")["src"]
                     #artikelnummer
                     sku = product.find("div",{"class":"product-info--sku"})
                     m=re.search('\d+',sku.text)
                     sku = m.group(0)
                     #name+url
                     pr_info = product.find("div",{"class":"product-info"})
                     pr_info_a = pr_info.find("a")
                     product_name=pr_info_a["title"]
                     product_url=pr_info_a["href"]
    
                    #price - unterelment von pr_info
                     price = pr_info.find("div",{"class":"product-info--price"})
                     price = price.text.replace('\n', '').strip()
                     print(price)
    #                    <div class="product-info--price ">
    #                    9,25&nbsp;€</div>
    
                     d = {}
                     d["index"] = row["index"]
                     d["index2"] = row["index2"]
                     d["index3"] = row["index3"]
                     d["index4"] = L
                     d["Kategorie - Level0"] = row["Kategorie - Level0"]
                     d["Kategorie - Level1"] = row["Kategorie - Level1"]
                     d["Kategorie - Level2"] = row["Kategorie - Level2"]
                     d["ArtikelNr"] = sku
                     d["url image"] = url_image
                     d["url"] = product_url
                     d["Name"] = product_name
                     d["Preis"] = price
                     l.append(d)
            
#    print(l) 
    
    df3 = pandas.DataFrame(l)
    df3.to_csv('Produkt - Level0 - ' + current_cat + '.csv') 

        
        
#        "product-info--price "
    
#-----------------------------------------------------------------------------
#Product Level 1 - info von der spezifischen Produktseite
#---------------------------------------------------------------------
print('---------------------------------------------------------------------')
print('Produkt Level - 1 wird ausgelesen')
print('---------------------------------------------------------------------')
I = 0
J = 0
K = 0
l = []
for index,row in df3.iterrows():
     I = I+1
     if I > 0:
         print ("I=",I,"/", row["Kategorie - Level1"],"/",row["Kategorie - Level2"])
         print (row["Name"],"/",row["ArtikelNr"])
         print (row["url"])
         url = row["url"]
         r5 = requests.get(url)
         c5 = r5.content
         soup5 = BeautifulSoup(c5,"html.parser")
         #hersteller
         hersteller = soup5.find("div",{"class":"product-detail-page--main--introduction--info--udxpluradentzzherbz"})
         hersteller = hersteller.find("span",{"class":"value"}).text.replace("/n","").strip()
         sku_hersteller = soup5.find("div",{"class":"product-detail-page--main--introduction--info--manufacturer_sku"})
         sku_hersteller = sku_hersteller.find("span",{"class":"value"}).text.replace("/n","").strip()
         product_desc = soup5.find("div",{"class":"product-detail-page--main--details--desc"})
         product_desc = product_desc.find("p").text.strip()
         url_image = soup5.find("div",{"class":"product-detail-page--main--introduction--media"})
         url_image = url_image.find("img")["src"]
         d = {}
         d["index"] = row["index"]
         d["index2"] = row["index2"]
         d["index3"] = row["index3"]
         d["index4"] = row["index4"]
         d["Kategorie - Level0"] = row["Kategorie - Level0"]
         d["Kategorie - Level1"] = row["Kategorie - Level1"]
         d["Kategorie - Level2"] = row["Kategorie - Level2"]
         d["ArtikelNr"] = row["ArtikelNr"]
         d["url"] = row["url"]
         d["Name"] = row["Name"]
         d["Preis"] = row["Preis"]
#         neue Elemente
         d["url image"] = url_image
         d["Hersteller"] = hersteller
         d["HerstellerNr"] = sku_hersteller
         d["Beschreibung"] = product_desc
         l.append(d)


#print(l) 

df4 = pandas.DataFrame(l)
df4.to_csv('Produkt - Level1.csv') 

#exporting website to txt
#with open('url5.txt','w') as f:
#    f.write(str(c5))
#
#with open('url_soup5.txt','w') as f:
#    f.write(str(soup5))
#
#
#
#m = re.search('(?<=abc)def', 'abcdef')
#m.group(0)











    
    





    






