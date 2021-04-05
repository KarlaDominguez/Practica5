from bs4 import BeautifulSoup
import requests
import re

def mostrarJugadores():
    print("╔══════════════════════════════════════════════════════════════╗")
    print("║      Lista de Jugadores de los Yankis de Nueva York          ║")
    print("╠════════════════════════════╦═════════════════════════════════╣")
    print("║ Nombre del jugador         ║          Codigo                 ║")
    print("╠════════════════════════════╬═════════════════════════════════╣")
    print("║ Aaron Judge         #99    ║       aaron-judge-592450        ║")
    print("║ Albert Abreu        #84    ║       albert-abreu-656061       ║")
    print("║ Aroldis Chapman     #54    ║       aroldis-chapman-547973    ║")
    print("║ Ben Heller          #61    ║       ben-heller-621294         ║")
    print("║ Chad Green          #57    ║       chad-green-643338         ║")
    print("║ Deivi García        #83    ║       deivi-garcia-665620       ║")
    print("║ Domingo Germán      #55    ║       domingo-german-593334     ║")
    print("║ Estevan Florial     #90    ║       estevan-florial-664314    ║")
    print("║ Gary Sánchez        #24    ║       gary-sanchez-596142       ║")
    print("║ Gerrit Cole         #45    ║       gerrit-cole-543037        ║")
    print("║ Luis Cessa          #85    ║       luis-cessa-570666         ║")
    print("║ Luke Voit           #59    ║       luke-voit-572228          ║")
    print("║ Mike Tauchman       #39    ║       mike-tauchman-643565      ║")
    print("║ Michael King        #73    ║       michael-king-650633       ║")
    print("║ Nick Nelson         #79    ║       nick-nelson-656793        ║")
    print("║ Kyle Higashioka     #66    ║       kyle-higashioka-543309    ║")
    print("║ Tyler Wade          #14    ║       tyler-wade-642180         ║")
    print("║ Zack Britton        #53    ║       zack-britton-502154       ║") 
    print("╚════════════════════════════╩═════════════════════════════════╝")

def Jugadores():
        lista_codigo=[
        'aaron-judge-592450','albert-abreu-656061','aroldis-chapman-547973','ben-heller-621294','chad-green-643338',
        'deivi-garcia-665620','domingo-german-593334','estevan-florial-664314','gary-sanchez-596142','gerrit-cole-543037',
        'luis-cessa-570666','luke-voit-572228','mike-tauchman-643565','michael-king-650633','nick-nelson-656793',
        'kyle-higashioka-543309','tyler-wade-642180','zack-britton-502154',
        ]
        link1='https://www.mlb.com/player/aaron-judge-592450'
        x="1"
        while(x=="1"):
            i=0
            w = str(input("  Introduzca un jugador: "))
            print("════════════════════════════════════════════════════════════════")
            if w in lista_codigo:
                jugador = w
                page = requests.get(link1+jugador)
                soup = BeautifulSoup(page.content ,"html.parser")
                inf = soup.find_all("ul")
                infText= inf[1].getText()
                z = infText.replace("                             ", "")
                y = z.replace("\n", "\n  ")
                print(y, end = '')
                data= page.text
                twitter= re.findall(r'(https://twitter?[\w\.%:\/-@]+)',data)
                instagram= re.findall(r'(https:/[\w\.%:\/-]+instagram?[\w\.%:\/-@]+)', data)
                if twitter:
                    print("Twitter:   " , end = ' ') 
                    print(twitter[0],end = '\n  ')
                if instagram:    
                    print("Instagram: ", end = ' ' )
                    print(instagram[0], end = ' ')
                print("")
                x = input("╔══════════════════════════════════════════════════════════════╗\n║                ¿Desea continuar la busqueda?                 ║\n╠═══════════════════════════════╦══════════════════════════════╣\n║              Si               ║               1              ║\n╠═══════════════════════════════╬══════════════════════════════╣\n║              No               ║               2              ║\n╚═══════════════════════════════╩══════════════════════════════╝\n   ").lower()
                print("════════════════════════════════════════════════════════════════")
                if x in ("1"): 
                    mostrarJugadores() 
            else:
                print("codigo no valido")

mostrarJugadores()

Jugadores()
