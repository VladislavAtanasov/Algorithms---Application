def bracket_validation(string):
    opencurls = 0
    opensquar = 0
    opencircl = 0
    for x in string:
        if x == "{":
            opencurls += 1
        elif x == "}":
            opencurls -= 1
        elif x == "(":
            opencircl += 1
        elif x == ")":
            opencircl -= 1
        elif x == "[":
            opensquar += 1
        elif x == "]":
            opensquar -= 1
    if opensquar == 0 and opencircl == 0 and opencurls == 0:
        if "{" in string:
            if string.index('{') != 0:
                return "NO"
            else:
                pass
    else:
        return "NO"


def main():
    print(bracket_validation("{125[12]{125}[12]125}"))

if __name__ == '__main__':
    main()
