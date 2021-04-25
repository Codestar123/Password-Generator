from tkinter import *
import tkinter.messagebox
import random 
import string

'''This is an app made for generating a self.random strong password'''
class Password():
    def __init__(self,w):
        self.specials = ['!','@','#','$','%','^','&','*','(',')','?','<','>',',','.','|','-','=','+','_',':',';','.',',','<','>','{','}','[',']','`','~']
        self.ints = string.digits
        self.letters = string.ascii_letters

        self.password = []
        characters_left = random.choice(range(7,13))

        while characters_left:
            self.password.append(self.generate())
            characters_left -= 1
            
        s = ''
        self.password = s.join(self.password)
        tkinter.messagebox.showinfo('Password',self.password)



        
    def generate(self):
        return random.choice(random.choice((self.specials,self.ints,self.letters)))
                                                             
        
            

    

class Window:
    def __init__(self):

        self.tk = Tk()
        self.tk.title('Generate your password')
        self.tk.resizable(0,0)
        self.tk.wm_attributes('-topmost',1)
        self.tk.geometry('400x500')
        self.tk.configure(bg = 'yellow')
        
        self.generate_button = Button(self.tk, text = "Generate", command = lambda : p(self), font = (None,20), bg = 'blue', fg = 'white').place(x = 130, y = 160)

p = Password
w = Window()
w.tk.mainloop()
