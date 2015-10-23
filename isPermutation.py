def isPermutation(S1,S2):
    if len(S1)!=len(S2):
        return False
    else:
        for char in S1:
            if S2.find(char)==-1:
                return False
            else:
                S2=S2.replace(char,"",1)
                return True
            
def main():
    s1 = input("please enter the string 1")
    s2 = input("please enter the string 2")
    if isPermutation(s1, s2):
        print("Yes")
    else:
        print("No")
    
        
        
if __name__ == '__main__':
    main()
