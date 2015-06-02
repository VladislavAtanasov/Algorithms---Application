def encrypt(string):
    fhalf = string[:len(string)/2]
    sehalf = string[len(string)/2:]
    reversestring = sehalf + fhalf
    print(reversestring)
    lengalpha = int(reversestring[:reversestring.index("~")])
    print(lengalpha)
    lengkey = reversestring[:reversestring.index("~"):-1]
    lengthkey = int(lengkey[lengkey.index("~")-1::-1])
    print(lengthkey)
    key = fhalf[fhalf.index("~") - lengthkey:fhalf.index("~")]
    print(key)
    alphabet = sehalf[sehalf.index("~") + 1: sehalf.index("~") + lengalpha + 1]
    print(alphabet)
    encryptalphabet = reversestring[reversestring.index(alphabet[len(alphabet)-1])+1:reversestring.index(alphabet[len(alphabet)-1])+len(alphabet) + 2]
    print(encryptalphabet)
    indexes = []
    for x in encryptalphabet:
        indexes.append(alphabet.index(x))
    print(indexes)
    stringofkey = ""
    while len(stringofkey) < len(encryptalphabet):
        stringofkey += key
    stringofkey = stringofkey[:len(encryptalphabet)]
    print(stringofkey)
    indexes_of_key = []
    for elem in stringofkey:
        indexes_of_key.append(alphabet.index(elem))
    print(indexes_of_key)
    indexes_of_word = []
    for ind in range(len(encryptalphabet)):
        new_index = indexes[ind] - indexes_of_key[ind]
        if new_index < 0:
            word_index = new_index + lengalpha
            indexes_of_word.append(word_index)
        else:
            indexes_of_word.append(new_index)
    print(indexes_of_word)
    word = ""
    for elem in indexes_of_word:
        print(encryptalphabet[elem])
        word += alphabet[elem]
    print(word)


def main():
    encrypt("o?uin uw?stutnfwat?~413~orwa? thfuisnnrsiu")

if __name__ == '__main__':
    main()
