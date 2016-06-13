


import urllib
import urllib2

url = 'https://chaboyams.schoolloop.com/'

req = urllib2.Request(url)
response = urllib2.urlopen(req)
the_page = response.read()