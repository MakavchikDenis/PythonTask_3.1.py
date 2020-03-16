

from PackageClass import TrainClass
from datetime import datetime



variableUser=int(input("1- Поиск поезда по направлению следования;"
                       "2-Поиск поезда по направлению следования и времени отправления;"
                       "0-Выход из программы \n"))

while variableUser!=0:
    if variableUser==1:
        varUserDeparturePoint =input("Введите станцию отправления: ")
        varUserDestination = input("Ведите станцию назначения: ")
        varUserResult="".join(varUserDeparturePoint)+"-"+ "".join(varUserDestination)
        arrayOb=TrainClass.Train.GeneralFun()
        count=-1
        for i in range(len(arrayOb)):
            if arrayOb[i].destination==varUserResult:
                var = int(arrayOb[i].commonPlace + arrayOb[i].coupe + arrayOb[i].luxury + arrayOb[i].reservedSeat)
                setattr(arrayOb[i],"totalNumberOfSear", var)
                print (arrayOb[i].get())
                print("\n")
                count=1
        if count==-1:
           print("Такого маршрута нет")
    elif variableUser==2:
        varUserDeparturePoint = input("Введите станцию отправления: ")
        varUserDestination = input("Ведите станцию назначения: ")
        varUserTime=input("Введите время в формате 00 00: ")
        varUserTimeFormat=datetime.strptime(varUserTime,"%H %M")
        varUserResult = "".join(varUserDeparturePoint) + "-" + "".join(varUserDestination)
        arrayOb = TrainClass.Train.GeneralFun()
        count=-1
        for i in range(len(arrayOb)):
            if arrayOb[i].destination==varUserResult:
                timeArray=str(arrayOb[i].time).split(".")
                timeOb=datetime.strptime(str("".join(timeArray[0]) + " " + "".join(timeArray[1])), "%H %M")
                if varUserTimeFormat<=timeOb:
                    setattr(arrayOb[i],"totalNumberOfSear",int(arrayOb[i].commonPlace+
                                                                        arrayOb[i].coupe+arrayOb[i].luxury+
                                                             arrayOb[i].reservedSeat))
                    print (arrayOb[i].get()+"\n")
                    count=1
        if count==-1:
            print("Такого маршрута нет")
    else:
        print("Введены неверные данные!!!!")
    variableUser = int(input("1- Поиск поезда по направлению следования;"
                             "2-Поиск поезда по направлению следования и времени отправления;"
                             "0-Выход из программы \n"))

print("Спасибо, что выбрали нашу программу!!")