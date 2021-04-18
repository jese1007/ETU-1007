import math
class Control_Ip:
    def __init__(self,ip):
        self.ip = ip

    def simplifier(self,ip):
        iparray = ip.split(":")
        reponse = hex(int(str(iparray[0]),16))[2:]
        for item in range(1,len(iparray)):
            print(iparray[item])
            try:
                reponse += ":" + hex(int(str(iparray[item]),16))[2:]
            except :
                reponse += ":" + iparray[item]
        return reponse
    
    def abreviation(self):
        slpit1p = self.ip.split(":")
        reponse = self.ip
        debut = 0
        fin = 0
        for i in range(len(slpit1p)):
            if slpit1p[i] == "0000":
                debut = i
                for y in range(debut+1,len(slpit1p)):
                    if slpit1p[debut] == slpit1p[y]:
                        fin = y
                    elif slpit1p[debut] != slpit1p[y]:
                        break
                break
        if int(debut) < int(fin) :
            reponse = reponse[:int(debut*4)+int(debut-1)] + "::" + reponse[int((fin+1)*4)+int(fin+1):len(reponse)]
        temp = reponse.split("/")
        temp[0] = self.simplifier(temp[0])
        if len(temp) > 1:
            temp[0] += "/" + temp[1]
        reponse = temp[0]
        return reponse

    def formeNormal(self):
        split2p = self.ip.split("::")
        reponse = ""
        droit = 0
        gauche = 0
        if len(split2p) == 1 :
            reponse = self.ip
        elif len(split2p) == 2 :
            zero = ""
            gauche = len(split2p[0].split(":"))
            if len(split2p[1]) > 0:
                testSlash = split2p[1].split("/")
                droit = len(split2p[1].split(":"))
                if testSlash[0] != "":
                   split2p[1] = ":" + split2p[1]
            print(droit)
            for i in range(int(8-gauche-droit)):
                zero += ":0"
            reponse = split2p[0] + zero + split2p[1]
        return reponse

    def transfIp6(self):
        normal = self.formeNormal()
        splitSlash = normal.split("/")
        reponse = normal
        if len(splitSlash) > 1 :
            split2point = splitSlash[0].split(":")
            valiny = ""
            zero = ""
            for item in range(len(split2point)):
                print(format(int(str(split2point[item]),16),'016b'))
                valiny += format(int(str(split2point[item]),16),'016b')
            for i in range(128-int(splitSlash[1])):
                zero += "0"
            valiny = valiny[:int(splitSlash[1])] + zero
            reponse = hex(int(valiny[:16],2))[2:]
            for i in range(1,8):
                reponse += ":" + hex(int(valiny[i*16:(i+1)*16],2))[2:]
                
        return reponse
    
    def configIp6(self):
        normal = self.formeNormal()
        abreviation = self.abreviation()
        finaly = self.transfIp6()
        titre = ("ip","formaNormal","Abreviation","Finaly")
        data = (self.ip,normal,abreviation,finaly)
        return titre,data

    def transfIp4(self):
        reponse = ""
        iparray = self.ip.split("/")
        reponse = iparray[0]
        classe = 0
        if len(iparray) > 1:
            reponse = ""
            valiny = ""
            ipInter = iparray[0].split(".")
            for i in range(len(ipInter)):
                reponse += format(int(ipInter[i]),'08b')
            reponse = reponse[:int(iparray[1])]
            for ink in range(32-int(iparray[1])):
                reponse += "0"
            for i in range(4):
                debut = i*8
                fin = (i+1)*8
                strko  = int(reponse[int(debut):int(fin)],2)
                if i > 0 :
                    valiny += "."+str(strko)
                elif i == 0:
                    valiny += str(strko)
            reponse = valiny
            classe = iparray[1]
        return  reponse,classe

    def nbreAdresse(self,classe):
        return int(math.pow(2, 32-int(classe)))-2

    def masque(self,classe):
        val = ['0', '0', '0', '0']
        jointure = "."
        nbre = int(classe/8)
        reste = classe % 8
        i = 0
        for i in range(nbre):
            val[i] = '255'
        i += 1
        rest = 0
        for y in range(reste):
            rest += int(math.pow(2, 7-y))
        if i < 8:
            val[i] = str(rest)
        return jointure.join(val)
    
    def adresse(self,ip,classe):
        iparray = ip.split(".")
        reseau = ""
        diffusion = ""
        valReseau = ""
        valDiffusion = ""
        for i in range(len(iparray)):
            reseau += format(int(iparray[i]),'08b')
            diffusion += format(int(iparray[i]),'08b')
        reseau = reseau[:int(classe)]
        diffusion = diffusion[:int(classe)]
        for y in range(32-int(classe)):
            reseau += "0"
            diffusion += "1"
        for i in range(4):
            debut = i*8
            fin = (i+1)*8
            strko1  = int(reseau[int(debut):int(fin)],2)
            strko2  = int(diffusion[int(debut):int(fin)],2)
            if i > 0 :
                valReseau += "."+str(strko1)
                valDiffusion += "."+str(strko2)
            elif i == 0:
                valReseau += str(strko1)
                valDiffusion += str(strko2)
        return valReseau,valDiffusion    

    def configIp4(self):
        ip = self.ip.split("/")
        classe = ""
        if len(ip) == 1:
            if int(iparray[0]) >= 0 and int(iparray[0])<= 127:
                classe = 8
            elif int(iparray[0]) >= 128 and int(iparray[0])<= 192:
                classe = 16
            elif int(iparray[0]) >= 193 and int(iparray[0])<= 255:
                classe = 24
        elif len(ip) > 1:
            classe = int(ip[1])
        
        (reseau,diffusion) = self.adresse(ip[0],classe)
        sous = self.masque(classe)
        disponible = self.nbreAdresse(classe)
        titre = ("ip", "Masque ", "adresse reseau", "adresse diffusion","nb disponible","Premier","fin")
        if len(ip) == 1 :
            self.ip = self.ip+"/"+str(classe)
        sep = "."
        datapermier = reseau.split(sep)
        datapermier[3] = str(int(datapermier[3])+1)
        premier = sep.join(datapermier)
        datafin = diffusion.split(sep)
        datafin[3] = str(int(datafin[3])-1)
        fin = sep.join(datafin)
        data = (self.ip,sous,reseau,diffusion,disponible,premier,fin)
        return titre,data
