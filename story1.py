
import time
from colorama import Fore, Back, Style

#this is are python story

def ask():#this is choice number 1 of whether uou want to do the mission of saving a dog or not
    ask=str(input("Do you accept this" + Fore.RED + " mission?" + Fore.RESET+"\'type yes or no\' "))
    if (ask == "yes" or ask == "Yes" ) :
        ask = True
        print(Back.CYAN + "Your mission is to save a dog from a well." + Back.RESET)
        print(Fore.RED + "Go find supplies to save dog. " +Fore.RESET)
    elif(ask == "no" or ask == "No" ):
        ask = False
        print(Back.CYAN + "Go get some dinner. " + Back.RESET)
    return ask
    
def choice1(): #This asks what should you do if you wanted to save the dog.
    x=str(input("What do you get " + Back.GREEN+ "a bucket and rope" + Back.RESET + " or " + Back.GREEN + "a firefighter" + Back.RESET + "?\'type bucket and rope or firefighter:\' "))
    if (x == "bucket and rope"):
        print ("What type of" + Back.BLACK +Fore.YELLOW + " transportation" + Back.RESET + Fore.RESET + "?")
    elif (x == "firefighter"):
        exit(Fore.RED + "You failed. It is the fire season, they are busy." + Fore.RESET)
    else:
        print("You can't type. You failed ")
    return x    
    
def transportation():#who want to take a taxi 
    t=str(input("What"+ Back.BLACK + Fore.YELLOW + "transportation" + Back.RESET + Fore.RESET + " do you want?\'type taxi or bus:\' "))
    if (t == 'bus'):
        print("What type of knots?")
    else:
        exit(Fore.RED + "You failed. It is dirty you got sick and died." + Fore.RESET)
    return t
    
def bus():#What type of knot in neccessary and best fit to save the dog.
    b=str(input(Fore.CYAN+ "How would you tie the knot, Double hitch or double knot? \'type Double hitch or double knot\'" + Fore.RESET))
    if (b == "Double hitch"):
        print(Fore.GREEN + "You saved the dog. You win!!!" + Fore.RESET)
    else:
        exit(Fore.RED +"You failed. It is not strong enough."+ Fore.RESET)
    return b

def eat():#Every hour goes by you get a hour closer to your next pizza.... This code is asking them what they want to eat :)
    a=str(input(Fore.CYAN + "Where would you go to eat," + Fore.RESET + Fore.GREEN + "Chipotle or Pizza Hut" + Fore.RESET + Fore.CYAN + "? \'type pizza hut or chipotle\'" + Fore.RESET))
    if a==("pizza hut"):
        print("What types of " +Back.WHITE +Fore.GREEN + "topping" +Back.RESET +Fore.RESET+ " do you want? \'meat lover or cheese\'  ")
    else:
        print(Back.WHITE+ Fore.GREEN+ 'You got diarrhea and failed.'+Back.RESET + Fore.RESET)
        exit()
        return a

def dog():#This asks what topping you would get for your pizza.
    dog=str(input(Fore.RED + "(Hint: You are lactose intolerance.) " + Fore.RESET))
    if dog==("meat lover"):
        print("Good pick." + Fore.YELLOW +"Let's go get a dog." + Fore.RESET)
    else:
        print(Fore.RED + "You failed. You are lactose intolerance:(" + Fore.RESET)
        exit()
        return dog

def store():#This questions you on What place you would go to get a new dog.
    p=str(input("Where do you want to go," + Back.WHITE + Fore.BLUE + "Petco or a sketchy van" + Back.RESET + Fore.RESET + "? \'type petco or van \' "))
    if p==("petco"):
        print(Fore.GREEN + "You got a new normal dog, yay!" + Fore.RESET)
    elif p==("van"):
        print(Fore.YELLOW + "You got a new super power dog!!! THAT'S SUPER!" + Fore.RESET)
        return p

ask  = ask()
if(ask == True):
    choice1()
    transportation()
    bus()

if(ask == False):       
    print("Let's go buy some food to eat. ")
    a = eat()
    dog()
    store()
exit = input("If you would like to end this program, press enter.")

    