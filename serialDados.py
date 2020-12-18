# -*- coding: utf-8 -*-

import serial #Import Serial Library
import time
import conn

class AquisDado():
    def __init__(self):
        SerialData = serial.Serial('COM3',57600)
        


    def atenMed(dataFrame):
        return int('0x'+dataFrame[60:62],0),int('0x'+dataFrame[64:66],0)

    def qualiSinal(dataFrame):
        return 100-int('0x'+dataFrame[4:6],0)
    


def atenMed(dataFrame):
    return int('0x'+dataFrame[60:62],0),int('0x'+dataFrame[64:66],0)

def qualiSinal(dataFrame):
    return 100-int('0x'+dataFrame[4:6],0)


SerialData = serial.Serial('COM3',57600)

##s = ""
##c = 0
##while(1):  
##    myData = SerialData.read()     
##    
##    s +=  str(myData.hex())
##    if(c==360):
##        break
##    c+=1
##
##print(s)
##l = s.split('aaaa')



l= ['', '200200831800929b000cd5002190002dd8000e9b000c520003240001e10417052f3f',
 '2002008318015fa0009ed200567e0020fd001fba002afc00156c000f21041b0532fb',
 '200200831800c67c00770d001571002f6f0014d9001742000c0f000361041b05305f',
 '200200831800cbeb0038b9009bed0042e20027d2001cc2000bab001127042c0558bd',
 '20020083180044a5006c9b00329e0027ee0019210045730009f00006f1043c054323',
 '20020083180034770053f2002f460061d4002e79001ce20018700006cf0439054e36',
 '20020083180046350086bc0021a30065e8000acf000fc3000a54000458042c0558a2',
 '2002008318008b5e00bc37003d08002b1c00404d00227c000a2a000517042c054208',
 '2002008318004cdf006f4a00114c00290a0009f0001cfc00060a0004af0422053fb0',
 '200200831800719d00de2c001d02006042001e9c0049850008ef00062a042b053274aa']
##
##
###removendo primeiro e último
if (len(l)>=3):
    del l[0]
    del l[len(l)-1]
##
for i in range(0,len(l)):
    if(qualiSinal(l[i])==100):
        print("Sinal Excelente")
        s_data = ["'aa'","'aa'"]
        j = 0
        while(j<67):
            print(l[i][j:j+2])
            s_data.append("'"+str(l[i][j:j+2])+"'")
            j+=2
        print(s_data)
        conn.insert(s_data)
    print(atenMed(l[i]))
    print("#######novo ciclo#########")
##
