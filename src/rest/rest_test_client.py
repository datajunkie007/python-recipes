import urllib
import time

# Test /hello call
u = urllib.urlopen('http://localhost:8080/hello?name=World!')
print(u.read().decode('utf-8'))

## Test /localtime call
u = urllib.urlopen('http://localhost:8080/localtime')
print(u.read().decode('utf-8'))