from Pc import Pc
from Switch import Switch
from Routeur import Routeur
pc1 = Pc("pc1","10.0.0.0","aaa.aaa.aaa")
pc2 = Pc("pc2","10.0.0.0","bbb.bbb.bbb")
switchX = Switch("switchX",24,"11.11.11.1","ss1.ss1.ss1")
switchX.addPc(pc1)
switchX.addPc(pc2)

# switchX.viewS()

pc3 = Pc("pc3","10.0.0.0","ccc.ccc.ccc")
pc4 = Pc("pc4","10.0.0.0","ddd.ddd.ddd")
switchY = Switch("switchY",24,"22.22.22.1","ss2.ss2.ss2")
switchY.addPc(pc3)
switchY.addPc(pc4)

# switchY.viewS()


routeur = Routeur()
routeur.addSwitch(switchX,switchY)

# routeur.viewS()

routeur.sendData(pc1,pc4,"Salut Petit 4!!!")

