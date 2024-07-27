from selenium import webdriver 
from PIL import Image
import tkinter as tk
from tkinter import ttk, filedialog
import os
import shutil

def openfile():
    file.set(filedialog.askopenfilename())

def openoutputdir():
    out.set(filedialog.askdirectory())

def submit():
    match(driver.get()):
        case 'Firefox':
            drv = webdriver.Firefox()
        case 'Chrome':
            drv = webdriver.Chrome()
    drv.maximize_window()
    drv.get(f'file:///{file.get()}')
    n_frames = int(fr.get())*int(duration.get())
    os.makedirs('out')
    for i in range(n_frames):
        drv.get_screenshot_as_file(f'./out/{i}.png')
    img = Image.open('./out/0.png')
    img.save('animation.gif', append_images=[Image.open(f'./out/{i}.png') for i in range(1, n_frames)], save_all=True, 
    duration= 1000/int(fr.get()))
    shutil.rmtree('out')
    drv.close()

root = tk.Tk()
root.title("Web2GIF")

#Standard aspect ratio 16:9
window = ttk.Frame(root, width=1024, height=576, padding="10 10 10 10")
window.grid_propagate(0)
window.grid(column=0, row=0, sticky=(tk.N,tk.W,tk.E,tk.S))
file = tk.StringVar()
filelabel = ttk.Label(window, text="Select Browser animation file:").grid(column=0, row=1, sticky=(tk.E, tk.W))
fileentry = ttk.Entry(window, textvariable=file, width=75).grid(column=0, row=2, columnspan=3, pady=30, sticky=tk.W)
filebutton = ttk.Button(window, text="Browse", command=openfile).grid(column=3, row=2, padx=10, pady=30, sticky=tk.W)
driver = tk.StringVar(value='Chrome')
driverlabel = ttk.Label(window, text="Web Driver to use:").grid(column=0, row=3, sticky=(tk.E, tk.W))
drivercombo = ttk.Combobox(window, values=['Firefox', 'Chrome'], state="readonly", textvariable=driver).grid(column=0, pady=30, row=4, sticky=(tk.W, tk.E))
fr = tk.StringVar(value='24')
frlabel = ttk.Label(window, text="Frame Rate (in FPS):").grid(column=0, row=5, sticky=(tk.E, tk.W))
frentry = ttk.Entry(window, textvariable=fr).grid(column=0, row=6, sticky=tk.W, pady=30)
duration = tk.StringVar(value='6')
durationlabel = ttk.Label(window, text="Animation Duration:").grid(column=0, row=7, sticky=(tk.E, tk.W))
durationentry = ttk.Entry(window, textvariable=duration).grid(column=0, row=8, sticky=tk.W, pady=30)
out = tk.StringVar()
outlabel = ttk.Label(window, text="Select Output directory:").grid(column=0, row=9, sticky=(tk.E, tk.W))
outentry = ttk.Entry(window, textvariable=out, width=75).grid(column=0, row=10, columnspan=3, pady=30, sticky=tk.W)
outbutton = ttk.Button(window, text="Browse", command=openoutputdir).grid(column=3, row=10, padx=10, pady=30, sticky=tk.W)
submit = ttk.Button(window, text="Create GIF", command=submit).grid(column=1, row=11, sticky=tk.W)
root.mainloop()








