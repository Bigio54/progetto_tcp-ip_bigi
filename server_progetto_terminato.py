import socket
import mysql.connector

PASSWORD = "password1234"
#parametri per la connessione al database 
connessione = mysql.connector.connect(
    host="10.10.0.10",
    user="bigi_nicola",
    password="bigi1234",
    database="5BTepsit",
    port=3306
)
cur = connessione.cursor()

def setCRUD(p):
    clausole = ""
    for key, value in p.items():
        clausole += f"and {key} = '{value}' "
    
    return clausole
#------------------------------------------------------------------------------------------------------------
#funzione che legge i valori all'interno della tabella
def lettura(p, x):
    query = ''
    if x == 1:
        query = f"SELECT * FROM dipendente where 1=1 {setCRUD(p)}"
    if x == 2:
        query = f"SELECT * FROM zona_lavoro where 1=1 {setCRUD(p)}"

    cur.execute(query)
    dati = cur.fetchall()
    return dati
#------------------------------------------------------------------------------------------------------------
#funzione che elimina una riga dalla tabella 
def elimina(p, x):
    query = ''
    if x == 1:
        query = f"DELETE FROM dipendente_nicola_bigi where 1=1 {setCRUD(p)}"
    if x == 2:
        query = f"DELETE FROM zona_di_lavoro_bigi_nicola where 1=1 {setCRUD(p)}"

    cur.execute(query)
    connessione.commit()
#-----------------------------------------------------------------------------------------------------------------
#funzione che serve a inserire una riga all'interno di una tabella 
def scrittura(p, x):
    query = ''
    if x == 1:
        query = f"INSERT INTO dipendente_nicola_bigi (nome,indirizzo, telefono, agente) VALUES ('{lista[0]}','{lista[1]}','{lista[2]}','{lista[3]}')"
    if x == 2:
        query = f"INSERT INTO zona_di_lavoro_bigi_nicola (nome_zona, numero_clienti,settore,citta) VALUES ('{lista[0]}','{lista[1]}','{lista[2]}','{lista[3]})"
    cur.execute(query)
    connessione.commit()
#-------------------------------------------------------------------------------------------------------------------
#funzione che serve per mofificare una riga di una tabella 
def modifica(p, x):
    query = ''
    if x == 1:
        query = f"UPDATE dipendente_nicola_bigi SET nome = '{lista[0]}', indirizzo = '{lista[1]}', telefono = '{lista[2]}', agente = '{lista[3]}' WHERE id = '{lista[4]}'"
    if x == 2:
        query = f"UPDATE zona_di_lavoro_bigi_nicola SET nome_zona = '{lista[0]}', numero_clienti = '{lista[1]}', Distretto = '{lista[2]}' WHERE id_zona = '{lista[3]}'"
    cur.execute(query)
    connessione.commit()
#----------------------------------------------------------------------------------------------------------------------
#inizializazione server 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("localhost", 8888))
s.listen()

print("In attesa di connessioni...")

conn, addr = s.accept()
print('Connected by', addr)
#--------------------------------------------------------------------------------------------------------------------
#gestione password 
if __name__ == '__main__':
    for i in range(3):
        password = conn.recv(1024).decode()
        if password == PASSWORD:
            conn.send("Password esatta.".encode())
            break
        else:
            if i < 3:
                conn.send(f"Password errata.\n".encode())
            else:
                conn.send("Tentativi terminati, connessione chiusa.".encode())
                conn.close()
                exit()
#-------------------------------------------------------------------------------------------------------------------
#gestione delle funzioni in base alla risposta
#esco se mette 5  
    while True:
        data = conn.recv(1024).decode()
        if not data:
            break  
        if data == "5":
            break  
#-------------------------------------------------------------------------------
#leggo i dati di una tabella e invio i risultati  
        if data == "1":
            scelta = conn.recv(1024).decode()
            nome = conn.recv(1024).decode()
            if scelta == "1":
                parametri = {"nome": nome}
            else:
                parametri = {"nome_zona": nome}
            result = lettura( parametri, int(scelta))
            conn.send(str(result).encode())
#-------------------------------------------------------------------------
#elimino un istanza dalla tabella            
        elif data == "2":
            scelta = conn.recv(1024).decode()
            id_elimina = conn.recv(1024).decode()
            if scelta == "1":
                parametri = {"id": id_elimina}         
            else:
                parametri = {"id_zona": id_elimina}
            elimina( parametri, int(scelta))
#-------------------------------------------------------------------------------
#inserisco una riga di valori all'interno di una tabella 
        elif data == "3":
            scelta = conn.recv(1024).decode()
            lista = []
            if scelta == "1":
                for i in range(4):
                    lista.append(conn.recv(1024).decode())
                parametri = {"nome": lista[0], "indirizzo": lista[1],"telefono": lista[2], "agente": lista[3]}
                
            else:
                for i in range(4):
                    lista.append(conn.recv(1024).decode())
                parametri = {"nome_zona": lista[0], "numero_clienti": lista[1], "settore": lista[2], "citta":lista[3]}
            scrittura( parametri, int(scelta))
#-----------------------------------------------------------------------------------------
#modifico un valore all'interno della tabella 
        elif data == "4":

            scelta = conn.recv(1024).decode()
            if scelta == "1":
                for i in range(5):
                    lista.append(conn.recv(1024).decode())
                parametri = {"id": lista[0], "nome": lista[1], "indirizzo": lista[2], "telefono": lista[3], "agente": lista[4]}

                
            else:
                for i in range(5):
                    lista.append(conn.recv(1024).decode())
                parametri = {"id_zona": lista[0], "nome_zona": lista[1], "numero_clienti": lista[2], "settore": lista[3],"citta":lista[4]}

            modifica( parametri, int(scelta))
#chiudo la connessione 
    conn.close()