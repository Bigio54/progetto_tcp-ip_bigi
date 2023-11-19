import socket
import mysql.connector

# Indirizzo IP e porta su cui il server ascolterà le connessioni
indirizzo_server = 'localhost'
porta_server = 12345

# Connessione al database MySQL
def db_get(parametri,pp):
    conn = mysql.connector.connect(
        host="10.10.0.10",
        user="bigi_nicola",
        password="bigi1234",
        database="5BTepsit",
        port=3306
    )
    cur = conn.cursor()

    # si chiama una funzione di libreria passando i parametri di ricerca dell'utente. esempio controlla_caratteri(nome)
    clausole = ""
    for key,value in parametri.items():
        clausole += f"and {key} = '{value}'"
    c=""
    for key,value in pp.items():
        c+=f"and {key} = '{value}'"
    


    query = f"SELECT * FROM dipendenti_nicola_bigi where 1=1 {clausole}"
    print(query)
    cur.execute(query)
    dati = cur.fetchall()
    if not dati:
        query=f"SELECT * FROM zona_di_lavoro_bigi_nicola where 1=1 {c}"
        cur.execute(query)
        dati=cur.fetchall()
    print(dati)

    return dati



# Creazione del socket del server
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Associazione del socket all'indirizzo e alla porta
server_socket.bind((indirizzo_server, porta_server))

# Il server ascolta le connessioni in entrata
server_socket.listen(0)

print(f"In attesa di connessioni su {indirizzo_server}:{porta_server}")

# Accetta la connessione dal client
client_socket, client_address = server_socket.accept()
print(f"Connessione accettata da {client_address}")
password_segreta="password1234"
tentativi_rimasti=3

while tentativi_rimasti > 0:
    password_inserita = client_socket.recv(1024).decode('utf-8')
    
    if password_inserita == password_segreta:
        print("Password corretta. Connessione riuscita.")
        client_socket.send("Password corretta. Connessione riuscita.".encode('utf-8'))
        break
    else:
        print("Password errata. Riprova.")
        tentativi_rimasti -= 1
        if tentativi_rimasti > 0:
            print(f"Tentativi rimasti: {tentativi_rimasti}")
            client_socket.send("Password errata. Riprova.".encode('utf-8'))
        else:
            print("Numero massimo di tentativi raggiunto. Connessione terminata.")
            client_socket.send("Numero massimo di tentativi raggiunto. Connessione terminata.".encode('utf-8'))
            client_socket.close()

while True:
    a=client_socket.recv(1024).decode("utf-8")
    par={"id_zona":a}
    p={"id":a}
   
    var=db_get(par,p)
    
    client_socket.send(str(var).encode('utf-8'))

# Chiude la connessione
client_socket.close()
server_socket.close()