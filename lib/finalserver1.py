import commands
import socket                   # Import socket module
s = socket.socket()             # Create a socket object
s1 = socket.socket()    
host = socket.gethostname()     # Get local machine name
port = 65533                    # Reserve a port for your service.
s.bind((host, port))            # Bind to the port
s.listen(5)
print 'Server listening....'
i=1
while True:
    conn1, addr = s.accept()     # Establish connection with client.
    print 'Got connection from', addr
    data = conn1.recv(500)
    print('Server received', repr(data))
    with open('userdata.txt', 'wb') as f:
         print 'file opened'
         print('receiving data...')
         data = conn1.recv(500)
            # print('data=%s', (data))
         if not data:
            break
        # write data to a file
         f.write(data)
              
    f.close()
    conn1.send('Thank you for connecting file')
    conn1.close()
    print('waiting for con2...')
    conn2, addr = s.accept()
    while True:
        print 'Got connection from', addr
        f = open('userimage.jpg', 'wb')
        print 'file opened'
        while True:
            print('receiving data...')
            data1 = conn2.recv(500)
            if not data1:
                break
            # write data to a file
            f.write(data1)
        f.close()
        conn2.close()
        conn2, addr = s.accept()
        
        print('done got it')
    ################### 
           # Establish connection with client.
        if i!=1:
            conn.send("0")
        conn, addr = s.accept()  
        print 'Got connection from', addr
        filename='userimage.jpg'
        f = open(filename,'rb')
        l = f.read()
        while (l):
            conn.send(l)
            l = f.read()
        f.close()
        #conn.send('Thank you connecting file')
        conn.close()
        if i!=5:
            conn, addr = s.accept()
            conn.send("1")
        
        if i==5:
            #conn.send("0")
            #conn.close()
            break
        i=i+1
        conn2.send("1")
        #####################    
    conn, addr = s.accept()     # Establish connection with client.
    print 'Got connection from', addr
    filename='userdata.txt'
    f = open(filename,'rb')
    l = f.read()
    while (l):
        conn.send(l)
        l = f.read()
    f.close()
       # conn.send('Thank you connecting file')
    conn.close()
    conn, addr = s.accept()     # Establish connection with client.
    print 'Got conn'
    with open('authdata.txt', 'wb') as f:
        print 'file opened'
           # print('receiving data...')
        data = conn.recv(500)
        if data == "1":
             if not data:
                 break
             f.write(data)
    #    if data == "0":
     #        if not data:
      #           break
       #      f.write(data)
    f.close()
    conn.send('Thank you for connecting file')
    conn.close()
#############
    f = open("authdata.txt",'rb')
    l = f.read()
    while (l):
        conn2.send(l)
        l = f.read()
    f.close()
    conn2.close()
    f = open("authdata.txt",'wb')
    f.close()

    break
                                                    

