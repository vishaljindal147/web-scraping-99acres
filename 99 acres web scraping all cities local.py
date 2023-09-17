from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import pandas as pd
import tabulate
import pymongo

path = "E:/System Folders/Chrome Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe"
s = Service(path)
browser = webdriver.Chrome(service=s)

url = ["https://www.99acres.com/search/property/buy/pune?keyword=pune&preference=S&area_unit=1&budget_min=0&res_com=R&isPreLeased=N",
       "https://www.99acres.com/search/property/buy/delhi?keyword=delhi&preference=S&area_unit=1&budget_min=0&res_com=R&isPreLeased=N",
       "https://www.99acres.com/search/property/buy/mumbai?keyword=mumbai&preference=S&area_unit=1&budget_min=0&res_com=R&isPreLeased=N",
       "https://www.99acres.com/search/property/buy/lucknow?keyword=lucknow&preference=S&area_unit=1&budget_min=0&res_com=R&isPreLeased=N",
       "https://www.99acres.com/search/property/buy/agra?keyword=agra&preference=S&area_unit=1&budget_min=0&res_com=R&isPreLeased=N",
       "https://www.99acres.com/search/property/buy/ahmedabad?keyword=ahmedabad&preference=S&area_unit=1&budget_min=0&res_com=R&isPreLeased=N",
       "https://www.99acres.com/search/property/buy/kolkata?keyword=kolkata&preference=S&area_unit=1&budget_min=0&res_com=R&isPreLeased=N",
       "https://www.99acres.com/search/property/buy/jaipur?keyword=jaipur&preference=S&area_unit=1&budget_min=0&res_com=R&isPreLeased=N",
       "https://www.99acres.com/search/property/buy/chennai?keyword=chennai&preference=S&area_unit=1&budget_min=0&res_com=R&isPreLeased=N",
       "https://www.99acres.com/search/property/buy/bengaluru?keyword=Bengaluru&preference=S&area_unit=1&budget_min=0&res_com=R&isPreLeased=N"]

cities = ["Pune","Delhi","Mumbai","Lucknow","Agra","Ahmedabad","Kolkata","Jaipur","Chennai","Bengaluru"]

data = {"Property name":[], "Property price":[], "Property type":[], "Property area":[], "Property locality":[], "Property link":[],"Property City":[]}
# time.sleep(15)

property_name_list = []
price_list = []
property_type_list = []
final_property_type_list = []
property_area_list = []
final_property_area_list = []
property_locality_list = []
final_property_locality_list = []
individual_property_link = []
property_city = []

data_extra = {"Property name extra":[],"Property price extra":[],"Property type extra":[],"Property area extra":[],"Property society extra":[], "Property link extra": [], "Property city extra": []}

Property_name_extra = [] 
Property_society_extra = []
final_Property_price_extra = []
Property_price_extra = []
Property_price_unit_extra = []
Property_area_extra = []
Property_type_extra = []
Property_link_extra = []
Property_society_extra = []
property_city_extra = []


# final_data = {"final_property_name" :[],"final_property_price" : [],"final_property_area" : [],"final_property_type" : [],"final_property_locality" : [],"final_property_link" : []}

# url = "https://www.99acres.com/property-in-bangalore-ffid-page-8"

index_u = 0

for index_u in range(len(url)):
    browser.get(url[index_u])

    for g in range (100):
        time.sleep(3)
        # print("str")
        property_name_list = browser.find_elements(By.CLASS_NAME,"projectTuple__projectName")
        for a in property_name_list:
            # print(a.text)
            data["Property name"].append(a.text)
            name = cities[index_u]
            data["Property City"].append(name)


        price_list = browser.find_elements(By.CSS_SELECTOR,".list_header_bold.configurationCards__srpPriceHeading.configurationCards__configurationCardsHeading")
        for p in price_list:
            # print(p.text)
            data["Property price"].append(p.text)


        property_type_list = browser.find_elements(By.CSS_SELECTOR,".configurationCards__cardsWrapper.configurationCards__srpCardStyle")
        for d in property_type_list:
            temp = (d.find_element(By.TAG_NAME,"span").text)
            final_property_type_list.append(temp)
            data["Property type"].append(temp)
            

        property_area_list = browser.find_elements(By.CSS_SELECTOR,".configurationCards__cardsWrapper.configurationCards__srpCardStyle")
        for e in property_area_list:
            try:
                temp = e.find_element(By.CSS_SELECTOR,".caption_subdued_medium.configurationCards__cardAreaSubHeadingOne").text
                final_property_area_list.append(temp)
                data["Property area"].append(temp)
            except Exception as e:
                print("property area list exception:",e)
                pass

        property_locality_list = browser.find_elements(By.CSS_SELECTOR,".configurationCards__cardsWrapper.configurationCards__srpCardStyle")
        for y in property_locality_list:
            try:
                temp = y.find_element(By.CSS_SELECTOR,".list_header_semiBold.configurationCards__configBandLabel").text
                final_property_locality_list.append(temp)
                data["Property locality"].append(temp)
            except Exception as e:
                pass

        # print(final_property_locality_list)

        individual_property_link = browser.find_elements(By.CLASS_NAME,("projectTuple__projectName"))

        for a in individual_property_link:
            temp = a.get_attribute("href")
            # print(temp)
            data["Property link"].append(temp)

        # print(data)
        # print(len(property_name_list),len(price_list),len(final_property_type_list),len(final_property_area_list),len(final_property_locality_list),len(individual_property_link))

        i=1
        for a in property_name_list:
            # print("i:",i,a.text)
            i+=1
        # print(len(property_name_list))

        i=1
        for a in price_list:
            # print("i:",i,a.text)
            i+=1
        # print(len(price_list))

        i = 1
        for a in final_property_type_list:
            print("rtpe i:",i,a)
            i+=1
        # print(len(final_property_type_list))

        i = 1
        for a in final_property_area_list:
            # print("i:",i,a)
            i+=1
        # print(len(final_property_area_list))

        i = 1
        for a in final_property_locality_list:
            print("locality i:",i,a)
            i+=1
        # print(len(final_property_locality_list))

        i = 1
        for a in individual_property_link:
            # print("i:",i,a.get_attribute("href"))
            i+=1
        # print(len(individual_property_link))

        Property_name_extra = browser.find_elements(By.ID,"srp_tuple_society_heading")
        for p in Property_name_extra:
            # print(p.text)
            data_extra["Property name extra"].append(p.text)
            data_extra["Property city extra"].append(cities[index_u])

        final_Property_price_extra = browser.find_elements(By.ID,"srp_tuple_price") 
        # print(len(final_Property_price_extra))
        for p in final_Property_price_extra:
            # print(p.text)
            data_extra["Property price extra"].append(p.text)

        Property_area_extra = browser.find_elements(By.ID,"srp_tuple_primary_area")
        for p in Property_area_extra:
            # print(p.text)
            data_extra["Property area extra"].append(p.text)

        Property_type_extra = browser.find_elements(By.ID,"srp_tuple_bedroom")
        for p in Property_type_extra:
            print("type",p.text)
            data_extra["Property type extra"].append(p.text)

        Property_society_extra = browser.find_elements(By.CLASS_NAME,"srpTuple__tupleTitleOverflow")
        for p in Property_society_extra:
            print("society",p.text)
            data_extra["Property society extra"].append(p.text)

        Property_link_extra = browser.find_elements(By.CSS_SELECTOR,".body_med.srpTuple__propertyName")
        for p in Property_link_extra:
            s = p.get_attribute("href")
            data_extra["Property link extra"].append(s)
        # print(len(Property_name_extra),len(Property_price_extra),len(Property_area_extra),len(Property_type_extra),len(Property_society_extra))


        try:
            # next_page_list = []
            # next_page_list = browser.find_elements(By.CLASS_NAME,"list_header_bold")
            # # next = next_list[1]
            # next_page_index = len(next_page_list) - 1
            # next_page = next_page_list[next_page_index]
            # print(next_page.get_attribute("href"))
            # browser.get(next_page.get_attribute("href"))
            p = 0
            
            g = browser.find_elements(By.XPATH,"""//a[@class="list_header_bold"]""")
            le = len(g)
            b = g[le - 1] 
            print(b.text)
            try:
                browser.execute_script("arguments[0].click()",b)
                print("Working")
            except Exception as e:
                print("Not working")
                print(e)
        except:
            pass
        # time.sleep(4)
        p += 1

    index_u += 1 

df = pd.DataFrame(data)
print(df)
print("\n\n")
df_extra = pd.DataFrame(data_extra)
df.columns = ["Property name", "Property price", "Property type", "Property area", "Property locality/Type (if locality not provided)", "Property link","Property City"]
df_extra.columns = ["Property name", "Property price", "Property type", "Property area", "Property locality/Type (if locality not provided)", "Property link","Property City"]
cd = pd.concat([df,df_extra],ignore_index=True)
print(df_extra)
print(cd)


cd.to_csv("Property.csv", encoding='utf-8', index=False)        # Writing it in a csv file

client = pymongo.MongoClient("mongodb://localhost:27017") 

# client = pymongo.MongoClient("mongodb+srv://vishal:property@cluster0.fztwz7i.mongodb.net/?retryWrites=true&w=majority&appName=AtlasApp") # Kindly uncomment it if it is to be connected over a network
print(client)
client.drop_database('property')    # Dropping previous database
db = client['property']             # Creating database

collection = db['bangalore_property']       # Creating tablwe


cd.reset_index(drop = True)     # Dropping index
ef = cd.to_dict(orient="records")
collection.insert_many(ef) # Inserting record wise
print("\n\n\:",ef)
browser.close()
