import socket

def port_checker(ip, port):

    # This function checks socket is open
    # Timeout of connection is set to 1 second
    # If socket is open - return info to console

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    
    result = sock.connect_ex((ip, port))
    sock.close()

    if result == 0:
        print ('FOUND! IP: {} PORT: {}'.format(ip, port))