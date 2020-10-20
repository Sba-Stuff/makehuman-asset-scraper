# makehuman-asset-scraper

As A 3D modeler and animator, I use Make Human for creating 3D character models. Make human is a free 3D character modeling software supported by its huge fans (community). Assets provided with software are very few. So, community creates different assets for 3d characters to bring variation. The problem is, these assets are not few that one can download. Moreover, I need all of the assets for bad time. Visiting link individualy and downloading all assets is not easy for me. So I created a scrapper for downloading all the assets from site at once. It creates folders with asset name, and throws all the asset files in that folder that I can reuse later. I Hope you will like this script and use it if you are a 3d Modeler Too.

How to run:

Make a Folder With Asset name like for clothes "clothes" With different scrappers I provided.
Make sure python.exe, that asset folder and scrapper scrips will be in the same place.
Open CMD at same place. And then type: python.exe <your script name>
Leave the rest on script.

Kind Note:
MHDD.py is dynamic file for downloading content.
You have to change following parameters at top of script to run perfectly;

mainpage_url = "custom" (this is what comes after in url for asset like in this link; "http://makehumancommunity.org/targets.html" url has targets.html so you have to put what is before html.


child_page_url = "content" (When you open suppose targets.html you see the list of contents having title, category etc. Hover over a link you see the child page url suppose for targets.html, one of the content link like Elf Series: ears has download url like http://makehumancommunity.org/target/elf_series_ears.html , so you put what comes after .org/ and before the content name/ in above example it is target)

model_folder = "customcontent" (This is folder where you throw all assets, you have to created that folder manually.)

number_of_pages = 1 (Number of pages that assets have, like for targets.html, the content pages are 6. So you have to put 6 in there)


Also you have to change the condition:
if ".zip" in str(link.get('href'))  or ".blend" in str(link.get('href')) and not "windows.zip" in str(link.get('href')):

To what ever you like, For example the targets content contains content with file name ".target" so you change above url to
if ".target" in str(link.get('href')):


I hope you will like this effort.


