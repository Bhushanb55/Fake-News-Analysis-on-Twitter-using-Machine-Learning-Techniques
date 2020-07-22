# -*- coding: utf-8 -*-
"""

@author: BHUSHAN

"""

import pickle


from tkinter import *
from tkinter import ttk





#doc_new = ['obama is running for president in 2016']

def Statment():    
   var =input("Please enter the news text you want to verify: ")
   print("You entered: " + str(var))


#function to run for prediction
def detecting_fake_news(var):    
#retrieving the best model for prediction call
    load_model = pickle.load(open('final_model.sav', 'rb'))
    prediction = load_model.predict([var])
    prob = load_model.predict_proba([var])

    return (print("The given statement is ",prediction[0])
            ,print("The truth probability score is ",prob[0][1]))
    
    
def result(var):
    
    var = str(var)
    global statments
    if(prediction==True):
        statments.set("True")
    else:
        statments.set("False")
        
        
        global results
        if(prediction==True):
            results.set("The given news is Real")
        else:
            results.set("The given news is Fake")
             
                  
    
        
    
            
        
        

        






root = Tk()
root.title("Fake News Detector")  
  
Statment = StringVar()
statments = StringVar()
results = StringVar()
prediction = StringVar()
var = StringVar()


mainframe = ttk.Frame(root, padding="50 50 70 70")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)




ttk.Label(mainframe, text="FAKE NEWS DETECTOR").grid(column=1, row=0, sticky=(N, S))

ttk.Label(mainframe, text="Please enter the news text you want to verify ").grid(column=0, row=4, sticky=W)
ttk.Label(mainframe, textvariable=Statment).grid(column=1, row=4, sticky=(W, E))
word_entry = ttk.Entry(mainframe, width=65, textvariable=var)
word_entry.grid(column=1, row=4, sticky=(W, E))


ttk.Label(mainframe, text="The given statement is ").grid(column=0, row=6, sticky=W)
ttk.Label(mainframe, textvariable=statments).grid(column=1, row=6, sticky=(W, E))


ttk.Label(mainframe, text="Result :").grid(column=0, row=8, sticky=W)
ttk.Label(mainframe, textvariable=results).grid(column=1, row=8, sticky=(W, E))


ttk.Button(mainframe, text="Run", command=lambda: result(var.get())).grid(column=3, row=10, sticky=W)




for child in mainframe.winfo_children():
    child.grid_configure(padx=15, pady=15)
    
root.mainloop()
    


if __name__ == '__main__':
    detecting_fake_news(var)
    
