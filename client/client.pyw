'''
Creates the client GUI and processes the requests
'''
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


class ClientGUI(tkinter.Frame):  # pylint: disable=too-many-ancestors
    '''
    Loads all of the GUI sections and contains their methods
    '''

    def __init__(self, root):
        '''
        Loads the GUI sections
        '''

        self.root = root

        super().__init__(self.root)

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

        # Server frame
        self.server_fr = tkinter.Frame(self.info_fr)
        self.server_fr.pack(fill=tkinter.X, expand=True)

        # Server label
        tkinter.Label(self.server_fr, text="Server:").pack(
            fill=tkinter.X, side=tkinter.LEFT, expand=True)

        # Server entry
        self.server_ent = tkinter.Entry(self.server_fr)
        self.server_ent.pack(
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

        # name frame
        self.name_fr = tkinter.Frame(self.info_fr)
        self.name_fr.pack(fill=tkinter.X, expand=True)

        # name label
        tkinter.Label(self.name_fr, text="Name:").pack(
            fill=tkinter.X, side=tkinter.LEFT, expand=True)

        # name entry
        self.name_ent = tkinter.Entry(self.name_fr)
        self.name_ent.pack(fill=tkinter.X,
                           side=tkinter.RIGHT, expand=True, padx=3, pady=3)

        Spacer(self.info_fr).pack(fill=tkinter.X, expand=True)

        tkinter.Button(self.info_fr, text="Connect", command=lambda: self.connect()).pack(
            fill=tkinter.X, expand=True)

    def set_log_fr(self):
        '''
        Sets the widgets in the log frame section for server O/I
        '''

        self.log_msg = ScrolledText(self.log_fr, state="disabled")
        self.log_msg.pack(fill=tkinter.BOTH, expand=True, padx=3, pady=3)

        self.add_log_text("Waiting to connect...")

        self.input_fr = tkinter.Frame(self.log_fr)
        self.input_fr.pack(fill=tkinter.BOTH, expand=True, padx=2, pady=2)

        self.input_ent = tkinter.Entry(self.input_fr)
        self.input_ent.pack(fill=tkinter.BOTH,
                            side=tkinter.LEFT, expand=True, padx=3, pady=3)

        # Send button
        tkinter.Button(self.input_fr, text="send", command=self.send_data()).pack(
            fill=tkinter.BOTH, side=tkinter.LEFT, expand=True, padx=3, pady=3)

        # Disconnect button
        tkinter.Button(self.input_fr, text="disconnect", command=self.disconnect()).pack(
            fill=tkinter.BOTH, side=tkinter.LEFT, expand=True, padx=3, pady=3)

    def connect(self):
        '''
        Opens the socket connection
        '''

        return

    def disconnect(self):
        '''
        Disconnects the socket connection
        '''

        return

    def send_data(self):
        '''
        Sends data to the server
        '''

        return

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

    tkinter_root.title("Chat Room- client")

    ClientGUI(tkinter_root).pack(fill=tkinter.BOTH, expand=True)

    tkinter_root.mainloop()


if __name__ == "__main__":
    run()
