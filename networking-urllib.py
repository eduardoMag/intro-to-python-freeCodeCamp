import urllib.error
import urllib.parse
import urllib.request

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in fhand:
    print(line.decode().strip())
    print()

# like a file
fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
counts = dict()
for line in fhand:
    words = line.decode().split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
print(counts)
print()

# reading web pages
fhand = urllib.request.urlopen('http://www.dr-chuck.com/page2.html')
for line in fhand:
    print(line.decode().strip())
    print()

