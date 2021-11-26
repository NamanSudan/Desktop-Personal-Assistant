import speech_recognition as sr
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import tkinter.ttk as ttk
from ttkthemes import ThemedStyle
from PIL import Image
import numpy as np
from datetime import datetime
from winsound import PlaySound, SND_FILENAME, SND_ASYNC

root=Tk()

root.title('eDIARY')

root.geometry('250x250')

root.iconbitmap('diary.ico')

today=str(datetime.now())

dt='\t'*5+today

theme= ThemedStyle(root).set_theme('itft1')

style_b = ttk.Style().configure('W.TButton', font=('Helvetica', 10, 'bold'), bd=20, focuscolor=root.cget('background'), background=root.cget('background') )

def light():
    root.config(background='white')
    ThemedStyle(root).set_theme('itft1')

def dark():
    root.config(background='black')
    ThemedStyle(root).set_theme('black')

bgbutton1 = ttk.Radiobutton(root, text='Light', command=lambda: light(), style='W.TButton')

bgbutton2 = ttk.Radiobutton(root, text='Dark', command=lambda: dark(), style='W.TButton')

bgbutton1.grid(row=0, column=1)

bgbutton2.grid(row=1, column=1)

def voice():

    root1 = Toplevel(bg=root.cget('background'))

    root1.title('Voice Assistant')

    root1.iconbitmap('diary.ico')

    label0 = ttk.Label(root1, text='What Shall I Do For You?', justify=LEFT,  style='W.TButton')

    label1 = ttk.Label(root1, text='1) Remember Something For You.', justify=LEFT,  style='W.TButton')

    label2 = ttk.Label(root1, text='2) Show Saved Memories.', justify=LEFT, style='W.TButton')

    label3 = ttk.Label(root1, text='3) Clear Memories', justify=LEFT, style='W.TButton')

    label0.grid(row=0, column=0, sticky=W, ipady=5, pady=10,)

    label1.grid(row=1, column=0, sticky=W, ipady=5, pady=10)

    label2.grid(row=2, column=0, sticky=W, ipady=5, pady=10)

    label3.grid(row=3, column=0, sticky=W, ipady=5, pady=10)

    label= ttk.Label(root1, text='')

    label.grid(row=4, column=1, ipady=5, pady=10)

    PlaySound('command_.wav', SND_FILENAME | SND_ASYNC)

    def tap(event=None):

        global r

        r= sr.Recognizer()

        with sr.Microphone() as source:

             audio = r.listen(source)

             try:

                text = r.recognize_google(audio)

                label.config(text=text)

             except:

                   label.config(text='Voice Not Audible,Speak Again')

        if text=='remember something for me':
            def tap1():

                with sr.Microphone() as source:

                    audio=r.listen(source)

                    try:

                       text1 = r.recognize_google(audio)+dt

                       file = open('eDIARY.txt', 'a')

                       file.write(text1)

                       file.write('\n'*2)

                       label.config(text=text1)

                       file.close()

                       PlaySound('done.wav', SND_FILENAME | SND_ASYNC)

                       button_.config(text="Tap 'Space' to Speak", command=tap)

                    except:

                        label.config(text='Voice Not Audible,Speak Again')

            PlaySound('tap1.wav', SND_FILENAME | SND_ASYNC)

            button_.config(command=tap1, text='Tap To Make Me Remember')

        if text=='show saved memories':

           file = open('eDIARY.txt', 'r')

           memo = file.read()

           label.config(text=memo)

           file.close()

        if text=='clear memories':

           file=open('eDIARY.txt', 'w')

           file.close()

           label.config(text='Data Cleared')

           PlaySound('data cleared.wav', SND_FILENAME | SND_ASYNC)

    button_ = ttk.Button(root1, text="Tap 'Space' to Speak", command=tap, style='W.TButton')

    root1.bind('<space>', tap)

    button_.grid(row=5, column=1, ipady=5, pady=10,)

    def Type(event=None):

            root1_1 = Toplevel()

            root1_1.title('Type...')

            root1_1.geometry('250x100')

            root1_1.iconbitmap('diary.ico')

            entry0 = Entry(root1_1, bd=10)

            def get_entry(event=None):

                text = entry0.get()+dt

                file = open('eDIARY.txt', 'a')

                file.write(text)

                file.write('\n')

                file.close()

                messagebox.showinfo('Saved', 'Successfully written in your eDIARY')

            def Show():

                entry0.config(show='')

                button0.config(command=Hide, text='Hide')

            def Hide():

                entry0.config(show='*')

                button0.config(command=Show, text='Show')

            button0 = ttk.Button(root1_1, text='Hide', command=Hide, style='W.TButton')

            buttonidk = ttk.Button(root1_1, text='Submit', command=get_entry, style='W.TButton')

            root1_1.bind('<Return>', get_entry)

            entry0.grid(row=0, column=0, columnspan=4, sticky='w', ipadx=30)

            button0.grid(row=1, column=3, ipady=5, pady=10,)

            buttonidk.grid(row=1, column=1, ipady=5, pady=10,)

    button00 = ttk.Button(root1, text="Tap To 'Enter' Type It By Yourself", command=Type, style='W.TButton')

    button00.grid(row=6, column=1, ipady=5, pady=10,)

    root1.bind("<Return>", Type)

    root1.mainloop()

def hide():

    root2 = Toplevel(bg=root.cget('background'))

    root2.title('Image Hider')

    root2.geometry('300x200')

    root2.iconbitmap('diary.ico')

    global entry

    entry = Entry(root2, bd=10)

    label = ttk.Label(root2, text='Address of Image:-', style='W.TButton')

    label.grid(row=0, column=0, pady=5)

    entry.grid(row=1, column=0)

    def get(event=None):

        try:

            a = entry.get()

            im = np.asarray(Image.open(a))

            np.save(a, im)

            PlaySound('done.wav', SND_FILENAME | SND_ASYNC)

        except:
            messagebox.showerror('Error', "Enter A Valid Address")

    def get1():

        add = filedialog.askopenfilename(initialdir="\Desktop\eDIARY", title='Select Image To Hide', filetypes=[('All Files', '*.*')])

        entry.insert(0, add)

    button = ttk.Button(root2, text='Enter Address of Image', command=get, style='W.TButton')

    root2.bind('<Return>', get)

    button1 = ttk.Button(root2, text='Browse', command=get1, style='W.TButton')

    button.grid(row=2, column=0, ipady=5, pady=10, padx=10)

    button1.grid(row=2, column=1, ipady=5, pady=10, padx=10)

def load():

    root3 = Toplevel(bg=root.cget('background'))

    root3.title('Image Loader')

    root3.geometry('300x150')

    root3.iconbitmap('diary.ico')

    global entry1

    entry1 = Entry(root3, bd=10)

    entry1.grid(row=0, column=0, pady=10, ipadx=30)

    def get2(event=None):

        try:

            a = entry1.get()

            b = np.load(a)

            img = Image.fromarray(b, 'RGB')

            img.show()

            PlaySound('load.wav', SND_FILENAME | SND_ASYNC)

        except:
            messagebox.showerror('Error', "Enter A Valid Address")

    def get3():

        add1 = filedialog.askopenfilename(initialdir="\Desktop\eDIARY", title='Select Image To Load', filetypes=[('All Files', '*.*')])

        entry1.insert(0, add1)

    button = ttk.Button(root3, text='Enter', command=get2, style='W.TButton')

    root3.bind('<Return>', get2)

    button1 = ttk.Button(root3, text='Browse', command=get3, style='W.TButton')

    button1.grid(row=1, column=1, ipady=5, pady=10,)

    button.grid(row=1, column=0, ipady=5, pady=10,)


button1 = ttk.Button(root, text='Voice Assistant',  command=voice, style='W.TButton')

button2 = ttk.Button(root, text='Hide Image',  command=hide, style='W.TButton')

button3 = ttk.Button(root, text='Load Hidden Image', command=load, style='W.TButton')

button1.grid(row=0, column=0, ipady=5, pady=10, padx=20)

button2.grid(row=1, column=0, ipady=5, pady=10, padx=20)

button3.grid(row=2, column=0, ipady=5, pady=10, padx=20)

root.mainloop()



