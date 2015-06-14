from BeautifulSoup import BeautifulSoup
import urllib2
import re

html_page = urllib2.urlopen("file:///home/manojpandey/Desktop/fb.html")
soup = BeautifulSoup(html_page)
for link in soup.findAll('a', href = re.compile(r'.*manojpandey1996/posts/*')):
    print link.get('href')