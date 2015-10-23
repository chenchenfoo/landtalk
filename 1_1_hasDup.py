def has_duplicates(values):
    dupval = []
    for i in range(0, len(values)):
        for x in range(i+1, len(values)):
            if values[i]==values[x]:
                #dupval[i]=values[i]  
                dupval.append(values[i])        
    print("Duplicated numbers are " + str(dupval))
            
        
def main():
    testValue = eval(input("enter the numbers"))
    has_duplicates(testValue)
    
if __name__ == '__main__':
    main()
