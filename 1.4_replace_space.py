import re

def replace_space(string_input):
    new_string = re.sub(' ', '%20', string_input)
    print(new_string)
    
def main():
    test_string = input("please enter the string")
    replace_space(test_string)
    
if __name__ == '__main__':
    main()
