def countSame(string, pos):
    #Counts number of same characters following a position
    pos1 = pos
    count = 0
    while pos1 < len(string) and string[pos1] == string[pos]:
        count = count +1
        pos1 = pos1 + 1
    return count


def String_Compress1(string):
    outstring = []
    pos = 0
    while pos < len(string):
        outstring.append(string[pos] + str(countSame(string, pos)))
        pos = pos + countSame(string, pos)
    result = ''.join(outstring)
    if len(result) < len(string):
        return result
        #print(result)
    else:
        return string
        #print(string)
        
def String_compress2(string_input):
    charcount = 0
    outstring = []
    lastchar = ""
    for char in string_input:
        if char==lastchar:
            charcount +=1
        else:
            if lastchar !="":
                outstring.append(lastchar+str(charcount))
            charcount = 1
        lastchar = char
    outstring.append(lastchar + str(charcount))    
    outstring="".join(outstring)
    if len(outstring)<len(string_input):
        return outstring
    else:
        return string_input

def main():
    test_string = input("Please enter the string")
    print("Compress1 Result：", String_Compress1(test_string))
    print("Compress2 Result：", String_Compress1(test_string))

if __name__ == '__main__':
    main()
