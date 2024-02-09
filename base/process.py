import pandas as pd
from bs4 import BeautifulSoup
import requests
from fake_useragent import UserAgent
import difflib
import os
agent = UserAgent()
def scrap_amazon(product):
    url = "https://www.amazon.in/s?k=" + product
    headers = {
        'authority': 'www.amazon.in',
        'pragma': 'no-cache',
        'cache-control': 'no-cache',
        'dnt': '1',
        'upgrade-insecure-requests': '1',
        'user-agent': agent.random,
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-fetch-site': 'none',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-dest': 'document',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    }
    
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    product_info_elements = soup.find_all("span", class_="a-size-medium a-color-base a-text-normal")
    product_price_elements = soup.find_all("span", class_="a-price-whole")
    
    product_name_details = []
    product_price_details = []
    
    for product_info_element in product_info_elements:
        product_name = product_info_element.text
        product_name_details.append(product_name)
    
    for product_price_element in product_price_elements:
        product_price = product_price_element.text
        product_price_details.append(product_price)
    
    max_length = max(len(product_name_details), len(product_price_details))
    df = pd.DataFrame({'Product_name': product_name_details + [None] * (max_length - len(product_name_details)),
                       'Product_price': product_price_details + [None] * (max_length - len(product_price_details))})
    
    excel_file_path = 'amazon_data.xlsx'
    current_directory = os.getcwd()
    
    # Create the full path for the Excel file in the current directory
    excel_file_path = os.path.join(current_directory, 'amazon_data.xlsx')
    df.to_excel(excel_file_path, index=False)
    
    print("Amazon data scrapped")
def scrap_flipkart(product):
    agent=UserAgent()
    url = "https://www.flipkart.com/search?q="+product
    headers = {
            'authority': 'www.amazon.com',
            'pragma': 'no-cache',
            'cache-control': 'no-cache',
            'dnt': '1',
            'upgrade-insecure-requests': '1',
            'user-agent':agent.random,
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'sec-fetch-site': 'none',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-dest': 'document',
            'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    }
    response = requests.get(url,headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    product_info_elements = soup.find_all("div", class_="_4rR01T")
    product_price_elements = soup.find_all("div", class_="_30jeq3")
    product_name_details = []
    product_price_details = []

    for product_info_element in product_info_elements:
        product_name = product_info_element.text
        product_name_details.append(product_name)
    for product_price_element in product_price_elements:
      product_price = product_price_element.text
      product_price_details.append(product_price)
      #print(product_price_details)
 
    max_length = max(len(product_name_details),len(product_price_details))
    df = pd.DataFrame({'Product_name': product_name_details + [None] * (max_length - len(product_name_details)), 'Product_price': product_price_details + [None] * (max_length - len(product_price_details))})
    excel_file_path = 'flipkart_data.xlsx'
    current_directory = os.getcwd()
    print(os.getcwd())
    excel_file_path = os.path.join(current_directory, 'flipkart_data.xlsx')
    df.to_excel(excel_file_path, index=False)
    print("flipkart data scrapped")

def comparison_product_amazon(product_name):
    product_name=product_name.upper()
    read_file=pd.read_excel('amazon_data.xlsx')
    amazon=find_close_match(product_name,read_file,0.10)
    for i in range(0,len(amazon)):
       print("%d for %s" %(i+1,amazon[i][0]))
    exect_product=int(input("In this list select any one appropriate product!!! by any one number"))
    amazon_get=amazon[exect_product-1][0]
    print(amazon_get+":Your selection!!!")
    amazon=find_close_match(amazon_get,read_file,0.60)
    gemini_use(read_file,amazon_get)
    #print(amazon)
def find_close_match(product_name,read_file,cutoff):
   sorted_values=read_file.sort_values('Product_price',ascending=True)
   similar_products = []
   for index, row in sorted_values.iterrows():
        product_title = row['Product_name']
        product_price = row['Product_price']
        #print(product_title,product_price)
        if isinstance(product_title, str):
         similar_titles = difflib.get_close_matches(product_name,[product_title], n=1, cutoff=cutoff)
         if similar_titles:
            similar_product_title = similar_titles[0]
            similar_products.append((similar_product_title, product_price))
   print(len(similar_products)) 
   return similar_products
def comparison_product_flipkart(product_name):
    product_name=product_name.upper()
    parent_directory=os.getcwd()
    excel_file_path_flipkart = os.path.join(parent_directory, 'flipkart_data.xlsx')
    read_file=pd.read_excel(excel_file_path_flipkart)
    excel_file_path_amazon=os.path.join(parent_directory, 'amazon_data.xlsx')
    file_read_amazon=pd.read_excel(excel_file_path_amazon)
    flipkart=find_close_match(product_name,read_file,0.10)
    # for i in range(0,len(flipkart)):
    #    print("%d for %s" %(i+1,flipkart[i][0]))
    return flipkart
    # flipkart_get=flipkart[exect_product-1][0]
    # print(flipkart_get+":Your selection!!!")
    # flipkart=find_close_match(flipkart_get,read_file,0.10)
    # conent=[]
    #gemini.gemini(read_file,flipkart_get)
    # for item in flipkart:
    #    conent.append(item)
       #print(item)
    #print(conent)
    # gemini_use(conent,flipkart_get)
def gemini_use(list,product):
    import google.generativeai as genai
    import os
    os.environ['GOOGLE_API_KEY']='AIzaSyBlyUe_82tAOYTqHwaohgEx9hiMLEyFbKo'
    genai.configure(api_key='AIzaSyBlyUe_82tAOYTqHwaohgEx9hiMLEyFbKo')
    genai.configure(api_key=os.environ['GOOGLE_API_KEY'])
    model = genai.GenerativeModel('gemini-pro')
    req="i have created the comparison between multiple ecomerce platforms when user enters the particular product in my website i will scrap in that product in multiple e-commmerce platfoms but the product are very syntactically similar but sementically not similar"
    gen=str(list)
    ques=",  in this given data find only '{}' and if the two products matches with theier names then you can take that into your account and you can take all the matching thing print like strictly ['product1='price1'*'product2=price2'*'product3=price3'*'product4=price4]".format(product)
    explanation="always follow the the above pattern of output please, then only i can split them and use for result and if u select the particular data take complete title for that ok and give it in above structure output and please dont look into multiple datas if the basic name of product in list matches and if you notice that they are same products take it"
    response = model.generate_content(req+gen+ques+explanation)
    #print(response.text)
    return response.text
def comparison_product_flipkart_amazon(product_name):
    print(product_name)
    product_name=str(product_name)
    product_name.upper()
    parent_directory=os.getcwd()
    excel_file_path_flipkart = os.path.join(parent_directory, 'flipkart_data.xlsx')
    read_file=pd.read_excel(excel_file_path_flipkart)
    excel_file_path_amazon=os.path.join(parent_directory, 'amazon_data.xlsx')
    file_read_amazon=pd.read_excel(excel_file_path_amazon)
    flipkart=find_close_match(product_name,read_file,0.05)
    amazon=find_close_match(product_name,file_read_amazon,0.05)
    # print(flipkart)
    # print(amazon)
    # print("_____________________________________________________________________________________")
    #print(flipkart)
    flipkart=gemini_use(flipkart,product_name)
    amazon=gemini_use(amazon,product_name)
    #print("this is flipkart",flipkart)
   #print("this is amazon",amazon)
    return flipkart,amazon
   # print(flipkart)

    
def main_allocate(user_product):
    scrap_flipkart(user_product)
    scrap_amazon(user_product)