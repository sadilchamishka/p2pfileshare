import socket

def message_with_length(message):
    '''
    Helper function to prepend the length of the message to the message itself
    Args:
        message (str): message to prepend the length
    Returns:
        str: Prepended message
    '''
    message = " " + message
    message = str((10000+len(message)+5))[1:] + message
    return message

def BoostrapRegistrate(bs, client):
    '''
    Register node at bootstrap server.
    Args:
        bs (Node): Bootstrap server node
        me (Node): This node
    Returns:
        list(Node) : List of other nodes in the distributed system
    Raises:
        RuntimeError: If server sends an invalid response or if registration is unsuccessful
    '''
    #self.unreg_from_bs()
    buffer_size = 1024
    message = "REG "+ client.ip + " " +str(client.port) +" " + client.name
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    msg = bytes(message_with_length(message),"utf-8")
    addr = (bs.ip, bs.port)
    client_socket.sendto(msg, addr)
    data, server = client_socket.recvfrom(buffer_size)
    client_socket.close()
    data = data.decode("utf-8")
    print(data)
    
    toks = data.split()
    
    if (len(toks) < 3):
        raise RuntimeError("Invalid message")
    
    if (toks[1] != "REGOK"):
        raise RuntimeError("Registration failed")
    
    num = int(toks[2])
    if (num < 0):
        raise RuntimeError("Registration failed")
        
    return toks
    
def BoostrapUnRegistrate(bs, client):
    '''
    Unregister node at bootstrap server.
    Args:
        bs (tuple(str, int)): Bootstrap server IP address and port as a tuple.
        me (tuple(str, int)): This node's IP address and port as a tuple.
        myname (str)        : This node's name
    Returns:
        list(tuple(str, int)) : List of other nodes in the distributed system
    Raises:
        RuntimeError: If unregistration is unsuccessful
    '''
    buffer_size = 1024
    message = "UNREG "+ client.ip + " " +str(client.port) +" " + client.name

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    msg = bytes(message_with_length(message),"utf-8")
    addr = (bs.ip, bs.port)
    client_socket.sendto(msg, addr)
    data, server = client_socket.recvfrom(buffer_size)
    client_socket.close()
    
    data = data.decode("utf-8")
    toks = data.split()
    print(data)
    if (toks[1] != "UNROK"):
        raise RuntimeError("Unreg failed")
