import re
import os
from datetime import date
from datetime import datetime
import util_general as ug
import util_methods as um
import time
os.system('clear')

# * ================================== *
# *    VERIFY THE ENCRYPTION METHOD    *
# * ================================== *
def decriptMenu(level,text,cesarKey,monoKeySize,monoKey,block,padding):
    alphabet = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ0123456789'
    if cesarKey != '':
        cesarKey = int(cesarKey) % len(alphabet)
    decryptedText = ''
    if level == 'cesar':
        decryptedText = um.cesarMethodDec(text,cesarKey)
    elif level == 'mono':
        decryptedText = um.monoMethodDec(text,monoKeySize,monoKey)
    elif level == 'trans':
        decryptedText = um.transMethodDec(text,block,padding)
    else:
        print('WARNING! Invalid encryption method.')
        return False

    return decryptedText


# * ================================== *
# *      READING CONFIGURATION FILE    *
# * ================================== *
def main():
    os.system('clear')
    architectureLevels = 0
    level1  = ''; level1ck = ''; level1mks = ''; level1mk = ''; level1tk = ''; level1tp = ''
    level2  = ''; level2ck = ''; level2mks = ''; level2mk = ''; level2tk = ''; level2tp = ''
    level3  = ''; level3ck = ''; level3mks = ''; level3mk = ''; level3tk = ''; level3tp = ''
    level4  = ''; level4ck = ''; level4mks = ''; level4mk = ''; level4tk = ''; level4tp = ''
    level5  = ''; level5ck = ''; level5mks = ''; level5mk = ''; level5tk = ''; level5tp = ''
    level6  = ''; level6ck = ''; level6mks = ''; level6mk = ''; level6tk = ''; level6tp = ''

    with open("configFile.txt","r") as configFile:
        os.system('clear')
        print('\n\n\n\n\n\n========================\nReading configFile.txt...\n')
        for variables in configFile:

            v1 = re.match(r".*~# architecture levels = (\d*)",variables)
            if v1: architectureLevels = int(v1.group(1))

            # * LEVEL 1
            l1 = re.match(r".*~# level 1 = ([a-zA-Z]*)",variables)
            l11 = re.match(r".*~# level 1 cesar key = ([-0-9]*)",variables)
            l12 = re.match(r".*~# level 1 mono size key = ([0-9]*)",variables)
            l13 = re.match(r".*~# level 1 mono key = (\w*)",variables)
            l14 = re.match(r".*~# level 1 trans key = ([0-9]*)",variables)
            l15 = re.match(r".*~# level 1 trans padding = ([a-z]*)",variables)
            if l1:
                level1 = l1.group(1).lower()
                if level1 == 'cesar' or level1 == 'mono' or level1 == 'trans':
                    print('level 1: '+level1)
                else:
                    print('ERROR! invalid method for level 1.')
                    exit()
            if l11:
                level1ck = l11.group(1)
                print('level 1 cesar key: '+level1ck)
            if l12:
                level1mks = l12.group(1)
                if level1mks == '27' or level1mks == '37':
                    print('level 1 mono key size: '+level1mks)
                else:
                    print('ERROR! invalid key size mono for level 1.')
                    exit()
            if l13:
                level1mk = l13.group(1)
                print('level 1 mono key: '+level1mk)
            if l14:
                level1tk_a = l14.group(1)
                if um.keyTransValidate(level1tk_a):
                    level1tk = level1tk_a
                    print('level 1 trans key: '+level1tk)
                else:
                    exit()
            if l15:
                level1tp_a = l15.group(1)
                if um.paddingValidate(level1tp_a):
                    level1tp = level1tp_a
                    print('level 1 trans padding: '+level1tp)
                else:
                    exit()

            # * LEVEL 2
            l2 = re.match(r".*~# level 2 = ([a-zA-Z]*)",variables)
            l21 = re.match(r".*~# level 2 cesar key = ([-0-9]*)",variables)
            l22 = re.match(r".*~# level 2 mono size key = ([0-9]*)",variables)
            l23 = re.match(r".*~# level 2 mono key = (\w*)",variables)
            l24 = re.match(r".*~# level 2 trans key = ([0-9]*)",variables)
            l25 = re.match(r".*~# level 2 trans padding = ([a-z]*)",variables)
            if l2:
                level2 = l2.group(1).lower()
                if level2 == 'cesar' or level2 == 'mono' or level2 == 'trans':
                    print('level 2: '+level2)
                else:
                    print('ERROR! invalid method for level 2.')
                    exit()
            if l21:
                level2ck = l21.group(1)
                print('level 2 cesar key: '+level2ck)
            if l22:
                level2mks = l22.group(1)
                if level2mks == '27' or level2mks == '37':
                    print('level 2 mono key size: '+level2mks)
                else:
                    print('ERROR! invalid key size mono for level 2.')
                    exit()
            if l23:
                level2mk = l23.group(1)
                print('level 2 mono key: '+level2mk)
            if l24:
                level2tk_a = l24.group(1)
                if um.keyTransValidate(level2tk_a):
                    level2tk = level2tk_a
                    print('level 2 trans key: '+level2tk)
                else:
                    exit()
            if l25:
                level2tp_a = l25.group(1)
                if um.paddingValidate(level2tp_a):
                    level2tp = level2tp_a
                    print('level 2 trans key: '+level2tp)
                else:
                    exit()

            # * LEVEL 3
            l3 = re.match(r".*~# level 3 = ([a-zA-Z]*)",variables)
            l31 = re.match(r".*~# level 3 cesar key = ([-0-9]*)",variables)
            l32 = re.match(r".*~# level 3 mono size key = ([0-9]*)",variables)
            l33 = re.match(r".*~# level 3 mono key = (\w*)",variables)
            l34 = re.match(r".*~# level 3 trans key = ([0-9]*)",variables)
            l35 = re.match(r".*~# level 3 trans padding = ([a-z]*)",variables)
            if l3:
                level3 = l3.group(1).lower()
                if level3 == 'cesar' or level3 == 'mono' or level3 == 'trans':
                    print('level 3: '+level3)
                else:
                    print('ERROR! invalid method for level 3.')
                    exit()
            if l31:
                level3ck = l31.group(1)
                print('level 3 cesar key: '+level3ck)
            if l32:
                level3mks = l32.group(1)
                if level3mks == '27' or level3mks == '37':
                    print('level 3 mono key size: '+level3mks)
                else:
                    print('ERROR! invalid key size mono for level 3.')
                    exit()
            if l33:
                level3mk = l33.group(1)
                print('level 3 mono key: '+level3mk)
            if l34:
                level3tk_a = l34.group(1)
                if um.keyTransValidate(level3tk_a):
                    level3tk = level3tk_a
                    print('level 3 trans key: '+level3tk)
                else:
                    exit()
            if l35:
                level3tp_a = l35.group(1)
                if um.paddingValidate(level3tp_a):
                    level3tp = level3tp_a
                    print('level 3 trans key: '+level3tp)
                else:
                    exit()

            # * LEVEL 4
            l4 = re.match(r".*~# level 4 = ([a-zA-Z]*)",variables)
            l41 = re.match(r".*~# level 4 cesar key = ([-0-9]*)",variables)
            l42 = re.match(r".*~# level 4 mono size key = ([0-9]*)",variables)
            l43 = re.match(r".*~# level 4 mono key = (\w*)",variables)
            l44 = re.match(r".*~# level 4 trans key = ([0-9]*)",variables)
            l45 = re.match(r".*~# level 4 trans padding = ([a-z]*)",variables)
            if l4:
                level4 = l4.group(1).lower()
                if level4 == 'cesar' or level4 == 'mono' or level4 == 'trans':
                    print('level 4: '+level4)
                else:
                    print('ERROR! invalid method for level 4.')
                    exit()
            if l41:
                level4ck = l41.group(1)
                print('level 4 cesar key: '+level4ck)
            if l42:
                level4mks = l42.group(1)
                if level4mks == '27' or level4mks == '37':
                    print('level 4 mono key size: '+level4mks)
                else:
                    print('ERROR! invalid key size mono for level 4.')
                    exit()
            if l43:
                level4mk = l43.group(1)
                print('level 4 mono key: '+level4mk)
            if l44:
                level4tk_a = l44.group(1)
                if um.keyTransValidate(level4tk_a):
                    level4tk = level4tk_a
                    print('level 4 trans key: '+level4tk)
                else:
                    exit()
            if l45:
                level4tp_a = l45.group(1)
                if um.paddingValidate(level4tp_a):
                    level4tp = level4tp_a
                    print('level 4 trans key: '+level4tp)
                else:
                    exit()

            # * LEVEL 5
            l5 = re.match(r".*~# level 5 = ([a-zA-Z]*)",variables)
            l51 = re.match(r".*~# level 5 cesar key = ([-0-9]*)",variables)
            l52 = re.match(r".*~# level 5 mono size key = ([0-9]*)",variables)
            l53 = re.match(r".*~# level 5 mono key = (\w*)",variables)
            l54 = re.match(r".*~# level 5 trans key = ([0-9]*)",variables)
            l55 = re.match(r".*~# level 5 trans padding = ([a-z]*)",variables)
            if l5:
                level5 = l5.group(1).lower()
                if level5 == 'cesar' or level5 == 'mono' or level5 == 'trans':
                    print('level 5: '+level5)
                else:
                    print('ERROR! invalid method for level 5.')
                    exit()
            if l51:
                level5ck = l51.group(1)
                print('level 5 cesar key: '+level5ck)
            if l52:
                level5mks = l52.group(1)
                if level5mks == '27' or level5mks == '37':
                    print('level 5 mono key size: '+level5mks)
                else:
                    print('ERROR! invalid key size mono for level 5.')
                    exit()
            if l53:
                level5mk = l53.group(1)
                print('level 5 mono key: '+level5mk)
            if l54:
                level5tk_a = l54.group(1)
                if um.keyTransValidate(level5tk_a):
                    level5tk = level5tk_a
                    print('level 5 trans key: '+level5tk)
                else:
                    exit()
            if l55:
                level5tp_a = l55.group(1)
                if um.paddingValidate(level5tp_a):
                    level5tp = level5tp_a
                    print('level 5 trans key: '+level5tp)
                else:
                    exit()

            # * LEVEL 6
            l6 = re.match(r".*~# level 6 = ([a-zA-Z]*)",variables)
            l61 = re.match(r".*~# level 6 cesar key = ([-0-9]*)",variables)
            l62 = re.match(r".*~# level 6 mono size key = ([0-9]*)",variables)
            l63 = re.match(r".*~# level 6 mono key = (\w*)",variables)
            l64 = re.match(r".*~# level 6 trans key = ([0-9]*)",variables)
            l65 = re.match(r".*~# level 6 trans padding = ([a-z]*)",variables)
            if l6:
                level6 = l6.group(1).lower()
                if level6 == 'cesar' or level6 == 'mono' or level6 == 'trans':
                    print('level 6: '+level6)
                else:
                    print('ERROR! invalid method for level 6.')
                    exit()
            if l61:
                level6ck = l61.group(1)
                print('level 6 cesar key: '+level6ck)
            if l62:
                level6mks = l62.group(1)
                if level6mks == '27' or level6mks == '37':
                    print('level 6 mono key size: '+level6mks)
                else:
                    print('ERROR! invalid key size mono for level 6.')
                    exit()
            if l63:
                level6mk = l63.group(1)
                print('level 6 mono key: '+level6mk)
            if l64:
                level6tk_a = l64.group(1)
                if um.keyTransValidate(level6tk_a):
                    level6tk = level6tk_a
                    print('level 6 trans key: '+level6tk)
                else:
                    exit()
            if l65:
                level6tp_a = l65.group(1)
                if um.paddingValidate(level6tp_a):
                    level6tp = level6tp_a
                    print('level 6 trans key: '+level6tp)
                else:
                    exit()

    print('\n\nDECRIPTING...\n')
    cipherText = ug.readSimpleFile('./texts/cipherText.txt')
    textLog = '\t\t\t--- DECRYPTION LOG ---\n\n'
    finalPlainText = ''
    if architectureLevels >= 1 and architectureLevels <= 6:
        if level1 != '' and level2 != '':
            if len(level6) > 0 and level6 != '' and architectureLevels == 6:
                textLog += 'Level 6 start time : {}\n'.format(ug.checkPoint())
                finalPlainText = decriptMenu(level6,cipherText,level6ck,level6mks,level6mk,level6tk,level6tp)
                textLog += 'Level 6 ending time: {}\n\n'.format(ug.checkPoint())
                ug.createDecipherFile('level6',finalPlainText)
            else:
                finalPlainText = cipherText
            if len(level5) > 0 and level5 != '' and architectureLevels >= 5:
                textLog += 'Level 5 start time : {}\n'.format(ug.checkPoint())
                finalPlainText = decriptMenu(level5,finalPlainText,level5ck,level5mks,level5mk,level5tk,level5tp)
                textLog += 'Level 5 ending time: {}\n\n'.format(ug.checkPoint())
                ug.createDecipherFile('level5',finalPlainText)
            else:
                finalPlainText = cipherText
            if len(level4) > 0 and level4 != '' and architectureLevels >= 4:
                textLog += 'Level 4 start time : {}\n'.format(ug.checkPoint())
                finalPlainText = decriptMenu(level4,finalPlainText,level4ck,level4mks,level4mk,level4tk,level4tp)
                textLog += 'Level 4 ending time: {}\n\n'.format(ug.checkPoint())
                ug.createDecipherFile('level4',finalPlainText)
            else:
                finalPlainText = cipherText
            if len(level3) > 0 and level3 != '' and architectureLevels >= 3:
                textLog += 'Level 3 start time : {}\n'.format(ug.checkPoint())
                finalPlainText = decriptMenu(level3,finalPlainText,level3ck,level3mks,level3mk,level3tk,level3tp)
                textLog += 'Level 3 ending time: {}\n\n'.format(ug.checkPoint())
                ug.createDecipherFile('level3',finalPlainText)
            else:
                finalPlainText = cipherText
            textLog += 'Level 2 start time : {}\n'.format(ug.checkPoint())
            finalPlainText = decriptMenu(level2,finalPlainText,level2ck,level2mks,level2mk,level2tk,level2tp)
            textLog += 'Level 2 ending time: {}\n\n'.format(ug.checkPoint())
            ug.createDecipherFile('level2',finalPlainText)

            textLog += 'Level 1 start time : {}\n'.format(ug.checkPoint())
            finalPlainText = decriptMenu(level1,finalPlainText,level1ck,level1mks,level1mk,level1tk,level1tp)
            textLog += 'Level 1 ending time: {}\n\n'.format(ug.checkPoint())
            ug.createDecipherFile('level1',finalPlainText)

            print('\n\n*** SUCCESSFUL PROCESS!\n\n')

            ug.createSimpleFile('./texts/decipherText.txt',finalPlainText.replace(',',' '))
            ug.createSimpleFile('./logs/DecryptionLOG.txt',textLog)
        else:
            print('*** WARNING! Level 1 and 2 are required.')
    else:
        print('*** WARNING! The range must be between 2 and 6 levels.')

if __name__ == "__main__":
    main()