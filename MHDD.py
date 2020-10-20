import requests
from bs4 import BeautifulSoup
import re
import os
import urllib.request
mainpage_url = "custom"
child_page_url = "content"
model_folder = "customcontent"
number_of_pages = 1

headers = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Max-Age': '3600',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
    }



def scraplinks(urli):
	links = []
	url = urli
	req = requests.get(url, headers)
	soup = BeautifulSoup(req.content, 'html.parser')
	for link in soup.findAll('a'):
    		#print(link.get('href'))
		if "/"+child_page_url+"/" in str(link.get('href')) and not "page" in str(link.get('href')):
			#print(link.get('href'))
			links.append("http://makehumancommunity.org"+str(link.get('href')))
	return links
def scrape_download_links(urli):
    print(urli)
    url = "http://makehumancommunity.org"+"/"+child_page_url+"/"+urli+".html"
    req = requests.get(url, headers)
    soup = BeautifulSoup(req.content, 'html.parser')
    for link in soup.findAll('a'):
        try:
            if ".zip" in str(link.get('href'))  or ".blend" in str(link.get('href')) and not "windows.zip" in str(link.get('href')):
                print(link.get('href'))
                print('Beginning file download with urllib2...')
                url4dl = str(link.get('href'))
                filer = url4dl.split("/")
                filll = filer[len(filer)-1]
                print(filll)
                urllib.request.urlretrieve(url4dl,model_folder+"/"+urli+"/"+filll)
        except:
            pass
                #print(link.get('href'))
    #print(ii)

def create_directory(name):
	if not os.path.exists(name):
    		os.mkdir(name)

def replace_string(string, fromi, toi):
	return string.replace(fromi, toi)

for pageno in range(0,number_of_pages):
    print("Scraping Page Number: "+str(pageno))
    if pageno != 0:
        scraped_links = scraplinks("http://makehumancommunity.org/"+mainpage_url+".html?page="+str(pageno))
    else:
        scraped_links = scraplinks("http://makehumancommunity.org/"+mainpage_url+".html")
    #print(scraped_links)
    fnames = []
    for x in scraped_links:
    	g = replace_string(x,"http://makehumancommunity.org/"+child_page_url+"/","")
    	g = replace_string(g,".html","")
    	fnames.append(g)
    for fi in range(0,len(fnames)):
        create_directory(model_folder+"/"+str(fnames[fi]))
        scrape_download_links(fnames[fi])
print("done")
#create_directory("ali")