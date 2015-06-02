def encrypt(string):
    fhalf = string[:len(string)/2]
    sehalf = string[len(string)/2:]
    reversestring = sehalf + fhalf
    lengalpha = int(reversestring[:reversestring.index("~")])
    lengkey = reversestring[:reversestring.index("~"):-1]
    lengthkey = int(lengkey[lengkey.index("~")-1::-1])
    lengthkey1 = lengkey[lengkey.index("~")-1::-1]
    key = fhalf[fhalf.index("~") - lengthkey:fhalf.index("~")]
    alphabet = sehalf[sehalf.index("~") + 1: sehalf.index("~") + lengalpha + 1]
    encryptalphabet = reversestring[reversestring.index(alphabet[len(alphabet)-1])+1:]
    encryptalphabet = encryptalphabet[:encryptalphabet.index(encryptalphabet[len(encryptalphabet) - 1]) - len(lengthkey1) - len(key)]
    indexes = []
    for x in encryptalphabet:
        indexes.append(alphabet.index(x))
    stringofkey = ""
    while len(stringofkey) < len(encryptalphabet):
        stringofkey += key
    stringofkey = stringofkey[:len(encryptalphabet)]
    indexes_of_key = []
    for elem in stringofkey:
        indexes_of_key.append(alphabet.index(elem))
    indexes_of_word = []
    for ind in range(len(encryptalphabet)):
        new_index = indexes[ind] - indexes_of_key[ind]
        if new_index < 0:
            word_index = new_index + lengalpha
            indexes_of_word.append(word_index)
        else:
            indexes_of_word.append(new_index)
    word = ""
    for elem in indexes_of_word:
        word += alphabet[elem]
    return word


def main():
    print(encrypt("vrItommseIal vihack~416~Ilocveakgrithms he"))
    print(encrypt("fl k.ccfsIolskv.~312~ .Ifrckslovelvo"))
    print(encrypt("o?uin uw?stutnfwat?~413~orwa? thfuisnnrsiu"))
    print(encrypt("rc hscesi tcrest~410~thisaecr .rcese"))
if __name__ == '__main__':
    main()
