import requests

# ------

if __name__ == "__main__":

    r = requests.get('https://api.github.com/events')
    print(r)

    print("Various attributes on the request object (get):")
    print("-----------------------------------------")
    print("apparent_encoding:")
    print(r.apparent_encoding)
    print("content:")
    print(r.content)
    print("text:")
    print(r.text)
    print("status_code:")
    print(r.status_code)
    print("url:")
    print(r.url)

    print("Various methods on the request object (get):")
    print("iter_content():")
    for element in r.iter_content():
        print(element)
    print("iter_lines():")
    for line in r.iter_lines():
        print(line)
    print("json():")
    for element in r.json():
        print(element)
