import requests

def print_details(request):
    print("Various attributes on the request object (get):")
    print("-----------------------------------------------")
    print("apparent_encoding:")
    print(request.apparent_encoding)
    print("content:")
    print(request.content)
    print("text:")
    print(request.text)
    print("status_code:")
    print(request.status_code)
    print("url:")
    print(request.url)

    print("Various methods on the request object (get):")
    print("--------------------------------------------")
    print("iter_content():")
    for element in request.iter_content():
        print(element)
    print("iter_lines():")
    for line in request.iter_lines():
        print(line)
    print("json():")
    for element in request.json():
        print(element)
    

# ------

if __name__ == "__main__":

    r = requests.get('https://api.github.com/events')
    print(r)
    print_details(request)
