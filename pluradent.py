##This programm will read out article numbers from the pluradent webshop
#
#






#import libraries

import requests
requests.__file__
import bs4
bs4.__file__
from bs4 import BeautifulSoup
import pandas
import os
import re
import time
import math
import socket

#import classes

#from pandas import ExcelWriter

#reading website
#cd "C:/Users/ericb/EED-Solutions by Eric Brahmann/Ideal Dental - Code/webI/"



    
#-----------------------------------------------------------------------------
#Kategorie Level 0 (right now only info - is not used yet)
#---------------------------------------------------------------------
#all_main_cat = soup.find_all("a",{"class":"level-top"})
#I = 0
#for item in all_main_cat:
#    I = I +1
#    print (I)
#    label = item.find_all("span",{"class":"label"})
#    try:
#        is_cat = 1
#        cat = label[0].text
#    except:
#        is_cat = 0
#        cat = ''
#    if is_cat == 1:
#        print(cat)


#-------------------------------------------------
#0) Initialisierung
#------------------------------------------------
    
#Log
outpath = 'C:/Users/ericb/EED-Solutions by Eric Brahmann/Ideal Dental - Code/webI/'
outpath = "C:/Users/ericb/EED-Solutions by Eric Brahmann/Ideal Dental - Dateien Code/webI/out/"
logfile =  outpath+'log.txt'  
localtime = time.asctime( time.localtime(time.time()) )
ip_address = socket.gethostbyname(socket.gethostname())     
with open(logfile,'w') as f:
        f.write('start: ' + localtime)
        f.write('\nip: ' + ip_address)  


    #Variables
cr = 0 #count_requests
        #dataframes
df1='';df2='';df3 = '';df4='';df5=''

sheet_out = "Tabelle1"

#Steuervariablen
request_cat2 = 0 #1:= requests url in order do read Category level 2 / 0:= imports excel file instead
request_prod0 = 1 #1:= requests url in order do read Product level 0 / 0:= imports excel file instead

 
#-------------------------------------------------
#0) Start
#------------------------------------------------

cat0 = {'praxisbedarf','laborbedarf'}
cat0 = {'praxisbedarf'}
for cat in cat0:
    print('-----------------------------------------------------')
    print(cat)
    print('-----------------------------------------------------')
    url = 'https://shop.pluradent.de/'+cat+'.html'
    print (url)
    with open(logfile,'a') as f:
        f.write('\n\n' + cat)
        f.write('\n-------------------------------------\n\n' )

#    url = 'https://shop.pluradent.de/praxisbedarf.html'
    r = requests.get(url);cr = cr+1
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
    cat_label = 'Kategorie_1'
    file = cat_label + '_'  + current_cat
    
    with open(logfile,'a') as f:
        f.write('\n\n' + cat_label + ' wird ausgelesen' + '\n\n' )
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

                
    df1 = pandas.DataFrame(l)
    df1.to_csv( file + '.csv') 
    df1.to_excel(outpath + file +'.xlsx' ,sheet_name = sheet_out)
#    writer = ExcelWriter(outxls)
#    df1.to_excel(writer,sheet)
#    writer.save()
    


    
    #-----------------------------------------------------------------------------
    #Kategorie Level 2
    #---------------------------------------------------------------------
    
    cat_label = 'Kategorie_2'
    file = cat_label + '_'  + current_cat
    
    with open(logfile,'a') as f:
        f.write('\n\n' + cat_label + ' wird ausgelesen' + '\n\n' )
    
    I = 0
    l = []
    if request_cat2 == 0:
        print("\n\timport dataframe from excel")
        df2 = pandas.read_excel(outpath +file+'.xlsx',sheet_name = sheet_out)
        with open(logfile,'a') as f:
            f.write('\n\t' + sheet_out + ' aus ' + file + ' gelesen' )
    elif request_cat2 == 1:
        for index,row in df1.iterrows():
             I = I+1
             
             if I != 0:
                 print ("I=",I," / ", row["Kategorie - Level1"])
                 print (row["url"])
                 url = row["url"]
                 r2 = requests.get(url);cr = cr+1
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
       
             if current_cat == 'laborbedarf':
                print('a')
                d = {}
                J = J +1
                d["index"] = ''
                d["index2"] = ''
                d["index3"] = J
                d["Kategorie - Level0"] = current_cat
                d["Kategorie - Level1"] = ''
                d["Kategorie - Level2"] = 'Kleingeräte Labor'
                d["url"] = 'https://shop.pluradent.de/laborbedarf/kleingeraete-labor.html'
                l.append(d)
                d = {}
                J = J +1
                d["index"] = ''
                d["index2"] = ''
                d["index3"] = J
                d["Kategorie - Level0"] = current_cat
                d["Kategorie - Level1"] = ''
                d["Kategorie - Level2"] = 'Ersatzteile Labor'
                d["url"] = 'https://shop.pluradent.de/laborbedarf/ersatzteile-labor.html'
                l.append(d)
             elif current_cat == 'praxisbedarf':
                d = {}
                J = J +1
                d["index"] = ''
                d["index2"] = ''
                d["index3"] = J
                d["Kategorie - Level0"] = current_cat
                d["Kategorie - Level1"] = ''
                d["Kategorie - Level2"] = 'Ersatzteile Praxis'
                d["url"] = 'https://shop.pluradent.de/praxisbedarf/ersatzteile-praxis.html'
                l.append(d)
            
             df2 = pandas.DataFrame(l)
             df2.to_csv( file + '.csv') 
             df2.to_excel(outpath +file+ '.xlsx',sheet_name = sheet_out)
        



    #-----------------------------------------------------------------------------
    #Product Level 0 - infos auf der Übersichtsseite
    #---------------------------------------------------------------------
    cat_label = 'Produkt_0'
    file = cat_label + '_'  + current_cat
    with open(logfile,'a') as f:
        f.write('\n\n' + cat_label + ' wird ausgelesen' + '\n\n' )
    
    print('---------------------------------------------------------------------')
    print('Produkt Level - 0 wird ausgelesen')
    print('---------------------------------------------------------------------')
    I = 0
    J = 0
    K = 0
    overall_pos = 0
    l = [];l2=[]
    if request_prod0 == 0:
        print("\n\timport dataframe from excel")
        df3 = pandas.read_excel(outpath +file + '.xlsx',sheet_name = sheet_out)
        with open(logfile,'a') as f:
            f.write('\n\t' + sheet_out + ' aus ' + file + ' gelesen' )
    elif request_prod0 == 1:
        for index,row in df2.iterrows():
             I = I+1
             if row["Kategorie - Level1"] != row["Kategorie - Level2"]:
                 print ("I=",I,"/", str(row["Kategorie - Level1"]),"/",row["Kategorie - Level2"])
                 print (row["url"])
                 url = row["url"]
                 with open(logfile,'a') as f:
                     f.write('\n\t' + str(row["Kategorie - Level1"]) + ' / ' + row["Kategorie - Level2"] + ' / '  + row["url"]) 
                
        #url = 'https://shop.pluradent.de/praxisbedarf/pluline-qualitaetsprodukte/praxismaterial/abformung.html'
                 r3 = requests.get(url);cr = cr+1
                 c3 = r3.content
                 soup3 = BeautifulSoup(c3,"html.parser")
        
                 #count pages
                 try:
                     pages = soup3.find_all("div",{"class":"pages"})
                     pages2 = pages[0].find_all("a")
                     K = 0
                     pagecount = 0
                     for page in pages2:
                         K= K+1
                         if page.text.isdigit():
                             pagecount = max(int(page.text),pagecount)
                 except:
                     pagecount = 1
                 
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
                
                     
                     
    
                 #anzahl positionen
                 positions = soup3.find("div",{"class":"amount"})
                 positions = positions.text.replace('\n','').strip()
                 try:
                     m = re.search('(\d+)\sPos', positions)
                     positions = int(m.group(1))
                 except:
                    m = re.search('(\d+)\s', positions)
                    positions = int(m.group(1))
                 overall_pos = overall_pos + positions                
                 pagecount2 = math.ceil(positions/elements)
                 try:            
                     with open(logfile,'a') as f:
                          f.write('\n\t\tpagecount= ' + str(pagecount))
                          f.write('\n\t\telements= ' + str(elements))
                          f.write('\n\t\tpositions= ' + str(positions))
                          f.write('\n\t\tpagecount2= ' + str(pagecount2))
                 except:
                     time.sleep(2)
                     with open(logfile,'a') as f:
                          f.write('\n\t\tpagecount= ' + str(pagecount))
                          f.write('\n\t\telements= ' + str(elements))
                          f.write('\n\t\tpositions= ' + str(positions))
                          f.write('\n\t\tpagecount2= ' + str(pagecount2))
                
                      
                 
                 #iterate
        #        for J in range(1,pagecount+1):
                 for J in range(1,pagecount2+1):
    #             for J in range(1,2):
                      
                     url_page = url+"?p="+str(J)
                     print(url_page)
        
        #read artikelnummer / url image / name / preis
        #url_page = 'https://shop.pluradent.de/praxisbedarf/pluline-qualitaetsprodukte/praxismaterial/abformung.html?p=1'
                     r4 = requests.get(url_page);cr = cr+1
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
                         
                         d2 = {}
                         d2["ArtikelNr"] = d["ArtikelNr"]
                         d2["Menge"] = 1
                         l2.append(d2)
                         
                         if len(l2) == 1000:
                             df5 = pandas.DataFrame(l2)
                             df5.set_index('ArtikelNr')
                             file2 = file + '_' + str(len(l))
                             df5.to_excel(outpath +file2+'.xlsx',sheet_name = sheet_out)
                             l2 = []
                     
            
#    print(l) 
        if 0 < len(l2) < 1000:
             df5 = pandas.DataFrame(l2)
             df5.set_index('ArtikelNr')
             file2 = file + '_' + str(len(l))
             df5.to_excel(outpath +file2+'.xlsx',sheet_name = sheet_out)
             l2 = []
    
        df3 = pandas.DataFrame(l)
        df3.to_csv( file + '.csv') 
        df3.to_excel(outpath +file+ '.xlsx',sheet_name = sheet_out)



    with open(logfile,'a') as f:
        f.write('\n\toverall - positions= ' + str(overall_pos))
        f.write('\n\t No of url access= ' + str(cr))
        f.write ('\n'+time.asctime( time.localtime(time.time()) ))

    
        
    #        "product-info--price "
        
    #-----------------------------------------------------------------------------
    #Product Level 1 - info von der spezifischen Produktseite
    #---------------------------------------------------------------------
    cat_label = 'Produkt Level - 1'
    with open(logfile,'a') as f:        
        f.write('\n\n' + cat_label + ' wird ausgelesen' + '\n\n' )

    print('---------------------------------------------------------------------')
    print('Produkt Level - 1 wird ausgelesen')
    print('---------------------------------------------------------------------')
    I = 0
    J = 0
    K = 0
    l = []
    l2=[]
    for index,row in df3.iterrows():
         I = I+1
         if I > 0:
             print ("I=",I,"/", row["Kategorie - Level1"],"/",row["Kategorie - Level2"])
             print (row["Name"],"/",row["ArtikelNr"])
             print (row["url"])
             url = row["url"]
             r5 = requests.get(url);cr = cr+1
             c5 = r5.content
             soup5 = BeautifulSoup(c5,"html.parser")
             #hersteller
             try:
                 hersteller = soup5.find("div",{"class":"product-detail-page--main--introduction--info--udxpluradentzzherbz"})
                 hersteller = hersteller.find("span",{"class":"value"}).text.replace("/n","").strip()
                 sku_hersteller = soup5.find("div",{"class":"product-detail-page--main--introduction--info--manufacturer_sku"})
                 sku_hersteller = sku_hersteller.find("span",{"class":"value"}).text.replace("/n","").strip()
                 try:
                     product_desc = soup5.find("div",{"class":"product-detail-page--main--details--desc"})
                     product_desc = product_desc.find("p").text.strip()
                 except:
                     product_desc = 'n.a.'
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
                 l2.append(d)
#                 alle Tausend artikel als Datei rausschreiben
                 if I % 1000 == 0:
                     df5 = pandas.DataFrame(l2)
                     df5.to_csv('Produkt - Level1 - ' + current_cat + '_' + str(I) + '.csv') 
                     l2 = []

             except:
                    err_message = 'I = ' + str(I) + ' \n url = ' + url + '\nFehler beim auslesen'
                    with open(logfile,'a') as f:
                        f.write('/n' + err_message)  

    
    #print(l) 
    
    df4 = pandas.DataFrame(l)
    df4.to_csv('Produkt - Level1 - ' + current_cat + '.csv') 

    
   
localtime = time.asctime( time.localtime(time.time()) )     


with open(logfile,'a') as f:
        f.write('end: ' + localtime)        
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











    
    





    






