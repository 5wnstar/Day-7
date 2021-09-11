import socket
def find_service_name():
    protocolname = str(input("Enter Your Protocol name TCP or UDP:"))
    p=int(input("Enter the port:"))
    for port in [p]:
        print ("Port:  => service name: ", (port, socket.getservbyport(port, protocolname)))
if __name__ == '__main__':
 find_service_name()
