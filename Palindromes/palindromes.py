def palindromes(inputstr):
    rotations_list_all = set()
    for x in range(len(inputstr)+1):
        rotated = ""
        rotated = inputstr[x:] + inputstr[:x]
        rotations_list_all.add(rotated)
    rotations_list = []
    for elem in rotations_list_all:
        if elem == elem[::-1]:
            rotations_list.append(elem)
    if len(rotations_list) == 0:
        print("NONE")
    else:
        for elem in rotations_list:
            print(elem)


def main():
    palindromes("shakira")
    palindromes("labalaa")
    palindromes("akawwaka")

if __name__ == '__main__':
    main()
