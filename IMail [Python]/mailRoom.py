import socket
import sys

print("This is the Console")
print("Commands start with '/' type '/tutorial' to get started :)")
print(' ')

sender = "DEFAULT"

def command():
    consoleInput = input()
    if consoleInput == '/help':
        print(' > Help Menue <');
        print(' >> /tutorial : Gives a tutorial for using commands')
        print(' >> /send [message] : Sends a message')
        print(' >> /sender [sender id] : Sets what the sender feild will be in a message (required) ')
        print(' >> /mail [new ; all ; read ; del] [file]: Prints list of new mail, all mail, prints text of a message, or deletes a message')
        print(' ')
        command()
    elif consoleInput == '/sender':
        newInput = input("-Please enter the name for your sender id : ")
        global sender
        sender = newInput
        print(" > Sender Id Set As : " + sender + " <")
        print(' ')
        command()
    elif consoleInput == '/tutorial':
        print(' ')
        print(' -- IMail Commands Tutorial --')
        print(' Commands Like /sender have attributes fields displayed in the help fiels as [attribute]. ')
        print(' These options will appear after you type the command ')
        print(' ')
        print('  Example : ')
        print('  You want to set your sender id as "Friend" ')
        print('  You would type "/sender", it will then ask you for what you want the attribute (in this case your id) to be.')
        print('  This will work with any commands containing attributes "[attribute]" ')
        print(' ')
        print(' All commands start with "/" , but attributes do not.')
        print(' ')
        print(' Find list of all commands and there attributes by typing "/help" ')
        print(' ')
        command()
    elif consoleInput == '/send':
        msgInput = input("-Please enter your message : ")
        ntwInput = input("-Please enter the network to recieve the message : ")
        HOST, PORT = ntwInput, 350
        data = [msgInput, ' [/-split-\] ' , sender]
        dataStr = ''.join(data)

        # Create a socket (SOCK_STREAM means a TCP socket)
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        # Connect to server and send data
            sock.connect((HOST, PORT))
            sock.sendall(bytes(dataStr, "utf-8"))
            
            print("Sent:     {}".format(data))
            print(' ')
        command()
    else:
        print(" > Unknown Command :( <")
        print(' ')
        command()

command()
