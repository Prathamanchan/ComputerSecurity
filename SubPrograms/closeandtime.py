import Tkinter as tk
import tkMessageBox
import time

root = tk.Tk()
start = time.time()

end = time.time()
print "heelo"
if end-start > 5:
	print(end - start)

def on_closing():
    if tkMessageBox.askokcancel("Quit", "Do you want to quit?"):
        root.destroy()

root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()

