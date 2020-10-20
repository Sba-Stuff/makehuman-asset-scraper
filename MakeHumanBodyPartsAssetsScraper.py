import requests
from bs4 import BeautifulSoup
import re
import os
import urllib.request

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
		if "/clothes/" in str(link.get('href')) and not "page" in str(link.get('href')):
			#print(link.get('href'))
			links.append("http://makehumancommunity.org"+str(link.get('href')))
	return links
def scrape_download_links(urli):
    print(urli)
    url = "http://makehumancommunity.org"+"/clothes/"+urli+".html"
    req = requests.get(url, headers)
    soup = BeautifulSoup(req.content, 'html.parser')
    for link in soup.findAll('a'):
        if ".mhclo" in str(link.get('href')) or ".obj" in str(link.get('href')) or ".mhmat" in str(link.get('href')) or ".thumb" in str(link.get('href')):
            print(link.get('href'))
            print('Beginning file download with urllib2...')
            url4dl = str(link.get('href'))
            filer = url4dl.split("/")
            filll = filer[len(filer)-1]
            print(filll)
            urllib.request.urlretrieve(url4dl,"bodyparts/"+urli+"/"+filll)
            #print(link.get('href'))
    #print(ii)

def create_directory(name):
	if not os.path.exists(name):
    		os.mkdir(name)

def replace_string(string, fromi, toi):
	return string.replace(fromi, toi)

for pageno in range(0,3):
    #print("Scraping Page Number: "+str(pageno))
    #if pageno != 0:
    #    scraped_links = scraplinks("http://makehumancommunity.org/bodyparts.html?page="+str(pageno))
    #else:
    scraped_links = scraplinks("http://makehumancommunity.org/bodyparts.html?page=2")
    fnames = []
    for x in scraped_links:
    	g = replace_string(x,"http://makehumancommunity.org/clothes/","")
    	g = replace_string(g,".html","")
    	fnames.append(g)
    for fi in range(0,len(fnames)):
        create_directory("bodyparts/"+str(fnames[fi]))
        scrape_download_links(fnames[fi])
print("done")
#create_directory("ali")