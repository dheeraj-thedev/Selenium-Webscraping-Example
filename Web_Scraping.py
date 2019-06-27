#Importing libraries
# If not avaialble use pip install bs4 to install the below mentioned library
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

my_url = 'https://www.flipkart.com/laptops/~gaming/pr?count=40&p%5B%5D=sort%3Dpopularity&sid=6bo%2Fb5g&wid=4.productCard.PMU_V2_2'

uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

#print(page_html)

page_soup = soup(page_html, 'html.parser')

print(type(page_soup))
print(page_soup)

containers = page_soup.findAll('div', {'class':'_3O0U0u'})

print(len(containers))
print(containers)

print(soup.prettify(containers[0]))


container=containers[1]
#print(container)

p = container.findAll('div',{'class':'_6BWGkk'})
p[0].text



filename = "Laptops.csv"
f = open(filename,"w")
headers = "Product_name, Pricing, Rating"
f.write(headers +"\n")

for i in containers:
    product_name = i.div.img['alt']
    
    price_container = i.findAll('div',{'class':'_6BWGkk'})
    price = price_container[0].text.strip()
    
    rating_container = i.findAll('div',{'class':'hGSR34'})
    rating = rating_container[0].text
    
    
#     print("Product :" + product_name)
#     print("Price : " + price)
#     print("Ratings :" + rating)
#     break
#String Parsing
    trim_price = "".join(price.split(','))
    rm_rupee = trim_price.split("₹")
    final_price = rm_rupee[1]
    
    final_rating = rating[0:3]
#   print(product_name.replace(",",'|')+ "," + final_price + ',' + final_rating +'\n')
    f.write(product_name.replace(",",'|')+ "," + final_price + ',' + final_rating +'\n')

f.close()

#import os
#os.remove("Laptops.csv")

# yOU MIGHT HAVE TO INSTALL PANDAS -> pip install pandas
import pandas as pd
df = pd.read_csv("Laptops.csv")
df.tail()
df.describe()

