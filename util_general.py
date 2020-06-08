"""
#module that create or read a .txt file
Created on Wed Apr 1 2020
@author: Diego Salas
"""
from io import open
from timeit import timeit
from datetime import datetime, date, time, timedelta
import calendar
import numpy as np
import pandas as pd
import matplotlib.pyplot as mpl

# ! CREATE FILE
def createSimpleFile(name,content):
    outputFile = open(name,'w')
    outputFile.write(content)
    outputFile.close()

# ! CREATE FILE WITH RUTE
def createSimpleFileRute(name,content):
    outputFile = open(name,'w')
    outputFile.write(content)
    outputFile.close()

# ! READ SIMPLE FILE
def readSimpleFile(name):
    cipherTextFile = open(name,'r', encoding="utf8")
    fileContent = cipherTextFile.readlines()
    cipherTextFile.close()

    cipherText = ""
    for fc in fileContent:
        cipherText += fc.replace("\n", " ")

    return cipherText

# ! CREATE CLEAN TEXT
def createCleanText(fileName):
    alphabet = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ0123456789"
    plainTextFile = open(fileName,'r', encoding="utf8")
    textFile = plainTextFile.readlines()
    plainTextFile.close()

    plainText = ""
    for tf in textFile:
        plainText += tf.replace("\n", " ").upper()

    cleanText = ""
    for tf in plainText:
        myChar = tf.upper()
        if myChar in alphabet:
            cleanText += myChar
        elif myChar == " ":
            cleanText += myChar
        else:
            cleanText += ""
    return cleanText

# ! CREATE CIPHER FILE
def createCipherFile(nameFile, cipherText):

    alphaM = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ0123456789"

    cleanText = ''
    for cp in cipherText:
        if cp in alphaM:
            cleanText += cp
        elif cp == ',':
            cleanText += ' '
        else:
            cleanText += ''

    createHistogram(cleanText,nameFile)

    outputFile = open('./cipherLevels/' + str(nameFile) + '.txt','w')
    content  = "Dirty text:\n"+cipherText+"\n\nClean text:\n"+cleanText
    outputFile.write(content)
    outputFile.close()

# ! CRWATE FILE
def createDecipherFile(nameFile, cipherText):
    alphaM = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ0123456789"

    cleanText = ''
    for cp in cipherText:
        if cp in alphaM:
            cleanText += cp
        elif cp == ',':
            cleanText += ' '
        else:
            cleanText += ''

    createHistogram(cleanText,nameFile)

    outputFile = open('./decipherLevels/' + str(nameFile) + '.txt','w')
    content  = "Dirty text:\n"+cipherText+"\n\nClean text:\n"+cleanText
    outputFile.write(content)
    outputFile.close()

# ! GENERATE HISTOGRAM
def createHistogram(plainText,title):
    alphabet = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ0123456789"
    A=0;B=0;C=0;D=0;E=0;F=0;G=0;H=0;I=0;J=0;K=0;L=0;M=0;N=0;Ñ=0;O=0;P=0;Q=0;R=0;S=0;T=0;U=0;V=0;W=0;X=0;Y=0;Z=0
    one=0;two=0;three=0;four=0;five=0;six=0;seven=0;eigth=0;nine=0;ten=0

    for cc in plainText:
        if cc in alphabet:
            if cc == 'A': A += 1
            if cc == 'B': B += 1
            if cc == 'C': C += 1
            if cc == 'D': D += 1
            if cc == 'E': E += 1
            if cc == 'F': F += 1
            if cc == 'G': G += 1
            if cc == 'H': H += 1
            if cc == 'I': I += 1
            if cc == 'J': J += 1
            if cc == 'K': K += 1
            if cc == 'L': L += 1
            if cc == 'M': M += 1
            if cc == 'N': N += 1
            if cc == 'Ñ': Ñ += 1
            if cc == 'O': O += 1
            if cc == 'P': P += 1
            if cc == 'Q': Q += 1
            if cc == 'R': R += 1
            if cc == 'S': S += 1
            if cc == 'T': T += 1
            if cc == 'U': U += 1
            if cc == 'V': V += 1
            if cc == 'W': W += 1
            if cc == 'X': X += 1
            if cc == 'Y': Y += 1
            if cc == 'Z': Z += 1
            if cc == '0': one += 1
            if cc == '1': two += 1
            if cc == '2': three += 1
            if cc == '3': four += 1
            if cc == '4': five += 1
            if cc == '5': six += 1
            if cc == '6': seven += 1
            if cc == '7': eigth += 1
            if cc == '8': nine += 1
            if cc == '9': ten += 1

    histogram = mpl.figure(u''+title)
    axis = histogram.add_subplot(111)

    aLabels = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','Ñ','O','P','Q','R','S','T','U','V','W','X','Y','Z','0','1','2','3','4','5','6','7','8','9']
    num = [A,B,C,D,E,F,G,H,I,J,K,L,M,N,Ñ,O,P,Q,R,S,T,U,V,W,X,Y,Z,one,two,three,four,five,six,seven,eigth,nine,ten]
    xx  = range(len(num))
    rects1 = axis.bar(xx,num,width=0.5,color = 'y',align='center')
    axis.set_xticks(xx)
    axis.set_xticklabels(aLabels)
    mpl.xlabel("Cipher Text")
    mpl.ylabel("Absolute Frecuency")

    def autolabel(rects):
        for rect in rects:
            height = rect.get_height()
            axis.text(rect.get_x() + rect.get_width()/2., 1.05*height,
                    '%d' % int(height),
                    ha='center', va='bottom')

    autolabel(rects1)
    mpl.show()


# ! EXECUTION TIME
def checkPoint():
    now = datetime.now()
    # currenTime = time(now.hour, now.minute, microseconds)
    # timeLap = currenTime - timedelta(seconds=microseconds)
    currenTime = str("%s" % now)
    return currenTime