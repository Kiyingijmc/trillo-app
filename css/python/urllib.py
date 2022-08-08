import urllib.request
with urllib.request.urlopen('https://www.levidia.ch/') as response:
  html = response.read()
  
  print(html)