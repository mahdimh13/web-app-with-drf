import pycurl
from urllib.parse import urlencode

c = pycurl.Curl()
#initializing the request URL
c.setopt(c.URL, 'http://127.0.0.1:8000/create/')
#the data that we need to Post
post_data = {'key': 'value'}
# encoding the string to be used as a query
postfields = urlencode(post_data)
#setting the cURL for POST operation
c.setopt(c.POSTFIELDS, postfields)
# perform file transfer
c.perform()
#Ending the session and freeing the resources
c.close()