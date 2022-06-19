import pycurl
import certifi
from io import BytesIO
from urllib.parse import urlencode
# Creating a buffer as the cURL is not allocating a buffer for the network response
buffer = BytesIO()
c = pycurl.Curl()
#initializing the request URL
c.setopt(c.URL, 'http://127.0.0.1:8000/history/%d'%c.getinfo(c.RESPONSE_CODE))
#setting options for cURL transfer
c.setopt(c.WRITEDATA, buffer)
#setting the file name holding the certificates
c.setopt(c.CAINFO, certifi.where())
# perform file transfer
c.perform()
#Ending the session and freeing the resources
c.close()