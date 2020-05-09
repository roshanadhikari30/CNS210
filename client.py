import tkinter
from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread

def receive_message():
    
    while True:
        try:
            msg = sock.recv(BUFFERSIZE).decode("utf8")
            msg_list.insert(tkinter.END, msg)
        except OSError:  
            break

def send_message(event=None):
    msg = my_msg.get()
    my_msg.set("")  # Clears input field.
    sock.send(bytes(msg, "utf8"))
    if msg == "exit":
        sock.close()
        top.quit()

def on_closing(event=None):                       
    my_msg.set("exit")      #this functions gets called when window is closed
    send_message()

top = tkinter.Tk()
top.title("Chat Client")
messages_frame = tkinter.Frame(top)

my_msg = tkinter.StringVar()  # For the messages to be sent.
my_msg.set("")
scrollbar = tkinter.Scrollbar(messages_frame)  # To navigate through past messages.
msg_list = tkinter.Listbox(messages_frame, height=15, width=50, yscrollcommand=scrollbar.set)
scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
msg_list.pack(side=tkinter.LEFT, fill=tkinter.BOTH)
msg_list.pack()

messages_frame.pack()

button_label = tkinter.Label(top, text="Enter Message:")
button_label.pack()
entry_field = tkinter.Entry(top, textvariable=my_msg, foreground="Green")
entry_field.bind("<Return>", send_message)
entry_field.pack()
send_button = tkinter.Button(top, text="Send", command=send_message)
send_button.pack()
quit_button = tkinter.Button(top, text="Quit", command=on_closing)
quit_button.pack()
top.protocol("WM_DELETE_WINDOW", on_closing)
HOST = "127.0.0.1"
PORT = 1234
BUFFERSIZE = 1024
ADDR = (HOST, PORT)
sock = socket(AF_INET, SOCK_STREAM)
sock.connect(ADDR)
receive_thread = Thread(target=receive_message)
receive_thread.start()
tkinter.mainloop()  