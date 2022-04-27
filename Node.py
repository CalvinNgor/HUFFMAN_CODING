class Node:

    def __init__(self, label, freq, node1=None, node2 =None):
        if node1 != None and node2 != None:
            #gestion des fils
            self.node1 = node1
            self.node2 = node2
            self.freq = node1.freq + node2.freq

        else:

            self.label = label
            self.fg = ""
            self.fd = ""
            self.freq = freq
            self.poids = ''



    def getLabel(self):
        return self.nom

    def getFG(self):
        return self.fg

    def getFD(self):
        return self.fd

    def getFreq(self):
        return self.freq

    def isLeaf(self):
        if self.label is None:
            return False
        else:
            return True

    def sommeFreq(self, freq1, freq2):
        freq = freq1 + freq2
        return freq

    def createParentNode(self, n1, n2):
        nodP = Node("",  self.sommeFreq(n1.getFreq(), n2.getFreq()))
        return nodP






