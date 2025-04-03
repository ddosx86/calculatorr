# touch description
a = "+" # touch you want to use for addition
s = "-" # touch you want to use for substraction
mult = "x" # touch you want to use for multiplication
d = "/" # touch you want to use for division
rep = "ans" # this his the touch for call the result of the previous calculus 
# sys variable
saveans = 1
print("Welcome to calculatorr v1.0 ")
from colorama import Fore, Style

# read the banner file
with open("logo.txt", "r") as file:
        logo = file.read()
# read the help file
with open("help.txt", "r") as file:
            h = file.read()

# print banner
print(Fore.GREEN + logo + Style.RESET_ALL)
# print the skeleton
print("Entrez une opération ou 'exit' pour quitter et h pour la liste des commande  ")
while True:
    i = input("calc:</ ") #ask the operation; you can change the prompt here
    # function
    def add (i):
        global rep
        global saveans
        part = i.split(a)
        if part[0] == rep:
            nb1 = saveans
        else:
            nb1 = float(part[0])
        
        if part[1] == rep:
            nb2 = saveans
        else:
            nb2 = float(part[1])
        
        saveans = nb1 + nb2
        return saveans
    
    def sous (i):
        global rep
        global saveans
        part = i.split(s)
        if part[0] == rep:
            nb1 = saveans
        else:
            nb1 = float(part[0])
        
        if part[1] == rep:
            nb2 = saveans
        else:
            nb2 = float(part[1])
        
        saveans = nb1 - nb2
        return saveans
    
    def prod (i):
        global rep
        global saveans
        part = i.split(mult)
        if part[0] == rep:
            nb1 = saveans
        else:
            nb1 = float(part[0])
        
        if part[1] == rep:
            nb2 = saveans
        else:
            nb2 = float(part[1])
        
        saveans = nb1 * nb2
        return saveans
    
    def div (i):
        global rep
        global saveans
        part = i.split(d) 
        if part[0] == rep: 
            nb1 = saveans 
        else: 
            nb1 = float(part[0])
        
        if part [1] == rep:
            if saveans == 0: 
                return "la division par zero est imposible" 
            else: 
                nb2 = saveans
                saveans = nb1 / nb2
                return saveans
        else:   
            nb2 = float(part[1])
            if nb2 == 0:
                return "division by zero isn't possible"
                
            else: 
                saveans = nb1 / nb2
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
             print(add(i))
        
        case _ if s in i:
             print(sous(i))
        
        case _ if mult in i:
            print(prod(i))
        
        case _ if d in i:
            print(div(i))
        
    

    



