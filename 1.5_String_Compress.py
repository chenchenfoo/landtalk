def countSame(string, pos):
    #Counts number of same characters following a position
    pos1 = pos
    count = 0
    while pos1 < len(string) and string[pos1] == string[pos]:
        count = count +1
        pos1 = pos1 + 1
    return count


def String_Compress(string):
    outstring = []
    pos = 0
    while pos < len(string):
        outstring.append(string[pos] + str(countSame(string, pos)))
        pos = pos + countSame(string, pos)
    result = ''.join(outstring)
    if len(result) < len(string):
        return result
    else:
        return string

def main():
    test_string = input("Please enter the string")
    String_Compress(test_string)

if __name__ == '__main__':
    main()
