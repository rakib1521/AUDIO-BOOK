from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import PyPDF2
import pyttsx3
from pyttsx3.drivers import sapi5




def speak(text,speed,voice):
    speak= pyttsx3.init()
    rate = speak.getProperty('rate')
    voices = speak.getProperty('voices')
    speak.setProperty('rate', speed)
    speak.setProperty('voice', voices[voice].id)
    speak.say(text)
    speak.runAndWait()

def pdfread(filename,speed,voice,s_page):
    path = open(filename,'rb')
    pdfreader= PyPDF2.PdfFileReader(path)
    page=pdfreader.numPages


    if s_page>page:
        messagebox.showinfo(title="Error", message="Select an valid Page")

    for i in range(s_page-1,page):

        start= pdfreader.getPage(i)
        text= start.extractText()
        speak(text,speed,voice)


def browseFiles():
    filename = filedialog.askopenfilename(initialdir = "/",
                                          title = "Select PDF",
                                          filetypes = (("PDF",
                                                        "*.pdf*"),
                                                       ("all files",
                                                        "*.*")))



    return filename



def sel_voice():
   selection_voice =  voice.get()
   return selection_voice

def sel_speed():
   selection_speed =  speed.get()
   return selection_speed


def start_read():
    filename=browseFiles()
    if filename=="":
        messagebox.showinfo(title="Error", message="Please Select a PDF")
    else:
        speed=sel_speed()
        voice=sel_voice()
        s_page=s_page_no_input.get()
        if s_page=="":
            s_page=1
        else:
            s_page=s_page_no_input.get()
        #print(filename)
        pdfread(filename,speed,int(voice),int(s_page))

def exit_all():
    window.destroy()

window = Tk()


window.title('AUDIO BOOK')


window.geometry("500x500")


window.config(background = "white")





s_page_no = Label(window, text="starting page no",width=20,font=("bold", 10))
s_page_no.place(x=00,y=40)
s_page_no_input = Entry(window)
s_page_no_input.place(x=240,y=40)


voice_label = Label(window, text="Select Voice",width=20,font=("bold", 10))
voice_label.place(x=00,y=120)
voice = IntVar()
R1 = Radiobutton(window, text="Male Voice", variable=voice, value=0,
                  command=sel_voice)
R1.pack( anchor = W )
R1.place(x=240,y=150)

R2 = Radiobutton(window, text="Female Voice", variable=voice, value=1,
                  command=sel_voice)
R2.pack( anchor = W )
R2.place(x=240,y=180)

e_speed_label = Label(window, text="Select Speed",width=20,font=("bold", 10))
e_speed_label.place(x=00,y=220)

speed = IntVar()
R1 = Radiobutton(window, text="Normal", variable=speed, value=200,
                  command=sel_speed)
R1.pack( anchor = W )
R1.place(x=240,y=250)

R2 = Radiobutton(window, text="Fast", variable=speed, value=300,
                  command=sel_speed)
R2.pack( anchor = W )
R2.place(x=240,y=280)

R3 = Radiobutton(window, text="Super Fast", variable=speed, value=400,
                  command=sel_speed)
R3.pack( anchor = W )
R3.place(x=240,y=310)

button_start = Button(window,
					text = "Start",
					command = start_read)
button_start.place(x=200,y=400)


button_stop = Button(window,
					text = "Stop",
					command = exit_all)
button_stop.place(x=250,y=400)




window.mainloop()
