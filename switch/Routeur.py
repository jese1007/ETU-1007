from Rout import Rout
from Control_Ip import Control_Ip
class Routeur:
    def __init__(self):
        self.route = []
        self.ip = []
        self.data = []
    
    def addData(self,data):
        self.data.append(data)

    def getDataRecent(self):
        response = self.data
        if len(response) > 0: 
            return response[len(response)-1]
        else:
            return None

    def getRoute(self):
        return self.route


    def findAllSwitch(self):
        response = []
        for i in range(len(self.route)):
            test1 = True
            test2 = True
            for y in range(len(response)):
                if response[y] == self.route[i].getSwitch1():
                    test1 = False
                if response[y] == self.route[i].getSwitch2():
                    test2 = False
            if test1:
                response.append(self.route[i].getSwitch1())
            if test2:
                response.append(self.route[i].getSwitch2())
        return response

    def getSwitch(self,pc):
        data = self.getRoute()
        response = None
        for item in range(len(data)):
            if data[item].getSwitch1().Isin(pc):
                response = data[item].getSwitch1()
            elif  data[item].getSwitch2().Isin(pc):
                response = data[item].getSwitch2()
        return response

    def addSwitch(self,switch1,switch2):
        test = True
        data = self.getRoute() 
        for item in range(len(data)):
            if data[item].getSwitch1() == switch1 and data[item].getSwitch2() == switch2 or data[item].getSwitch2() == switch1 and data[item].getSwitch1() == switch2 :
                test = False
                break
        if test :
            entrer = Rout(switch1,switch2)
            self.route.append(entrer)

    def sendData(self,pc1,pc2,data):
        pc1.addData(data)
        print("Debut "+pc1.getNom()+"  Data : "+data)
        switchS = self.getSwitch(pc1)
        switchS.addData(data)
        switchS.viewS()
        print("  send vers " + switchS.getNom() +"  Data : "+switchS.getDataRecent())
        switchR = self.getSwitch(pc2)
        if switchS == None or switchR == None:
            print("l'un ou les deux n'apartient pas a un switch")
        elif switchS == switchR :
            pc2.addData(switchS.getDataRecent())
            print("fin "+pc2.getNom())
        else:
            self.addSwitch(switchS,switchR)
            self.addData(switchS.getDataRecent())
            self.viewS()
            print("  send vers Routeur " +"  Data : "+data)
            switchR.addData(self.getDataRecent())
            switchR.viewS()
            print("  send vers "+switchR.getNom() +"  Data : "+switchR.getDataRecent())
            pc2.addData(switchR.getDataRecent)
            print("fin "+pc2.getNom())


    def viewS(self):
        print("Routing table ")
        data  = self.findAllSwitch()
        for item in range(len(data)):
            control = Control_Ip(data[item].getIp()+"/"+str(data[item].getClasse()))
            ip = control.configIp4()[1]
            print(data[item].getNom()+"  |  "+ip[2]+"/"+str(data[item].getClasse())+"  |  "+data[item].getMac())

        print("")
            
         