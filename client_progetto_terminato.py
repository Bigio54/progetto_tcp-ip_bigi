import socket
import sys
#-----------------------------------------------------------------------------
#parametri per la connessione al server
HOST = 'localhost' 
PORT = 8888

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
#-----------------------------------------------------------------
#funzione per connettersi al server mediante le password 
def login():
    for i in range(3):
        password = input("Inserisci la password: ")
        s.send(password.encode())
        response = s.recv(1024).decode()
        if response == "Password esatta.":
            print('Password esatta.\n')
            break
        else:
            print(response)
            if i == 2: 
                s.close()
                sys.exit()
#------------------------------------------------------------------
#stampo il menu con le possibili query che si possono eseguire
def menu():
    print("\n Operazioni disponibili:")
    print("1. Leggi i valori di una tabella")
    print("2. Elimina una riga da una tabella  tabella")
    print("3. Inserisci una riga  nella tabella")
    print("4. Modifica un valore all'interno di una  tabella")
    print("5. Esci")    
#---------------------------------------------------------------------
#inserimento per i dipendenti 
def dati_dip():
    s.send(input("Inserisci il nome del dipendente: ").encode())
    s.send(input("Inseriscil'indirizzo del dipendente: ").encode())
    s.send(input("Inserisci il telefono del dipendente: ").encode())
    s.send(input("Inserisci l'agente del dipendente: ").encode())
#--------------------------------------------------------------------
#inserimento dati zona
def dati_zona():
    s.send(input("Inserisci il nome della zona: ").encode())
    s.send(input("Inserisci il numero dei clienti della zona: ").encode())
    s.send(input("Inserisci il settore della zona: ").encode())
    s.send(input("Inserisci la citta della zona:").encode())
#main
if __name__ == '__main__':
    login()
#gestione delle scelte
    while True:
        menu()

        scelta = input("Operazione: ")
        s.send(scelta.encode())

        if scelta == "5":
            print("\nPagina chiusa.\n")
            break

        if scelta == "1":

            scelta2 = 0
            while(scelta2 != "1" and scelta2 != "2"):
                scelta2=input("Inserisci 1 per leggere dipendenti o 2 per le zone: ")

            s.send(scelta2.encode())

            if scelta2 == "1":
                nome_d = input("Inserisci il nome del dipendente: ")
                s.send(nome_d.encode())
                response = s.recv(1024).decode()
                print(response)
            else:
                nome = input("Inserisci il nome della zona: ")
                s.send(nome.encode())
                response = s.recv(1024).decode()
                print(response)

        if scelta == "2":

            scelta2 = 0
            while(scelta2 != "1" and scelta2 != "2"):
                scelta2=input("Inserisci 1 per eliminare dipendenti o 2 per eliminare zone: ")

            s.send(str(scelta2).encode())

            if scelta2 == "1":
                id_elimina = input("Inserisci l'id del dipendente da eliminare: ")
                s.send(id_elimina.encode())
            else:
                id_elimina = input("Inserisci l'id della zona da eliminare: ")
                s.send(id_elimina.encode())

        if scelta == "3":

            scelta2 = 0
            while(scelta2 != "1" and scelta2 != "2"):
                scelta2=input("Inserisci 1 per inserire dipendenti o 2 per inserire zone: ")

            s.send(str(scelta2).encode())

            if scelta2 == "1":
                dati_dip()
            else:
                dati_zona()
                
        if scelta == "4":
            scelta2 = 0
            while(scelta2 != "1" and scelta2 != "2"):
                scelta2=input("Inserisci 1 per modificare dipendenti o 2 per modificare zone: ")

            s.send(str(scelta2).encode())

            if scelta2 == "1":
                id_modifica = input("Inserisci l'id del dipendente: ")
                s.send(id_modifica.encode())
                dati_dip()
            else:
                id_modifica = input("Inserisci l'id della zona: ")
                s.send(id_modifica.encode())
                dati_zona()

    s.close()