from bs4 import  BeautifulSoup as soup
from urllib.request import urlopen as uReq
url = "https://www.flipkart.com/search?q=iphone&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_0_3_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_0_3_na_na_na&as-pos=0&as-type=RECENT&suggestionId=iphone%7CMobiles&requestId=eaf0a368-4390-4227-b06e-92dee26d197b&as-searchtext=iph"
uClient = uReq(url)
data_info = uClient.read()
uClient.close()
page_soup=soup(data_info,"html.parser") #parsing of information
containers = page_soup.findAll("div",{"class":"_3O0U0u"})
#print(len(containers))
#print(soup.prettify(containers[0]))
container=containers[0]
print(containers[0].text)

#print(container.div.img["alt"])

prices= page_soup.findAll("div",{"class":"col col-5-12 _2o7WAb"})
ratings=page_soup.findAll("div",{"class","niH0FQ"})
#print(prices[0].text)
with open('ProductInfo.csv', 'w', encoding='utf-8') as f:
     headers="Product Name, Price, Rating\n"
     f.write(headers)

     for container in containers:
      model = container.div.img["alt"]
      priceinfo=container.findAll("div",{"class":"col col-5-12 _2o7WAb"})
      price = priceinfo[0].text.strip()
      prorate=container.findAll("div",{"class","hGSR34"})
      ratings=prorate[0].text
      fprice=price[:7]

      frating=ratings[:3]
      print(model+","+fprice+","+frating+"\n")
      f.write(model+","+fprice+","+frating+"\n")
f.close()
