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
    statusCode = c.getinfo(pycurl.HTTP_CODE)
    c.close()
    if statusCode != 200:
        print "URL healthcheck failed:" + url
        content = storage.getvalue()
        print content
        sys.exit(1)
    print "URL healthcheck passed:" + url



f = open(configFileName)
lines = f.readlines()
f.close()

for item in lines:
    runHealthCheck(item)