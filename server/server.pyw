'''
Creates the client GUI and processes the requests
'''
# For the socket connection
import socket
# For the GUI
import tkinter
from tkinter.scrolledtext import ScrolledText


class Spacer(tkinter.Label):  # pylint: disable=too-many-ancestors
    '''
    Loads a blank space by putting a label in
    '''

    def __init__(self, root):
        '''
        Loads the blank space
        '''
        self.root = root

        super().__init__(self.root)

        self.config(text="")


class ServerGUI(tkinter.Frame):  # pylint: disable=too-many-ancestors
    '''
    Loads all of the GUI sections and contains their methods
    '''

    def __init__(self, root):
        '''
        Loads the GUI sections
        '''

        self.root = root

        super().__init__(self.root)

        self.server_alive = False

        # Set up the two main frames needed

        self.info_fr = tkinter.Frame(self.root)
        self.info_fr.pack(fill=tkinter.X, side=tkinter.LEFT,
                          expand=True, anchor=tkinter.N)

        self.log_fr = tkinter.Frame(self.root)
        self.log_fr.pack(fill=tkinter.BOTH, side=tkinter.RIGHT, expand=True)

        self.set_info_frame()

        self.set_log_fr()

    def set_info_frame(self):
        '''
        Sets up the entry for the needed connection information
        '''

        # Host frame
        self.host_fr = tkinter.Frame(self.info_fr)
        self.host_fr.pack(fill=tkinter.X, expand=True)

        # Host label
        tkinter.Label(self.host_fr, text="Host:").pack(
            fill=tkinter.X, side=tkinter.LEFT, expand=True)

        # Host entry
        self.host_ent = tkinter.Entry(self.host_fr)
        self.host_ent.pack(
            fill=tkinter.X, side=tkinter.RIGHT, expand=True, padx=3, pady=3)

        # port frame
        self.port_fr = tkinter.Frame(self.info_fr)
        self.port_fr.pack(fill=tkinter.X, expand=True)

        # port label
        tkinter.Label(self.port_fr, text="Port:").pack(
            fill=tkinter.X, side=tkinter.LEFT, expand=True)

        # port entry
        self.port_ent = tkinter.Entry(self.port_fr)
        self.port_ent.pack(fill=tkinter.X,
                           side=tkinter.RIGHT, expand=True, padx=3, pady=3)

        Spacer(self.info_fr).pack(fill=tkinter.X, expand=True)

        tkinter.Button(self.info_fr, text="Start Server", command=lambda: self.start_server()).pack(
            fill=tkinter.X, expand=True)

    def set_log_fr(self):
        '''
        Sets the widgets in the log frame section for server O/I
        '''

        self.log_msg = ScrolledText(self.log_fr, state="disabled")
        self.log_msg.pack(fill=tkinter.BOTH, expand=True, padx=3, pady=3)

        self.add_log_text("Waiting for host and port...")

        self.input_fr = tkinter.Frame(self.log_fr)
        self.input_fr.pack(fill=tkinter.BOTH, expand=True, padx=2, pady=2)

        self.input_ent = tkinter.Entry(self.input_fr)
        self.input_ent.pack(fill=tkinter.BOTH,
                            side=tkinter.LEFT, expand=True, padx=3, pady=3)
        self.input_ent.bind("<Return>", lambda e: self.send_data())

        # Send button
        tkinter.Button(self.input_fr, text="send", command=lambda: self.send_data()).pack(
            fill=tkinter.BOTH, side=tkinter.LEFT, expand=True, padx=3, pady=3)

        # Close button
        tkinter.Button(self.input_fr, text="close server", command=lambda: self.close_server()).pack(
            fill=tkinter.BOTH, side=tkinter.LEFT, expand=True, padx=3, pady=3)

    def start_server(self):
        '''
        Opens the socket connection
        '''

        if self.server_alive:
            self.add_log_text(
                """====================================
Server already running
Please stop the server and try again
====================================""")
            return

        self.add_log_text("Attempting to start server...")

        self.host = str(self.host_ent.get())
        self.port = self.port_ent.get()

        try:
            self.port = int(self.port)
        except ValueError:
            self.add_log_text("Port isn't valid")
            self.add_log_text("Stoping server start\n======================")
            return

        if self.port < 1023 or self.port > 65535:
            self.add_log_text("Port isn't valid")
            self.add_log_text("Stoping server start\n======================")
            return

        if not self.host:
            self.add_log_text("Host isn't valid")
            self.add_log_text("Stoping server start\n======================")
            return

        self.add_log_text("Sever started successfully")
        self.add_log_text("Waiting for client connection...")
        self.server_alive = True

    def close_server(self):
        '''
        Disconnects the socket connection
        '''

        self.add_log_text("Server closed\n=============")
        self.server_alive = False

    def send_data(self):
        '''
        Sends data to the server
        '''
        if not self.server_alive:
            return

        self.add_log_text(str(self.input_ent.get()))
        self.input_ent.delete(0, tkinter.END)

    def add_log_text(self, msg):
        '''
        Adds the given message to the log output
        '''

        msg = str(msg) + "\n"

        self.log_msg.config(state="normal")
        self.log_msg.insert(tkinter.END, msg)
        self.log_msg.config(state="disabled")


def run():
    '''
    Runs the GUI for testing
    '''
    tkinter_root = tkinter.Tk()

    tkinter_root.title("Chat Room- server")

    ServerGUI(tkinter_root).pack(fill=tkinter.BOTH, expand=True)

    tkinter_root.mainloop()


if __name__ == "__main__":
    run()
