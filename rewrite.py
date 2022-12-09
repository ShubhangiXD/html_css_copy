from bs4 import BeautifulSoup as bs

# soup = bs(urllib.urlopen('test.html').read())

# txt = soup.find('div', {'class' : 'body'})


# f = urllib.urlopen("http://www.python.org")
# s = f.read()
# soup = bs(s)
# txt = soup.find('div', {'class' : 'body'})
# f.close()
# print(html2text.html2text(txt))

# with urllib.request.urlopen("http://www.python.org") as url:
#     s = url.read()
#     # soup = s
#     # txt = soup.find('div', {'class' : 'body'})
#     # print(html2text.html2text(txt))
#     print(s)

# soup = bs.contents('test.html')
# print(soup.get_text())
text_file = open("test.html", "r")
 
#read whole file to a string
data = text_file.read()
print(type(data))
 
#close file
text_file.close()
# print(data)