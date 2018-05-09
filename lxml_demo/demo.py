'''The necessary packages can be installed with pip
'''
import lxml.html
import requests

url = 'http://econpy.pythonanywhere.com/ex/001.html'

r = requests.get(url)

t = r.text  # unicode
c = r.content  # bytes

# Note that with lxml we need to use .content because html.fromstring
# implicitly expects bytes as input
tree = lxml.html.fromstring(c)

# we can use the xpath method to create XPath queries.
