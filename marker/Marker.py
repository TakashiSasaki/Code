import urllib.parse
import dns.resolver
import logging

print(urllib.parse.urlsplit("file://surfacepro5/c:/a/b/c"))

class Marker():
    magic = "c39bf83a4d185b0c2a1c2d0a069d37ae6c0cbc44"
    def __init__(self, url):
        pass    
    pass

def checkDnsMagic():
    responses = dns.resolver.query("magic.moukaeritai.work", "TXT")
    if len(responses) != 0:
        logging.warning("Failed to get TXT record of magic.moukaeritai.work.")
    if responses[0] != Marker.magic:
        logging.warning("Magic number does not match with magic.moukaeritai.work.")

if __name__ == "__main__":
    checkDnsMagic()    
