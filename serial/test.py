# import serial
# import time


# ser = serial.Serial(port="/dev/tty.usbmodem144103", baudrate=115200, bytesize=8, parity='N', stopbits=1)

# for i in range(10):
#     print(ser.readline().decode('utf-8'))
#     time.sleep(0.01)

# ser.close()

# import tkinter as tk

# class MainWindow:
#     def __init__(self, master):
#         self.master = master
#         master.title("Two-Panel GUI")
        
#         self.left_panel = tk.Frame(master, width=200, height=200, bg="red")
#         self.left_panel.pack(side="left", fill="both", expand=True)
        
#         self.right_panel = tk.Frame(master, width=200, height=200, bg="blue")
#         self.right_panel.pack(side="right", fill="both", expand=True)

# root = tk.Tk()
# app = MainWindow(root)
# root.mainloop()

import tkinter as tk

class Console(tk.Text):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.config(state=tk.DISABLED)

    def write(self, message):
        self.config(state=tk.NORMAL)
        self.insert(tk.END, message)
        self.see(tk.END)
        self.config(state=tk.DISABLED)

root = tk.Tk()

console = Console(root, height=10, width=50)
console.pack()

console.write("Hello, world!\n")
console.write("This is a test.\n")

root.mainloop()
