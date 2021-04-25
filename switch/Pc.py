class Pc:
    def __init__(self, nom, ip, mac):
        self.nom = nom
        self.ip = ip
        self.mac = mac
        self.data = [] 
    def getNom(self):
        return self.nom

    def setIp(self,ip):
        self.ip = ip

    def addData(self,data):
        self.data.append(data)

    def getIp(self):
        return self.ip
    
    def getMac(self):
        return self.mac

    def __eq__(self,other):
        if not isinstance(other,Pc):
            return NotImplemented
        return  self.mac == other.mac 