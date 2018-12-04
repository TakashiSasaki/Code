import dns.resolver
import logging

class BaseMarker(object):
    magic = b"c39bf83a4d185b0c2a1c2d0a069d37ae6c0cbc44"
    pass

def getDnsTxts(fqdn):
    answer = dns.resolver.query(fqdn, "TXT")
    answer0 = answer.response.answer[0]
    item = answer0.items[0]
    strings = item.strings
    return strings

def checkDnsMagic():
    strings = getDnsTxts("magic.moukaeritai.work")
    if len(strings) != 1:
         logging.warning("Failed to get TXT record of magic.moukaeritai.work.")
    if strings[0] != BaseMarker.magic:
         logging.warning("Magic number does not match with magic.moukaeritai.work.")

if __name__ == "__main__":
    checkDnsMagic()    
