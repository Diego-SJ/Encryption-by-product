# * ================================== *
# * CESAR ENCRYPTION METHOD *
# * ================================== *
def cesarMethod(plainText,key):

    try:
        int (key)
    except:
        print('\n*** ERROR! The cesar key is not a number or is invalid.')
        exit()

    alphabet = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ0123456789"
    alphaM = "abcdefghijklmnñopqrstuvwxyz"
    cipherText = ""
    for pt in plainText:
        if pt in alphabet:
            cc = alphabet[((alphabet.index(pt) + int(key)) % (len(alphabet)))]
            cipherText += cc
        elif pt in alphaM:
            cipherText += pt
        elif pt == " " or ",":
            cipherText += ","
        else:
            cipherText += ""

    print('\nCesar encrypt ok\n'+cipherText)

    return cipherText

def cesarMethodDec(cipherText,key):
    try:
        int (key)
    except:
        print('\nERROR! The cesar key is not a number or is invalid.')
        exit()
    alphabet = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ0123456789"
    alphaM = "abcdefghijklmnñopqrstuvwxyz"
    plainText = ""
    for pt in cipherText:
        if pt in alphabet:
            plainText += alphabet[((alphabet.index(pt) - int(key)) % (len(alphabet)))]
        elif pt == " " or pt == ",":
            plainText += ","
        elif pt in alphaM:
            plainText += pt
        else:
            plainText += ""

    print('\nCesar decrypt ok\n'+plainText)

    return plainText

# * ================================== *
# * MONOALPHABETICAL ENCRYPTION METHOD *
# * ================================== *
def monoMethod(plainText,monoKeySize,key):
    alphabet = ''
    alphabetNumber = '0123456789'
    if monoKeySize == '27':
        alphabet = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'
    elif monoKeySize == '37':
        alphabet = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ0123456789'
    else:
        print('*** ERROR! Invalid monoalphabetical key, use 27 or 37.')

    alphaM = "abcdefghijklmnñopqrstuvwxyz"
    cipherText = ''
    if keyValidate(alphabet,key):
        for i in range(len(plainText)):
            if plainText[i] in alphabet:
                indxAlpha = alphabet.find(plainText[i])
                cipherText += key[indxAlpha]
            elif plainText[i] in alphabetNumber:
                cipherText += plainText[i]
            elif plainText[i] == " " or plainText[i] == ",":
                cipherText += ","
            elif plainText[i] in alphaM:
                cipherText += plainText[i]
            else:
                cipherText += ""
    else:
        exit()

    print('\nMono encrypt ok\n'+cipherText)

    return cipherText

def monoMethodDec(cipherText,monoKeySize,key):
    try:
        alphabet = ''
        alphabetNumber = '0123456789'
        if monoKeySize == '27':
            alphabet = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'
        elif monoKeySize == '37':
            alphabet = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ0123456789'
        else:
            print('*** ERROR! Invalid monoalphabetical key, use 27 or 37.')
        alphaM = "abcdefghijklmnñopqrstuvwxyz"
        plainText = ''
        if keyValidate(alphabet,key):
            for i in range(len(cipherText)):
                if cipherText[i] in alphabet:
                    indxAlpha = key.find(cipherText[i])
                    plainText += alphabet[indxAlpha]
                elif cipherText[i] in alphabetNumber:
                    plainText += cipherText[i]
                elif cipherText[i] == ' ' or cipherText[i] == ',':
                    plainText += ','
                elif cipherText[i] in alphaM:
                    plainText += cipherText[i]
                else:
                    plainText += ''
        else:
            exit()

        print('\nMono decrypt ok\n'+plainText)

        return plainText
    except:
        print('*** ERROR! Invalid key.')
        exit()

def keyValidate(alphabet,key):
    if(len(alphabet) != len(key)):
        print('\n*** ERROR! The monoalphabetical key must be equal to the alphabet [A-Z][0-9]')
        return False

    flag = True
    for a in alphabet:
        if not a in key:
            flag = False

    if not flag:
        print("\n*** ERROR! A letter from the monoalphabetic alphabet is missing from your key.")
        return False
    else:
        return True

# * ================================== *
# *  TRANSPOSITION ENCRYPTION METHOD   *
# * ================================== *
def get_number_location(key, kywrd_num_list):
    num_loc = ""
    for i in range(len(key)):
        for j in range(len(key)):
            if kywrd_num_list[j] == i:
                num_loc += str(j)
    return num_loc

def keyword_num_assign(key):
    alpha = "12345678"
    kywrd_num_list = list(range(len(key)))
    init = 0
    for i in range(len(alpha)):
        for j in range(len(key)):
            if alpha[i] == key[j]:
                init += 1
                kywrd_num_list[j] = init - 1
    return kywrd_num_list

def keyTransValidate(key):
    alphabet = "12345678"
    if(len(key) > len(alphabet) or len(key) < 4):
        print("\n*** ERROR! The transposition key be must equal to the alphabet [4-8]")
        return False
    flag = 0
    for k in key:
        repeat = 0
        for l in key:
            if l in alphabet:
                if k == l:
                    repeat += 1
            else:
                flag += 1
            if repeat > 1:
                flag += 1
    if flag >= 1:
        print("\n*** ERROR! A key number is repeated or is invalid in transposition method.")
        return False
    else:
        return True

def paddingValidate(padding):
    alpha = "abcdefghijklmnñopqrstuvwxyz"
    flag = True
    if len(padding) > 1:
        print("*** ERROR! Padding must be a only one character.")
        flag = False
    elif padding not in alpha:
        print("*** ERROR! Padding must be a lower case character. [a-z]")
        flag = False
    return flag

def transMethod(plainText,keyin,paddingin):
    key = ''
    padding = ''
    if keyTransValidate(keyin):
        key = keyin
    else:
        exit()
    if paddingValidate(paddingin):
        padding = paddingin
    else:
        exit()

    msg = plainText.replace(' ', ',')

    # assigning numbers to keywords
    kywrd_num_list = keyword_num_assign(key)

    print("\n\n========== Transposition grid ==========\n")
    # printing key
    for i in range(len(key)):
        print(key[i], end=" ", flush=True)
    # for
    print()
    for i in range(len(key)):
        print(str(kywrd_num_list[i]), end=" ", flush=True)
    # for
    print("\n-------------------------")

    # in case characters don't fit the entire grid perfectly.
    extra_letters = len(msg) % len(key)
    # print(extraLetters)
    dummy_characters = len(key) - extra_letters
    # print(dummyCharacters)

    if extra_letters != 0:
        for i in range(dummy_characters):
            msg += padding
    # if

    # print(msg)

    num_of_rows = int(len(msg) / len(key))

    # Converting message into a grid
    arr = [[0] * len(key) for i in range(num_of_rows)]
    z = 0
    for i in range(num_of_rows):
        for j in range(len(key)):
            arr[i][j] = msg[z]
            z += 1
        # for
    # for

    for i in range(num_of_rows):
        for j in range(len(key)):
            print(arr[i][j], end=" ", flush=True)
        print()
    # for

    # getting locations of numbers
    num_loc = get_number_location(key, kywrd_num_list)

    # cipher
    cipher_text = ""
    k = 0
    for i in range(len(key)):
        if k == len(key):
            break
        else:
            d = int(num_loc[k])
        # if
        for j in range(num_of_rows):
            cipher_text += arr[j][d]
        # for
        k += 1

    print('\nTrans encrypt ok\n'+cipher_text)

    return cipher_text

def transMethodDec(cipherText,keyin,padding):
    try:
        msg = cipherText

        key = ''
        if keyTransValidate(keyin):
            key = keyin
        else:
            exit()

        # assigning numbers to keywords
        kywrd_num_list = keyword_num_assign(key)

        num_of_rows = int(len(msg) / len(key))

        # getting locations of numbers
        num_loc = get_number_location(key, kywrd_num_list)

        # Converting message into a grid
        arr = [[0] * len(key) for i in range(num_of_rows)]

        # decipher
        plain_text = ""
        k = 0
        itr = 0

        for i in range(len(msg)):
            d = 0
            if k == len(key):
                k = 0
            else:
                d: int = int(num_loc[k])
            for j in range(num_of_rows):
                arr[j][d] = msg[itr]
                itr += 1
            if itr == len(msg):
                break
            k += 1
        print()

        for i in range(num_of_rows):
            for j in range(len(key)):
                plain_text += str(arr[i][j])

        print('\nTrans decrypt ok\n'+plain_text.replace(padding,''))

        return plain_text.replace(padding,'')
    except:
        print('*** ERROR! Key length does not match encryption key.')
        exit()



