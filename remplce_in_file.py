import sys
import os


if len(sys.argv) < 4:
    print("Merci d'indiquer le nom du fichier, la chaine de caractere a remplacer et la chaine de caractere de remplacement.")
    sys.exit()
    
filename = sys.argv[1]
string = sys.argv[2]
replace_string = sys.argv[3]

if not os.path.exists(filename):
    print("Le fichier n'existe pas.")
    sys.exit()

with open(filename, "r") as file:
    content = file.read()

new_content = content.replace(string, replace_string)

with open(filename, "w") as file:
    file.write(new_content)