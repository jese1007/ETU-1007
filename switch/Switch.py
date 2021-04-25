from Control_Ip import Control_Ip
class Switch:
    def __init__(self,nom,classe,ip,mac):
        self.nom = nom
        self.pc = []
        self.ip = ip
        self.mac = mac
        self.classe = classe
        self.data = []
    def getNom(self):
        return self.nom

    def addData(self,data):
        self.data.append(data)

    def getDataRecent(self):
        response = self.data
        if len(response) > 0: 
            return response[len(response)-1]
        else:
            return None

    def getIp(self):
        return self.ip
    
    def getMac(self):
        return self.mac
    
    def getClasse(self):
        return self.classe
    
    def getPc(self):
        return self.pc

    def checkPc(self,pc):
        controlpc = Control_Ip(pc.getIp()+"/"+self.classe)
        datapc = controlpc.configIp4()[1]
        controlsw = Control_Ip(self.getIp()+"/"+self.classe)
        datasw = controls.configIp4()[1]
        retour = False
        if datapc[2] == datasw[2]:
            retour = True
        return retour

    def addPc(self,pc):
        test = True
        data = self.getPc()
        for item in range(len(data)):
            if data[item] == pc:
                test = False
                break
        if test :
            controlsw = Control_Ip(self.getIp()+"/"+str(self.classe))
            datasw = controlsw.configIp4()[1]
            sep = "."
            change = datasw[2].split(sep)
            change[3] = str(int(len(data)+2))
            pc.setIp(sep.join(change))
            self.pc.append(pc)
    
    def Isin(self,pc):
        valiny = False
        data = self.getPc()
        for item in range(len(data)):
            if data[item] == pc:
                valiny = True
                break
        return valiny
    
    def viewS(self):
        write = ""
        print("Host table "+self.getNom())
        for item in range(len(self.pc)):
            write = self.pc[item].getNom()+"  |  "+self.pc[item].getMac()+"  |  "+self.pc[item].getIp()
            print(write)
        
        print("")

    def __eq__(self,other):
        if not isinstance(other,Switch):
            return NotImplemented
        return self.ip == other.ip and self.mac == other.mac and self.classe == other.classe

               

    