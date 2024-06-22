first_S = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '(']
first_Z = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '(', 'E']
first_W = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '(']
first_W2 = ['*', ':', '+', '-', '^', 'E']
first_P = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '(']
first_R = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
first_R2 = ['.', 'E']
first_L = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
first_L2 = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'E']
first_C = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
first_O = ['*', ':', '+', '-', '^']

class bcolors:
    OKGREEN = '\033[92m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

class Parser:
    def __init__(self, input):
        self.input = input
        self.index = 0
        self.current = input[0]

    def parse(self):
        self.parse_S()

    def check_if_match(self, expected):
        if(self.current == expected):
            self.index += 1
            if(self.index >= len(self.input)):
                print(f"{bcolors.OKGREEN}Wyrażenie jest zgodne z gramatyką{bcolors.ENDC}")
                return
            else:
                self.current = self.input[self.index]
        else:
            print(f"{bcolors.FAIL}Wyrażenie nie jest zgodne z gramatyką{bcolors.ENDC}")
            print(f"{bcolors.FAIL}Nieprawidłowy znak: {self.current} na pozycji: {self.index + 1}{bcolors.ENDC}")
            exit()

    def parse_S(self):
        if(self.current in first_W):
            self.parse_W()
            self.check_if_match(';')
            self.parse_Z()
        else:
            print(f"{bcolors.FAIL}Wyrażenie nie jest zgodne z gramatyką{bcolors.ENDC}")
            print(f"{bcolors.FAIL}Nieprawidłowy znak: {self.current} na pozycji: {self.index + 1}{bcolors.ENDC}")
            exit()

    def parse_Z(self):
        if(self.current in first_W):
            self.parse_W()
            self.check_if_match(';')
            self.parse_Z()
        else:
            pass

    def parse_W(self):
        self.parse_P()
        self.parse_W_prim()

    def parse_W_prim(self):
        if(self.current in first_O):
            self.parse_O()
            self.parse_W()
        else:
            pass

    def parse_P(self):
        if(self.current == '('):
            self.check_if_match('(')
            self.parse_W()
            self.check_if_match(')')
        else:
            self.parse_R()

    def parse_R(self):
        if(self.current in first_L):
            self.parse_L()
            self.parse_R_prim()
        else:
            print(f"{bcolors.FAIL}Wyrażenie nie jest zgodne z gramatyką{bcolors.ENDC}")
            print(f"{bcolors.FAIL}Nieprawidłowy znak: {self.current} na pozycji: {self.index + 1}{bcolors.ENDC}")
            exit()

    def parse_R_prim(self):
        if(self.current == '.'):
            self.check_if_match('.')
            self.parse_L()
        else:
            pass

    def parse_L(self):
        if(self.current in first_C):
            self.parse_C()
            self.parse_L_prim()
        else:
            print(f"{bcolors.FAIL}Wyrażenie nie jest zgodne z gramatyką{bcolors.ENDC}")
            print(f"{bcolors.FAIL}Nieprawidłowy znak: {self.current} na pozycji: {self.index + 1}{bcolors.ENDC}")
            exit()

    def parse_L_prim(self):
        if(self.current in first_L2):
            self.parse_L()
        else:
            pass
    
    def parse_C(self):
        if(';' not in self.input[self.index:]):
            print(f"{bcolors.FAIL}Wyrażenie niepoprawne. Podane wyrażenie nie jest zakończone średnikiem.{bcolors.ENDC}")
            exit()
        else:
            if(self.current in first_C):
                self.index += 1
                if(self.index >= len(self.input)):
                    print(f"{bcolors.OKGREEN}Wyrażenie jest zgodne z gramatyką{bcolors.ENDC}")
                    return
                else:
                    self.current = self.input[self.index]
            else:

                
                print(f"{bcolors.FAIL}Wyrażenie nie jest godne z gramatyką{bcolors.ENDC}")
                print(f"{bcolors.FAIL}Nieprawidłowy znak: {self.current} na pozycji: {self.index + 1}{bcolors.ENDC}")
                exit()

    def parse_O(self):
        if(self.current in first_O):
            self.index += 1
            if(self.index >= len(self.input)):
                print(f"{bcolors.OKGREEN}Wyrażenie jest zgodne z gramatyką{bcolors.ENDC}")
                return
            else:
                self.current = self.input[self.index]
        else:
            print(f"{bcolors.FAIL}Wyrażenie nie jest zgodne z gramatyką{bcolors.ENDC}")
            print(f"{bcolors.FAIL}Nieprawidłowy znak: {self.current} na pozycji: {self.index + 1}{bcolors.ENDC}") 
            exit()
        

        
print("------------------------------------------------------------------------")
input = input("Podaj wyrażenie: ")

parser = Parser(input)
parser.parse()
print("------------------------------------------------------------------------")

