from colorama import Fore, Back, Style
import os
# os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

NPM_FILE = "npm.txt"
PIP_FILE = "pip.txt"

def printBorder(backcolor="", forecolor="", text=""):
	print(backcolor + forecolor + "\n" + text + Style.RESET_ALL + "\n")

def printTop(message): print("\n" + Fore.BLUE + message)
def printImperative(message): print("\n" + Fore.RED + message)
def printFinish(): reset()
def reset(): print(Fore.WHITE+Back.BLACK+Style.NORMAL)
def printList(items): 
	print(Fore.YELLOW)
	for i in items:
		print("*", i.replace("\n", ""))

def readFile(txtfile):
	with open(txtfile) as tf:
		printList(tf)

def installAll():
      installNpm()
      installPip()
	
def installNpm():
	os.system("npm i -r npm.txt")
	
def installPip():
	os.system("pip install -r pip.txt")

if __name__ == "__main__":
    printTop("DOWN BELOW LIST NPM TO INSTALL:")
    readFile(NPM_FILE)

    printTop("DOWN BELOW LIST PIP TO INSTALL:")
    readFile(PIP_FILE)
    
    print(Style.BRIGHT)
    printTop("Do You Want To Install ALL?\n")
    print(Fore.WHITE+"options:",end="")
    printList(["1 : Yes/y", "2 : (Just using npm install)npm", "3 : (Just using pip install)pip", "4/(or other number) : Cancel/c"])
    printImperative("Choose from option!")
    reset()
    while(True):
        choiceInstall = input("Your Input :")
        if choiceInstall.isdigit():
            if choiceInstall == "1":
                installAll()
            elif choiceInstall == "2":
                installNpm()
            elif choiceInstall == "3":
                installPip()
            else:
                printImperative("Please input a number from options menu!")
                reset()
                continue
        else:
            printImperative("Please input a number from options menu!")
            reset()
            continue
        break
    printFinish()