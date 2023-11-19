import socket


def menu():
    print("inserire 1 per visualizzare tutti i dati di una zona di lavoro inserito l id")
    print("inserire 2 per visualizzare tutti i dati di un cliente inserito l id ")
    
# Indirizzo IP e porta del server a cui ci si connetterà
indirizzo_server = 'localhost'
porta_server = 12345

# Creazione del socket del client
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connessione al server
client_socket.connect((indirizzo_server, porta_server))
tentativi_rimasti=3
while True:
    while tentativi_rimasti>0:
        password =input("inserisci la password per connecterti al server ")
        client_socket.send(str(password).encode('utf-8'))
        response=client_socket.recv(1024).decode('utf-8')
    print(response)
    
    if response == "Password corretta. Connessione riuscita.":
        break
    elif "Tentativi rimasti:" in response:
        tentativi_rimasti -= 1
    else:
        print("Connessione non riuscita.")
        client_socket.close()
        break
#------------------------------------------------------------------------------------------------------
#dipendenti_nicola_bigi
#zona_di_lavoro_bigi_nicola
while True:
    
    menu() 
    risp=int(input())
    while risp<1 or risp>2:
        menu()
        risp=input()
        
    if risp==1:
        print("inserire l id della zona  ")
        tmp=int(input())
    else:
        print("inserire l id del cliente ")
        tmp=int(input()) 
    
    a=str(tmp)
    client_socket.send(a.encode("utf-8")) 
    response=client_socket.recv(1024).decode("utf-8")
    print(response) 

      

    

# Chiude la connessione
client_socket.close()