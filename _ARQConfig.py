from io import open
import os
import re
from cmd import Cmd as terminal
import util_general as mf
os.system('clear')

def paddingValidate(padding):
    alpha = "abcdefghijklmnñopqrstuvwxyz"
    flag = True
    if len(padding) > 1:
        print("*** ERROR! PADDING MUST BE A ONLY ONE CHARACTER")
        flag = False
    if padding not in alpha:
        print("*** ERROR! PADDING MUST BE A LOWER CASE CHARACTER [a-z]")
        flag = False
    return flag

def createConfigFile(numLevels):
    os.system('clear')
    print('=========================================\n')
    print('Enter the encryption method for each level\n\n1) Cesar\n2) Monoalphabetical\n3) Permutation\n')

    ctf =  '---- CONFIGURATION FILE ----\n'
    ctf += '~# architecture levels = '+str(numLevels)+'\n\n'
    ctf += 'Encription methods\n1) cesar\n2) Monoalphabetical\n3) Permutation\n\n'
    ctf += 'IMPORTANT: Replace <?> with yor own data\n\n'

    flag = 1
    while(flag <= numLevels):
        try:
            lev = int (input('Level '+str(flag)+': '))
        except:
            print('*** ERROR! Invalid input.')
        else:
            inUser = False

            if lev >= 1 and lev <= 3:
                if lev == 1:
                    met = 'cesar'
                elif lev == 2:
                    met = 'mono'
                elif lev == 3:
                    met = 'trans'
                ctf += '~# level '+str(flag)+' = ' + met

                if lev == 1:
                    ctf += '\n~# level '+str(flag)+' cesar key = ?\n\n'
                    flag += 1
                elif lev == 2:
                    while inUser ==  False:
                        sizeKeyMono = input('   Key size (27 or 37): ')
                        if sizeKeyMono == '27' or sizeKeyMono == '37':
                            ctf += '\n~# level '+str(flag)+' mono size key = ' + sizeKeyMono
                            ctf += '\n~# level '+str(flag)+' mono key = ?\n\n'
                            inUser = True
                            flag += 1
                        else:
                            print('*** WARNING! The key size must be 27 or 37')
                elif lev == 3:
                    while inUser ==  False:
                        paddingTrans = input('  Padding [a-z]: ')
                        if paddingValidate(paddingTrans):
                            ctf += '\n~# level '+str(flag)+' trans padding = ' + paddingTrans
                            ctf += '\n~# level '+str(flag)+' trans key = ?\n\n'
                            inUser = True
                            flag += 1
            else:
                print('*** ERROR! Invalid input.')
    mf.createSimpleFile('configFile.txt',ctf)
    print('\n\n*** Config file complete.\n\n')

def main():
    print('-----------------------------------------\n')
    flag = True
    while(flag):
        try:
            numLevels = int(input('NUMBER OF ENCRYPTION LEVELS: '))
        except:
            print('*** WARNING! Invalid input.')
        else:
            if numLevels >= 2 and numLevels <= 6:
                flag = False
            else:
                print('*** WARNING! The range must be between 2 and 6 levels.')
    createConfigFile(numLevels)

if __name__ == '__main__':
    main()