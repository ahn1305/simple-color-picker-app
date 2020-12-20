import tkinter as tk ## importing tkinter
from tkinter.colorchooser import askcolor ## importing ask color from color chooser                  


## defining callback function



def callback():
    result = askcolor(color="#6A9662", title = "Ashwin's color picker") ## calling askcolor , and defining color and title 
  
root = tk.Tk() ## storing root window in root
tk.Button(root, text='Choose Color',  fg="darkgreen", command=callback).pack(side=tk.LEFT, padx=10) 
          
tk.Button(text='Quit', command=root.quit,fg="red").pack(side=tk.LEFT, padx=10)
          
tk.mainloop()