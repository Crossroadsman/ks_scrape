'''
Both packages are available through pip:
> pip install beautifulsoup4
> pip install requests
'''
import requests
from bs4 import BeautifulSoup

TARGET = 'http://gregminuskin.com'

r = requests.get(TARGET)

# Make sure we got a result
# Check the status code and the headers:
print(r.status_code)
print(r.headers)

# Store the content in a variable
# (content is the response body as bytes (for non-text requests);
#  text is the response body after `encoding` has been applied)
# To avoid Mojibake issues, we always want to pass beautiful soup the
# bytes content and let bs handle the encoding.
c = r.content

# fix `c` by replacing malformed characters
# (some malformed characters, especially windows smart quotes, seem to
# be impossible to fix with bs (or even unicodedammit), so we're just
# replacing all instances with straight quotes before we pass the content
# to bs)
c = c.replace(b"&#8217;", b"'")
c = c.replace(b"&#8220;", b'"')
c = c.replace(b"&#8221;", b'"')
print(c)

# Now do the parsing with beautiful soup
#parser = 'html.parser'
soup = BeautifulSoup(c)
print(soup.original_encoding) # bs's guess on encoding

# We can see the html in a minimally prettified way:
#pretty = soup.prettify()
#print(pretty)


# We can look at the paragraphs:
ps = soup.find_all('p')
for p in ps:
    try:
        print(p.string)
    except UnicodeEncodeError as inst:
        print(p.string.encode("utf8"))
        print(inst)

'''
text = soup.get_text()
print(text)
'''
