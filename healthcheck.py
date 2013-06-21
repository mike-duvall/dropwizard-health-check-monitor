from StringIO import StringIO
import pycurl
import sys


configFileName = sys.argv[1]
print "Reading config file:" + configFileName


def runHealthCheck(url):
	print "Checking URL:" + url
	storage = StringIO()
	c = pycurl.Curl()
	c.setopt(pycurl.URL, url )
	c.setopt(pycurl.FOLLOWLOCATION, 1)
	c.setopt(c.WRITEFUNCTION, storage.write)
	c.perform()
	c.close()
	content = storage.getvalue()
	if "ERROR" in content:
		print content
		sys.exit(1)
	print "URL healthcheck passed:" + url



f = open(configFileName)
lines = f.readlines()
f.close()

for item in lines:
	print item
	runHealthCheck(item)


