import requests
from bs4 import BeautifulSoup
import pandas as pd

Product_name = []
Prices = []
Description = []
Reviews = []


#get all page link so using for loops
# for i in range(2,10):
    
     # url = "https://www.flipkart.com/search?q=mobiles+under+50000&as=on&as-show=on&otracker=AS_Query_OrganicAutoSuggest_1_15_na_na_na&otracker1=AS_Query_OrganicAutoSuggest_1_15_na_na_na&as-pos=1&as-type=HISTORY&suggestionId=mobiles+under+50000&requestId=4a122e40-7212-4263-b7a4-f756daaaf375&page="+str(1)
     # r = requests.get(url) #it gives the total responces counting from the html code
     # print(r)

     # soup = BeautifulSoup(r.text,"lxml") #it gives the whole html code
     # # print(soup)

     # while True:
        #np = soup.find("a" , class_ ="_1LKTO3").get("href") #it give the next page link which is non-clickable
        #print(np)
        #cnp = "https://www.flipkart.com"+np #it make the above link cliackable by adding domain name 
        #print(cnp)

        #it gives the next page link
        #url = cnp
        #r = requests.get(url)
        #soup = BeautifulSoup(r.text,"lxml")


#printing all pages
for i in range(2,12):
    
    url = "https://www.flipkart.com/search?q=mobiles+under+50000&as=on&as-show=on&otracker=AS_Query_OrganicAutoSuggest_1_15_na_na_na&otracker1=AS_Query_OrganicAutoSuggest_1_15_na_na_na&as-pos=1&as-type=HISTORY&suggestionId=mobiles+under+50000&requestId=4a122e40-7212-4263-b7a4-f756daaaf375&page="+str(i)
    r = requests.get(url) #it gives the total responces counting from the html code
    #print(r)
    soup = BeautifulSoup(r.text,"lxml")

    box = soup.find("div", class_="_1YokD2 _3Mn1Gg") #it is use to call in a particular class

    names = box.find_all("div", class_ = "_4rR01T") #it gives the calling class html code total thing
    # print(names)
    for i in names: #here it get the only names
        name = i.text
        Product_name.append(name)
    # print(Product_name)
    # print(len(Product_name)) #lenth of names it give total

    prices = box.find_all("div", class_ = "_30jeq3 _1_WHN1")
    for i in prices:
        name = i.text
        Prices.append(name)
    # print(Prices)

    desc = box.find_all("ul", class_="_1xgFaf")
    for i in desc:
        name = i.text
        Description.append(name)
    # print(Description )

    reviews = box.find_all("div", class_="_3LWZlK")
    for i in reviews:
       name = i.text
       Reviews.append(name)
    # print(Reviews )

#print all data in a row and coulmn format
df = pd.DataFrame({"Product_name":Product_name,"Prices":Prices,"Description":Description,"Reviews":Reviews})
# print(df)

#all data store in Excel sheet 
df.to_csv("flipkart_mobiles_under_50000.csv")
