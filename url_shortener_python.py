import pyshorteners

link = input("enter the link : ")
shortener = pyshorteners.Shortener()
print(shortener.tinyurl.short(link))
