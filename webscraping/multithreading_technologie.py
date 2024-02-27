import requests
from bs4 import BeautifulSoup
import re
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import concurrent.futures

service = Service(ChromeDriverManager().install())
test= [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]

techonlogies1= {}
techonlogies2= {}
techonlogies3= {}
techonlogies4= {}

links= []
def get_page_content(url):
    response = requests.get(url)
    return response.text

def find_number_of_pages(content):
    pages_number_regex = re.compile('max-page-number">(\d+)')
    match= pages_number_regex.search(content)
    return match.group(1)

def find_links_to_surveys(content):
    link_regex = re.compile(r'href="(https://www.pracuj.pl/praca/[^\s"]+)"')
    double_links = link_regex.findall(content)
    
    for i in range(0, len(double_links), 2):
        links.append(double_links[i])
    
    #f = open("linki_do_ogloszen.txt", "w", encoding='utf-8')
    #for link in links:
     #   f.write(str(link)+"\n")
    #f.close()
    return 

def fetch_with_selenium(url, dict, thread_number):
    
    # Konfiguracja Selenium z WebDriver Manager
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-images")
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
    #service = Service(ChromeDriverManager().install())
    browser = webdriver.Chrome(service=service, options=chrome_options)

    browser.get(url)
    page_content = browser.page_source
    browser.quit()
    tech_regex = re.compile(r'{"name":"([a-zA-Z-#,.!@#$%^&*(1234567890]{1,40})"}')
    match= tech_regex.findall(page_content)
    for tech in match:
        if tech in dict:
            dict[tech] +=1
        else:
            dict[tech]= 1
    
    #print(thread_number,": ", dict)
    return 




url = "https://it.pracuj.pl/praca?pn=" 
content = get_page_content(url)
max_pages= find_number_of_pages(content)

for i in range(1, int(8)):
    page_url= url+str(i)
    print(page_url)
    content = get_page_content(page_url)
    find_links_to_surveys(content)
    print(len(links))

#print("ogloszenie link: 0", links_to_surveys[3])
cw1= links[:len(links)//4]
cw2= links[len(links)//4*1:len(links)//2]
cw3= links[len(links)//4*2:len(links)//4*3]
cw4= links[len(links)//4*3:len(links)]

def process_links(cw, dict, n):
    for link in cw:
        fetch_with_selenium(link, dict,n)
    print(f"watek {n}: ", dict)
    name= f"watek{n}.txt"
    f = open(name, "w", encoding='utf-8')
    f.write(str(dict)+"\n")
    f.close()
    #print("final: ", techonlogies)
        
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
    executor.submit(process_links, cw1, techonlogies1, 1)
    executor.submit(process_links, cw2, techonlogies2, 2)
    #executor.submit(process_links, cw3, techonlogies3, 3)
    #executor.submit(process_links, cw4, techonlogies4, 4)
#dynamic_content= fetch_with_selenium(links_to_surveys[3])
#print(dynamic_content)
#f = open("technologie_dict.txt", "w", encoding='utf-8')
#f.write(str(techonlogies)+"\n")
#f.close()
#print("slownik", techonlogies)
# dictionaryName":"ItTechnologies","customItems":\[(.+)],"items"

#for link in links_to_surveys:
#    print("ogloszenie: " ,link)
#    dynamic_content= fetch_with_selenium(link)   
#   print(dynamic_content)
