from dataclasses import dataclass, field
from typing import ClassVar
import dns.resolver
import logging

@dataclass
class Marker():
    magic : bytes = b"c39bf83a4d185b0c2a1c2d0a069d37ae6c0cbc44"
    labelSet : set = field(default_factory = set)
    randomHexs : dict = field(default_factory = dict)
    selfUrls : dict = field(default_factory = dict)
    targetUrls : dict = field(default_factory = dict)
    relativeUrls : dict = field(default_factory = dict)

    def __init__(self):
        pass

    def checkDnsMagic(self):
        strings = getDnsTxts("magic.moukaeritai.work")
        if len(strings) != 1:
            logging.warning("Failed to get TXT record of magic.moukaeritai.work.")
            return False
        if strings[0] != self.magic:
            logging.warning("Magic number does not match with magic.moukaeritai.work.")
            return False
        return True

def getDnsTxts(fqdn):
    answer = dns.resolver.query(fqdn, "TXT")
    answer0 = answer.response.answer[0]
    item = answer0.items[0]
    strings = item.strings
    return strings

