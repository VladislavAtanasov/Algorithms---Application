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
    encryptalphabet = reversestring[reversestring.index(alphabet[len(alphabet)-1])+1:reversestring.index(alphabet[len(alphabet)-1])+18]
    print(encryptalphabet)
    indexes = []
    for x in encryptalphabet:
        indexes.append(alphabet.index(x))
    print(indexes)
    print(x/16 + x%16 )
def main():
    encrypt("vrItommseIal vihack~416~Ilocveakgrithms he")

if __name__ == '__main__':
    main()
