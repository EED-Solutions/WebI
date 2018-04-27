#This programm will read out article numbers from the pluradent webshop


#import libraries
import requests
import bs4

#main function
def main(web = 1):
    #returns 1, if no error
    if web == 1:
        print("web1")
        url = 'https://shop.pluradent.de/'
    else:
        print("web0")
        url = 'n.a.'
    
    print(url)
    return "1"

L = main(1)
print(L)



