from urllib import request

response = request.urlopen("https://no.pinterest.com/")

# print(response)

data = response.read()

# print(data)


text = data.decode("utf-8")

# print(text)

html = request.urlopen("https://no.pinterest.com/pin/1149966086146898777/").read().decode()

# print(html)
print(response.status)
print(response.headers)