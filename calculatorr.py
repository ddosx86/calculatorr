#!/usr/bin/env python3
import os
# touch description
a = "+" # touch you want to use for addition
s = "-" # touch you want to use for substraction
mult = "x" # touch you want to use for multiplication
d = "/" # touch you want to use for division
exp = "e"#touch you want to use for exponent
fact = "!" # touch you want to use for factorial
rep = "ans" # this his the touch for call the result of the previous calculus 
# sys variable
saveans = 1
print("Welcome to calculatorr v1.1 ")
from colorama import Fore, Style
# import the path
path = os.path.expanduser("~/.local/bin")
# read the banner file
with open(f"{path}/logo.txt") as file:
        logo = file.read()
# read the help file
with open(f"{path}/help.txt") as file:
            h = file.read()

# print banner
print(Fore.GREEN + logo + Style.RESET_ALL)
# print the skeleton
print("Enter an operation or 'exit' to quit and 'h' for help/command list  ")
while True:
    i = input("calc:</ ").strip() #ask the operation; you can change the prompt here
    i = "".join(i.split())
    # function
    
    def carry (nb1, nb2, op):
        global rep
        global saveans
        match op:
            case 1:
                nb1 = nb1.strip()
                nb2 = nb2.strip()
                if nb1 == rep:
                    nb1 = saveans
                else:
                    nb1 = float(nb1)
                if nb2 == rep:
                    nb2 = saveans
                else:
                    nb2 = float(nb2)
                saveans = nb1 + nb2
                return saveans
            case 2:
                nb1 = nb1.strip()
                nb2 = nb2.strip()
                if nb1 == rep:
                    nb1 = saveans
                else:
                    nb1 = float(nb1)
                if nb2 == rep:
                    nb2 = saveans
                elif nb2 == 0:
                    saveans = nb1
                    return saveans
                else:
                    nb2 = float(nb2)
                if nb2 == 0:
                    saveans = nb1
                    return saveans
                else:
                    saveans = nb1 - nb2
                    return saveans
            case 3:
                nb1 = nb1.strip()
                nb2 = nb2.strip()
                if nb1 == rep:
                    if saveans == 0:
                        return saveans
                    else:
                        nb1 = saveans
                else:
                    nb1 = float(nb1)
                if nb2 == rep:
                    if saveans == 0:
                        return saveans
                    else:
                        nb2 = saveans
                else:
                    nb2 = float(nb2)
                saveans = nb1 * nb2 
                return saveans
            case 4:
                nb1 = nb1.strip()
                nb2 = nb2.strip()
                if nb1 == rep:
                    nb1 = saveans
                else:
                    nb1 = float(nb1)
                if nb2 == rep:
                    if saveans == 0:
                        return "division by zero isn't possible"
                    elif saveans == 1:
                        return nb1
                    else:
                        nb2 = saveans
                else:
                    if nb2 == "0":
                        return "division by zero isn't possible"
                    else:
                        nb2 = float(nb2)

                saveans = nb1 / nb2
                return saveans
            case 5:
                nb1 = nb1.strip()
                nb2 = nb2.strip()
                if nb1 == 0:
                    saveans = 0
                    return saveans
                if nb1 == 1:
                    saveans = 1
                    return saveans
                if nb2 == 0:
                    saveans = 1
                    return saveans
                if nb2 == 1:
                    saveans = nb1 
                    return saveans
                nb1 = float(nb1)
                nb2 = float(nb2)
                saveans = nb1 ** nb2
                return saveans
            case 6:
                nb1 = nb1.strip()
                number = []
                i = 1
                if nb1 == rep:
                    nb1 = saveans
                else:
                    nb1 = int(nb1)
                if nb1>1558:
                    return"value to big. do not exceed 1558"
                while i < nb1:
                    i = i + 1
                    number.append(i)
                result = 1
                for n in number:
                    result *= n
                saveans = result 
                return saveans
                

                    


                
                        

    
    match i:
        # if we want to quit
        case _ if "exit" in i:
            print("Bye !")
            break
        
        # print the help file
        case _ if "h" in i:
            print(h)
        
        case _ if a in i:
            part = i.split(a)
            nb1 = part[0]
            nb2 = part[1]
            print(carry(nb1, nb2, 1))
            
        
        case _ if s in i:
            part = i.split(s)
            nb1 = part[0]
            nb2 = part[1]
            print(carry(nb1, nb2, 2))
        
        case _ if mult in i:
            part = i.split(mult)
            nb1 = part[0]
            nb2 = part[1]
            print(carry(nb1, nb2, 3))
        
        case _ if d in i:
            part = i.split(d)
            nb1 = part[0]
            nb2 = part[1]
            print(carry(nb1, nb2, 4))
        case _ if exp in i:
            part = i.split(exp)
            nb1 = part[0]
            nb2 = part[1]
            print(carry(nb1, nb2, 5))
        case _ if fact in i:
            part = i.split(fact)
            nb1 = part[0]
            nb2 = 0
            print(carry(nb1 ,nb2 ,6))
        case _ if rep in i:
            print(saveans)
        
        case _:
            print("unrecognized operation: type h to see help. If necessary modify the operation keys, see the wiki :)")
    

    



