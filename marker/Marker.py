class Marker():
    __slots__ = ["randomHexs", "selfUrls", "targetUrls", "labelSets", "relativeUrls"]

    def __init__(self):
        self.randomHexs = {}
        self.selfUrls = {}
        self.targetUrls = {}
        self.labelSets = {}
        self.relativeUrls = {}

