

class Train:
    number=0
    destination = 0
    time=0
    commonPlace=0
    coupe = 0
    reservedSeat=0
    luxury=0
    totalNumberOfSear=0
    fileReader=0


    def __init__(self,number,destination,time,commonPlace,coupe,reservedSeat,luxury):
        self.number=number
        self.destination=destination
        self.time=time
        self.commonPlace= int(commonPlace)
        self.coupe=int(coupe)
        self.reservedSeat= int(reservedSeat)
        self.luxury= int(luxury)

    def setAttribute(self,number,destination,time,commonPlace,coupe,reservedSeat,luxury ):
        self.number = number
        self.destination = destination
        self.time = time
        self.commonPlace = int(commonPlace)
        self.coupe = int(coupe)
        self.reservedSeat = int(reservedSeat)
        self.luxury = int(luxury)

    def get(self):
        return str("Номер поезда: "+self.number + "\n"+
                   "Путь назначения: "+self.destination +"\n"+
                   "Время отправления: "+self.time +"\n"+
                    "Общее количество свободных мест: " + str(self.totalNumberOfSear)+"\n"+
                    "Общих: "+ str(self.commonPlace) +"\n"+
                    "Купе: "+str(self.coupe) +"\n"+
                    "Плацкарт: "+str(self.reservedSeat)+"\n"+
                    "Люкс: " + str(self.luxury))

    #def __del__(self):
         #print("Удаление объекта")


    @staticmethod
    def GeneralFun():
        Train.fileReader = open("Schedule.txt", "r")
        arrayOb=[]
        varStr=Train.fileReader.readline()
        while varStr!="\n":
            arryStr=varStr.split(",")
            num = "".join(arryStr[0])
            des = "".join(arryStr[1])
            tim="".join(arryStr[2])
            comm="".join(arryStr[3])
            cou="".join(arryStr[4])
            res="".join(arryStr[5])
            lux="".join(arryStr[6])
            ob=Train(num,des,tim,comm,cou,res,lux)
            arrayOb.append(ob)
            varStr=Train.fileReader.readline()
        Train.fileReader.close()
        return arrayOb
