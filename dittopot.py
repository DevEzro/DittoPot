import socket

HOST = "0.0.0.0"
PORT = 22222

def title():
    print(r'''
    ___ _____  _____  _____  ___  ___  ___  _____ 
   /   \\_   \/__   \/__   \/___\/ _ \/___\/__   \
  / /\ / / /\/  / /\/  / /\//  // /_)//  //  / /\/
 / /_//\/ /_   / /    / / / \_// ___/ \_//  / /   
/___,'\____/   \/     \/  \___/\/   \___/   \/                                                  
              
              MINIMALIST HONEYPOT
    ''')
    
def run_honeypot():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as srv:
        srv.bind((HOST, PORT))
        srv.listen()
        print(f"Listening ({HOST}:{PORT}): ")
        
        while True:
            conn, addr = srv.accept()
            print(f"[WARN] Connection detected - IP: {addr}")
            conn.sendall(b"Access Denied\n")
            conn.close()
            
if __name__ == "__main__":
  title()
  run_honeypot()