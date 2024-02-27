import requests
from bs4 import BeautifulSoup
import re
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())

techonlogies= {}
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

def fetch_with_selenium(url):
    
    # Konfiguracja Selenium z WebDriver Manager
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-images")
    #service = Service(ChromeDriverManager().install())
    browser = webdriver.Chrome(service=service, options=chrome_options)

    browser.get(url)
    page_content = browser.page_source
    browser.quit()
    tech_regex = re.compile(r'{"name":"([a-zA-Z-#,.!@#$%^&*(1234567890]{1,40})"}')
    match= tech_regex.findall(page_content)
    for tech in match:
        if tech in techonlogies:
            techonlogies[tech] +=1
        else:
            techonlogies[tech]= 1
    
    print(techonlogies)
    return 




url = "https://it.pracuj.pl/praca?pn=" 
content = get_page_content(url)
max_pages= find_number_of_pages(content)

for i in range(1, int(max_pages)):
    page_url= url+str(i)
    print(page_url)
    content = get_page_content(page_url)
    find_links_to_surveys(content)
    print(len(links))

#print("ogloszenie link: 0", links_to_surveys[3])

for link in links:
    fetch_with_selenium(link)
print("final: ", techonlogies)

#dynamic_content= fetch_with_selenium(links_to_surveys[3])
#print(dynamic_content)
f = open("technologie_dict.txt", "w", encoding='utf-8')
f.write(str(techonlogies)+"\n")
f.close()
#print("slownik", techonlogies)
# dictionaryName":"ItTechnologies","customItems":\[(.+)],"items"

#for link in links_to_surveys:
#    print("ogloszenie: " ,link)
#    dynamic_content= fetch_with_selenium(link)   
#   print(dynamic_content)