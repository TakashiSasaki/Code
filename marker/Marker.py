class Marker():
    __slots__ = ["randomHex", "selfUrl", "targetUrl", "labelSet", 
     "randomHexs", "selfUrls", "targetUrls", "labelSets",
     "relativeUrls"]

    def __init__(self):
        self.randomHex = ""
        self.randomHexs = {}
        self.selfUrl = ""
        self.selfUrls = {}
        self.targetUrl = ""
        self.targetUrls = {}
        self.labelSet = set()
        self.labelSets = {}
        self.relativeUrls = {}

