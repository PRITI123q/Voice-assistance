import webbrowser
import pyttsx3
import speech_recognition as sr
import re
import wikipedia
import os
import random
import tkinter as tk
from tkinter import Tk
from tkinter import *
import ctypes
from tkinter import _tkinter
import PIL
from PIL import ImageTk
from PIL import Image

engine=pyttsx3.init('sapi5')
window=Tk()


window.configure(bg="black")
SET_WIDTH=2500
SET_HEIGHT=1900

def main():
    
    bgImg=Image.open("ty1.jpg")
    window.title("Assistant")
    canvas=tk.Canvas(window,width=SET_WIDTH,height=SET_HEIGHT)
    canvas.pack()
   
    image=ImageTk.PhotoImage(bgImg)
 
    canvas.create_image(650,300,image=image)     

    label=Label(canvas,image=image)
    label.image=image

    label.pack()
    
    
    btn=tk.Button(canvas,text="CLICK ME",bg="black",fg="white",command=command1)
    
    
    #canvas.create_window()
    
    btn.place(relx=1,rely=1,relwidth=50,relheight=30)
    
    
    
    btn_window=canvas.create_window(700,500,window=btn)
    
    E1=Entry(window,bd=5,show='*')
    E1.pack(side=TOP)  


def wishme():
    

    pyttsx3.speak("hello i am your assistant i am here to perform various tasks for you  please tell me how i can help you")

def take_cmd():
    
    r=sr.Recognizer()
    with sr.Microphone() as source:
        pyttsx3.speak("what can i do for you")
        print("Please tell me your requirements")
        
        audio=r.listen(source)
    try:
        print("Recognizing..")
       
        text=r.recognize_google(audio,language='en-in').lower()
        
        
        pyttsx3.speak("Please wait while opening")
        return text
    except Exception as e:
        print(e)

        print("couldn't recognize ,say that again plz")
        return "none"  
        
def command1():
    while True:
          

          text=take_cmd()
          
          if("start" in text) or ("webserver" in text) and ("apache" in text) or ("httpd" in text):
             webbrowser.open("http://192.168.42.244/cgi-bin/home.py?c=systemctl%20start%20httpd")
             pyttsx3.speak("apache webserver is running")
             break
          if("status" in text) or ("webserver" in text) and ("apache" in text) or ("httpd" in text):
             webbrowser.open("http://192.168.42.244/cgi-bin/home.py?c=systemctl%20status%20httpd")
             pyttsx3.speak("Here is your status of apache webserver")
             break
          elif (("run" in text) or ("launch" in text)) and (("docker" in text) or ("container" in text)):
             pyttsx3.speak("opening  web page to launch docker ")             
             webbrowser.open("http://192.168.42.244/login.html")
             break
             
          elif (("run" in text) or ("launch" in text) and ("Linux" in text) or ("commands" in text)):
             pyttsx3.speak("opening a page to run linux command ")
             webbrowser.open("http://192.168.42.244/login.html")
             break
          elif 'open google' in text:
            pyttsx3.speak("opening google")
            webbrowser.open("google.com")
            break
          elif 'open youtube' in text:
              webbrowser.open("youtube.com")
              pyttsx3.speak("opening you tube")
              break
          elif 'wikipedia' in text:
            pyttsx3.speak("searching wikipedia....")
            text=text.replace("wikipedia","")
            results=wikipedia.summary(text,sentences=2)
            pyttsx3.speak("according to wikipedia")
            print(results)
            pyttsx3.speak(results)
            break
          
  
          
          else:
            print("sorry")
            break
if __name__=="__main__":
    wishme()
    main()


window.mainloop()
