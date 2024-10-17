from re import L
from tkinter import *
import datetime
from numpy import imag
import pandas as pd
import webbrowser


from chat import get_response,bot_name,image

BG_GRAY = "#F5F5F1"
BG_COLOR = "#CF352E"
BG="#242526"
TEXT_COLOR = "#F5F5F1"

FONT = "Roboto 14"
FONT_BOLD = "Roboto 15"

class ChatApplication:
    def __init__(self):
        self.window = Tk()
        #helper function
        self._setup_main_window()
    
    def run(self):
        self.window.mainloop() # to start application

    def _setup_main_window(self):
        self.window.title("Chat")
        self.window.resizable(width=False, height=False)
        # to give different attributes
        self.window.configure(width=470, height=550,bg=BG_COLOR)

        # Head label
        head_label = Label(self.window, bg = BG_COLOR, fg = "#242526", text = "What's Your Movie Mood Today?", font = FONT_BOLD, pady = 10)
        head_label.place(relwidth=1)

        # Tiny divider
        line = Label(self.window, width = 450, bg = BG_GRAY)
        line.place(relwidth=1, rely= 0.07, relheight=0.012)

        # Text widget
        self.text_widget = Text(self.window, width = 20, height=2, bg=BG, fg=TEXT_COLOR,
        font = FONT, padx=5, pady=5)

        self.text_widget.place(relheight=0.745, relwidth=1, rely=0.08)
        self.text_widget.configure(cursor="arrow", state=DISABLED)

        #scroll bar
        scrollbar = Scrollbar(self.text_widget)
        scrollbar.place(relheight=1,relx=0.974)
        scrollbar.configure(command=self.text_widget.yview)

        # Bottom label
        bottom_label = Label(self.window, bg=BG_GRAY, height=80)
        bottom_label.place(relwidth=1, rely=0.825)

        # message entry box
        self.msg_entry = Entry(bottom_label, bg=BG, fg=TEXT_COLOR, font=FONT)
        self.msg_entry.place(relwidth=0.74, relheight=0.06, rely=0.008, relx=0.011)
        self.msg_entry.focus()
        self.msg_entry.bind("<Return>", self._on_enter_pressed)
      

        # Button 
        send_button = Button(bottom_label,text = "Send", fg=TEXT_COLOR, 
        font=FONT, width=20, bg=BG, command = lambda: self._on_enter_pressed(None))
        send_button.place(relx=0.77, rely=0.008, relheight=0.06, relwidth=0.22)



    def _on_enter_pressed(self, event):
        msg = self.msg_entry.get()
        
        self._insert_message(msg, "\n You")
        
        

            
            
       
                
        
    def _insert_message(self, msg, sender):
        if not msg:
                return
            
        self.msg_entry.delete(0, END)
        msg1 = f"{sender}: {msg}\n\n"
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END, msg1)
        self.text_widget.configure(state=DISABLED)

        msg2 = f"{bot_name}: {get_response(msg)}\n\n"
        x=image(msg)
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END, msg2)
        def callback(url):
         webbrowser.open_new(url)  



        if x == "Thriller":
         global my_image,m2,m3,m4
         my_image = PhotoImage(file="C:\\Users\\SAFIYA ATEEQ\\Desktop\\Chatbot\\Pictures\\the-call4.gif")
         #self.text_widget.image_create(END,pady =10,padx=10,  image=my_image)
         label1=Label(self.text_widget, image=my_image, cursor = "hand2")
         label1.pack()
         label1.bind("<Button-1>", lambda e: callback("https://www.netflix.com/ae-en/title/81342505"))
         self.text_widget.window_create('end',window=label1)
         
         m2 = PhotoImage(file="C:\\Users\\SAFIYA ATEEQ\\Desktop\\Chatbot\\Pictures\\shuuter.gif")
         label2=Label(self.text_widget, image=m2, cursor = "hand2")
         label2.pack()
         label2.bind("<Button-1>", lambda e: callback("https://www.netflix.com/title/70095139"))
         self.text_widget.window_create('end',window=label2)
         
         m3 = PhotoImage(file="C:\\Users\\SAFIYA ATEEQ\\Desktop\\Chatbot\\Pictures\\parasite.gif")
         label3=Label(self.text_widget, image=m3, cursor = "hand2")
         label3.pack()
         label3.bind("<Button-1>", lambda e: callback("https://w88.bemovies.co/movie/parasite-41796"))
         self.text_widget.window_create('end',window=label3)

         m4 = PhotoImage(file="C:\\Users\\SAFIYA ATEEQ\\Desktop\\Chatbot\\Pictures\\frac.gif")
         label4=Label(self.text_widget, image=m4,cursor = "hand2")
         label4.pack()
         label4.bind("<Button-1>", lambda e: callback("https://www.netflix.com/ae-en/title/80223997"))
         self.text_widget.window_create('end',window=label4)



        if x == "Comedy":
         global m5,m6,m7,m8
         m5 = PhotoImage(file="C:\\Users\\SAFIYA ATEEQ\\Desktop\\Chatbot\\Pictures\\yes.gif")
         label5=Label(self.text_widget, image=m5, cursor = "hand2")
         label5.pack()
         label5.bind("<Button-1>", lambda e: callback("https://www.netflix.com/ae-en/title/80223997"))
         self.text_widget.window_create('end',window=label5)

         m6 = PhotoImage(file="C:\\Users\\SAFIYA ATEEQ\\Desktop\\Chatbot\\Pictures\\game.gif")
         label6=Label(self.text_widget, image=m6, cursor = "hand2")
         label6.pack()
         label6.bind("<Button-1>", lambda e: callback("https://www.netflix.com/ae-en/title/80201565"))
         self.text_widget.window_create('end',window=label6)

         m7 = PhotoImage(file="C:\\Users\\SAFIYA ATEEQ\\Desktop\\Chatbot\\Pictures\\kung.gif")
         label7=Label(self.text_widget, image=m7, cursor = "hand2")
         label7.pack()
         label7.bind("<Button-1>", lambda e: callback("https://www.netflix.com/ae-en/title/70075480"))
         self.text_widget.window_create('end',window=label7)

         m8 = PhotoImage(file="C:\\Users\\SAFIYA ATEEQ\\Desktop\\Chatbot\\Pictures\\wel.gif")
         label8=Label(self.text_widget, image=m8, cursor = "hand2")
         label8.pack()
         label8.bind("<Button-1>", lambda e: callback("https://www.netflix.com/ae-en/title/70091146"))
         self.text_widget.window_create('end',window=label8)



        if x == "Horror":
         global m9,m10,m11,m12
         m9 = PhotoImage(file="C:\\Users\\SAFIYA ATEEQ\\Desktop\\Chatbot\\Pictures\\orp.gif")
         label9=Label(self.text_widget, image=m9, cursor = "hand2")
         label9.pack()
         label9.bind("<Button-1>", lambda e: callback("https://www.netflix.com/ae-en/title/70113004"))
         self.text_widget.window_create('end',window=label9)

         m10 = PhotoImage(file="C:\\Users\\SAFIYA ATEEQ\\Desktop\\Chatbot\\Pictures\\conj.gif")
         label10=Label(self.text_widget, image=m10, cursor = "hand2")
         label10.pack()
         label10.bind("<Button-1>", lambda e: callback("https://www.netflix.com/ae-en/title/70251894"))
         self.text_widget.window_create('end',window=label10)

         m11 = PhotoImage(file="C:\\Users\\SAFIYA ATEEQ\\Desktop\\Chatbot\\Pictures\\hush.gif")
         label11=Label(self.text_widget, image=m11, cursor = "hand2")
         label11.pack()
         label11.bind("<Button-1>", lambda e: callback("https://www.netflix.com/ae-en/title/800918794"))
         self.text_widget.window_create('end',window=label11)

         m12 = PhotoImage(file="C:\\Users\\SAFIYA ATEEQ\\Desktop\\Chatbot\\Pictures\\spl.gif")
         label12=Label(self.text_widget, image=m12, cursor = "hand2")
         label12.pack()
         label12.bind("<Button-1>", lambda e: callback("https://w88.bemovies.co/movie/split-19806"))
         self.text_widget.window_create('end',window=label12)



        if x == "Romance":
         global m13,m14,m15,m26,m27
         m13 = PhotoImage(file="C:\\Users\\SAFIYA ATEEQ\\Desktop\\Chatbot\\Pictures\\me.gif")
         label13=Label(self.text_widget, image=m13, cursor = "hand2")
         label13.pack()
         label13.bind("<Button-1>", lambda e: callback("https://www.netflix.com/ae-en/title/80043744"))
         self.text_widget.window_create('end',window=label13)

         m14 = PhotoImage(file="C:\\Users\\SAFIYA ATEEQ\\Desktop\\Chatbot\\Pictures\\bef.gif")
         label14=Label(self.text_widget, image=m14, cursor = "hand2")
         label14.pack()
         label14.bind("<Button-1>", lambda e: callback("https://w88.bemovies.co/movie/before-sunrise-17659"))
         self.text_widget.window_create('end',window=label14)

         m15 = PhotoImage(file="C:\\Users\\SAFIYA ATEEQ\\Desktop\\Chatbot\\Pictures\\abt.gif")
         label15=Label(self.text_widget, image=m15, cursor = "hand2")
         label15.pack()
         label15.bind("<Button-1>", lambda e: callback("https://w88.bemovies.co/movie/about-time-19112"))
         self.text_widget.window_create('end',window=label15)

         m26 = PhotoImage(file="C:\\Users\\SAFIYA ATEEQ\\Desktop\\Chatbot\\Pictures\\la.gif")
         label16=Label(self.text_widget, image=m26, cursor = "hand2")
         label16.pack()
         label16.bind("<Button-1>", lambda e: callback("https://w88.bemovies.co/movie/la-la-land-19613"))
         self.text_widget.window_create('end',window=label16)

         m27 = PhotoImage(file="C:\\Users\\SAFIYA ATEEQ\\Desktop\\Chatbot\\Pictures\\cl.gif")
         label17=Label(self.text_widget, image=m27, cursor = "hand2")
         label17.pack()
         label17.bind("<Button-1>", lambda e: callback("https://w88.bemovies.co/movie/clouds-63841"))
         self.text_widget.window_create('end',window=label17)




        if x == "Action":
         global m16,m17,m18,m32
         m32 = PhotoImage(file="C:\\Users\\SAFIYA ATEEQ\\Desktop\\Chatbot\\Pictures\\kin.gif")
         label18=Label(self.text_widget, image=m32, cursor = "hand2")
         label18.pack()
         label18.bind("<Button-1>", lambda e: callback("https://w88.bemovies.co/movie/kingsman-the-secret-service-19542"))
         self.text_widget.window_create('end',window=label18)

         m16 = PhotoImage(file="C:\\Users\\SAFIYA ATEEQ\\Desktop\\Chatbot\\Pictures\\ext.gif")
         label19=Label(self.text_widget, image=m16, cursor = "hand2")
         label19.pack()
         label19.bind("<Button-1>", lambda e: callback("https://www.netflix.com/ae-en/title/80230399"))
         self.text_widget.window_create('end',window=label19)

         m17 = PhotoImage(file="C:\\Users\\SAFIYA ATEEQ\\Desktop\\Chatbot\\Pictures\\13.gif")
         label20=Label(self.text_widget, image=m17, cursor = "hand2")
         label20.pack()
         label20.bind("<Button-1>", lambda e: callback("https://w88.bemovies.co/movie/13-hours-the-secret-soldiers-of-benghazi-18842"))
         self.text_widget.window_create('end',window=label20)

         m18 = PhotoImage(file="C:\\Users\\SAFIYA ATEEQ\\Desktop\\Chatbot\\Pictures\\old.gif")
         label21=Label(self.text_widget, image=m18, cursor = "hand2")
         label21.pack()
         label21.bind("<Button-1>", lambda e: callback("https://www.netflix.com/ae-en/title/81038963"))
         self.text_widget.window_create('end',window=label21)



        '''if x == "Sci-fi":

         m18 = PhotoImage(file="C:\\Users\\SAFIYA ATEEQ\\Pictures\\inc(1).gif")
         label2=Label(self.text_widget, image=m18, cursor = "hand2")
         label2.pack()
         label2.bind("<Button-1>", lambda e: callback("https://www.netflix.com/ae-en/title/70131314"))
         self.text_widget.window_create('end',window=label2)'''



            

        if x == "Animation":
         global m28,m19,m20,m21
         m28 = PhotoImage(file="C:\\Users\\SAFIYA ATEEQ\\Desktop\\Chatbot\\Pictures\\how.gif")
         label22=Label(self.text_widget, image=m28, cursor = "hand2")
         label22.pack()
         label22.bind("<Button-1>", lambda e: callback("https://www.netflix.com/ae-en/title/70109893"))
         self.text_widget.window_create('end',window=label22)

         m19 = PhotoImage(file="C:\\Users\\SAFIYA ATEEQ\\Desktop\\Chatbot\\Pictures\\kung.gif")
         label23=Label(self.text_widget, image=m19, cursor = "hand2")
         label23.pack()
         label23.bind("<Button-1>", lambda e: callback("https://www.netflix.com/ae-en/title/70075480"))
         self.text_widget.window_create('end',window=label23)

         m20 = PhotoImage(file="C:\\Users\\SAFIYA ATEEQ\\Desktop\\Chatbot\\Pictures\\luca.gif")
         label24=Label(self.text_widget, image=m20, cursor = "hand2")
         label24.pack()
         label24.bind("<Button-1>", lambda e: callback("https://w88.bemovies.co/movie/luca-70342"))
         self.text_widget.window_create('end',window=label24)

         m21 = PhotoImage(file="C:\\Users\\SAFIYA ATEEQ\\Desktop\\Chatbot\\Pictures\\in.gif")
         label25=Label(self.text_widget, image=m21, cursor = "hand2")
         label25.pack()
         label25.bind("<Button-1>", lambda e: callback("https://w88.bemovies.co/movie/inside-out-19725"))
         self.text_widget.window_create('end',window=label25)

        if x == "Fantasy":
         global m22,m23,m29
         m22 = PhotoImage(file="C:\\Users\\SAFIYA ATEEQ\\Desktop\\Chatbot\\Pictures\\mon.gif")
         label26=Label(self.text_widget, image=m22, cursor = "hand2")
         label26.pack()
         label26.bind("<Button-1>", lambda e: callback("https://www.netflix.com/title/80022607"))
         self.text_widget.window_create('end',window=label26)

         m29 = PhotoImage(file="C:\\Users\\SAFIYA ATEEQ\\Desktop\\Chatbot\\Pictures\\sp.gif")
         label27=Label(self.text_widget, image=m29, cursor = "hand2")
         label27.pack()
         label27.bind("<Button-1>", lambda e: callback("https://www.netflix.com/ae-en/title/60023642"))
         self.text_widget.window_create('end',window=label27)

         m23 = PhotoImage(file="C:\\Users\\SAFIYA ATEEQ\\Desktop\\Chatbot\\Pictures\\lo.gif")
         label28=Label(self.text_widget, image=m23, cursor = "hand2")
         label28.pack()
         label28.bind("<Button-1>", lambda e: callback("https://www.netflix.com/se-en/title/60004484"))
         self.text_widget.window_create('end',window=label28)

        if x =="New":
         global m24,my_image2,m31,m30
         m24 = PhotoImage(file="C:\\Users\\SAFIYA ATEEQ\\Desktop\\Chatbot\\Pictures\\pen.gif")
         label29=Label(self.text_widget, image=m24, cursor = "hand2")
         label29.pack()
         label29.bind("<Button-1>", lambda e: callback("https://www.netflix.com/ae-en/title/81350434"))
         self.text_widget.window_create('end',window=label29)

         my_image2 = PhotoImage(file="C:\\Users\\SAFIYA ATEEQ\\Desktop\\Chatbot\\Pictures\\the-call4.gif")
         label30=Label(self.text_widget, image=my_image2, cursor = "hand2")
         label30.pack()
         label30.bind("<Button-1>", lambda e: callback("https://www.netflix.com/ae-en/title/81342505"))
         self.text_widget.window_create('end',window=label30)

         m31 = PhotoImage(file="C:\\Users\\SAFIYA ATEEQ\\Desktop\\Chatbot\\Pictures\\yes.gif")
         label31=Label(self.text_widget, image=m31, cursor = "hand2")
         label31.pack()
         label31.bind("<Button-1>", lambda e: callback("https://www.netflix.com/ae-en/title/80223997"))
         self.text_widget.window_create('end',window=label31)

         m30 = PhotoImage(file="C:\\Users\\SAFIYA ATEEQ\\Desktop\\Chatbot\\Pictures\\cl.gif")
         label32=Label(self.text_widget, image=m30, cursor = "hand2")
         label32.pack()
         label32.bind("<Button-1>", lambda e: callback("https://w88.bemovies.co/movie/clouds-63841"))
         self.text_widget.window_create('end',window=label32)











        self.text_widget.configure(state=DISABLED)
        
        
        
    


        self.text_widget.see(END)

    

   

   



            


if __name__ == "__main__":
    app = ChatApplication()
    app.run()




    



