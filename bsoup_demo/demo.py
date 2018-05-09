'''
Both packages are available through pip:
> pip install beautifulsoup4
> pip install requests
'''
import requests
import bs4

TARGET = 'http://scripting.com'

r = requests.get(TARGET)

# Make sure we got a result
# Check the status code and the headers:
print(r.status_code)
print(r.headers)

# Store the content in a variable
# (content is the content in bytes; text is the content in unicode)
c = r.content
t = r.text
encoding = r.encoding

# Now do the parsing with beautiful soup
parser = 'html.parser'
soup = bs4.BeautifulSoup(c, parser)

# We can see the html in a minimally prettified way:
pretty = soup.prettify(encoding)
print(pretty)

# We can look at the paragraphs:
ps = soup.find_all('p')
for p in ps:
    try:
        print(p.string)
    except UnicodeEncodeError as inst:
        print(inst)

