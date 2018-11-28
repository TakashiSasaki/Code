hexdict = {}
for x in range(15):
    hexdict[format(x,"01x")] = {}
    for y in range(15):
        hexdict[format(x,"01x")][format(y,"01x")] = format(x^y,"01x")

def xor(xstring, ystring):
    z = []
    for x,y in zip(xstring, ystring):
        z.append(hexdict[x.lower()][y.lower()])
    return "".join(z)
