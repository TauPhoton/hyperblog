#Sustitution method coder/decoder script
#Tau Photon Jan 17th 2022

import string

def run():
    permanency = True

    while permanency:
        print ("""encrypt[e]
                  decrypt[d]
              
                  """)
        menu_option = input('enter an option:_ ').lower()
        if menu_option == 'e':
            pass
        elif menu_option == 'd':
            pass
        permanency = False

if __name__ == '__main__':
    run()