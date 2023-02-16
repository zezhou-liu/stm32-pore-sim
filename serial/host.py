import tkinter as tk
from tkinter import ttk
import threading
import serial
import time
class SerialPortConfig:
    def __init__(self, root):
        self.root = root
        self.root.title("Serial Port Configuration")

        self.port_var = tk.StringVar(value="/dev/tty.usbmodem142103")
        self.baud_var = tk.StringVar(value="9600")
        self.data_len_var = tk.StringVar(value="8")
        self.parity_var = tk.StringVar(value="None")
        self.stop_bits_var = tk.StringVar(value="1")

        port_label = tk.Label(self.root, text="Port:")
        port_label.grid(row=0, column=0, padx=5, pady=5, sticky="W")

        self.port_entry = tk.Entry(self.root, textvariable=self.port_var)
        self.port_entry.grid(row=0, column=1, padx=5, pady=5)

        baud_label = tk.Label(self.root, text="Baud rate:")
        baud_label.grid(row=1, column=0, padx=5, pady=5, sticky="W")

        self.baud_combo = ttk.Combobox(self.root, textvariable=self.baud_var, values=[9600, 19200, 38400, 57600, 115200])
        self.baud_combo.grid(row=1, column=1, padx=5, pady=5)

        data_len_label = tk.Label(self.root, text="Data length:")
        data_len_label.grid(row=2, column=0, padx=5, pady=5, sticky="W")

        self.data_len_combo = ttk.Combobox(self.root, textvariable=self.data_len_var, values=[1,2,3,4,5, 6, 7, 8])
        self.data_len_combo.grid(row=2, column=1, padx=5, pady=5)

        parity_label = tk.Label(self.root, text="Parity:")
        parity_label.grid(row=3, column=0, padx=5, pady=5, sticky="W")

        self.parity_combo = ttk.Combobox(self.root, textvariable=self.parity_var, values=["None", "Odd", "Even"])
        self.parity_combo.grid(row=3, column=1, padx=5, pady=5)

        stop_bits_label = tk.Label(self.root, text="Stop bits:")
        stop_bits_label.grid(row=4, column=0, padx=5, pady=5, sticky="W")

        self.stop_bits_combo = ttk.Combobox(self.root, textvariable=self.stop_bits_var, values=[1, 2])
        self.stop_bits_combo.grid(row=4, column=1, padx=5, pady=5)

        connect_button = tk.Button(self.root, text="Connect", command=self.connect)
        connect_button.grid(row=5, column=0, padx=5, pady=5, sticky="W")
        
        receive_button = tk.Button(self.root, text="Receive", command=self._receive_data_thread)
        receive_button.grid(row=5, column=1, padx=5, pady=5, sticky="W")

        cancel_button = tk.Button(self.root, text="Cancel", command=self.cancel)
        cancel_button.grid(row=5, column=2, padx=5, pady=5, sticky="E")

    def connect(self):
        port = self.port_var.get()
        baud = int(self.baud_var.get())
        data_len = int(self.data_len_var.get())

        if self.parity_var.get() == "None":
            parity = serial.PARITY_NONE
        elif self.parity_var.get() == "Even":
            parity = serial.PARITY_EVEN
        elif self.parity_var.get() == "Odd":
            parity = serial.PARITY_ODD
        stop_bits = float(self.stop_bits_var.get())

        try:
            self.ser = serial.Serial(port=port, baudrate=baud, bytesize=data_len, parity=parity, stopbits=stop_bits)
            print("Port is opened.")
        except Exception as e:
            print("Port can't be opened:", e)
    
    def _receive_data_thread(self):
        threading.Thread(target=self.receive_data).start()
    
    def receive_data(self):
        # create a new window for displaying the received data
        self.receive_window = tk.Toplevel(self.root)
        self.receive_window.title("Received Data")
        self.receive_window.geometry("400x300")

        # create a text box widget in the new window to display the received data
        self.receive_text = tk.Text(self.receive_window)
        self.receive_text.pack(fill="both", expand=True)
        
        self.receive_window.protocol("WM_DELETE_WINDOW", self.close_port)
        # start the serial connection
        self.connect()

        # start receiving and displaying the serial data
        while True:
            data = self.ser.readline().decode('utf-8')
            self.receive_text.insert("end", data)
            self.receive_text.see("end")
    
    def close_port(self):
        self.ser.close()
        self.receive_window.destroy()
        
    def cancel(self):

        self.root.quit()
        
        
    
if __name__ == "__main__":
    root = tk.Tk()
    app = SerialPortConfig(root)
    root.mainloop()

