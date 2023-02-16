# import serial
# import time


# ser = serial.Serial(port="/dev/tty.usbmodem144103", baudrate=115200, bytesize=8, parity='N', stopbits=1)

# for i in range(10):
#     print(ser.readline().decode('utf-8'))
#     time.sleep(0.01)

# ser.close()

import tkinter as tk

class MainWindow:
    def __init__(self, master):
        self.master = master
        master.title("Two-Panel GUI")
        
        self.left_panel = tk.Frame(master, width=200, height=200, bg="red")
        self.left_panel.pack(side="left", fill="both", expand=True)
        
        self.right_panel = tk.Frame(master, width=200, height=200, bg="blue")
        self.right_panel.pack(side="right", fill="both", expand=True)

root = tk.Tk()
app = MainWindow(root)
root.mainloop()
