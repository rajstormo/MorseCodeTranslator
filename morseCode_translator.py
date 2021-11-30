from tkinter import *

morse_code = {     
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-',
    'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
    '9': '----.', '0': '-----', ',': '--..--', '.': '.-.-.-', '?': '..--..', '/': '-..-.', '-': '-....-',
    '(': '-.--.', ')': '-.--.-', ';': '-.-.-.', ':': '---...', '+': '.-.-.', '=': '-...-', '!': '-.-.--'
}

class MorseCodeTranslator:
    def __init__(self,root):

        # Label for heading
        self.heading_label = Label(root,text="MORSE CODE TRANSLATOR",font=("Castellar",25,"bold"),pady=15)
        self.heading_label.pack()

        # Frame for mode selection
        self.mode_frame = Frame(root,padx=15)
        self.mode_frame.pack(anchor=W)

        self.mode_label = Label(self.mode_frame,text="Mode :")
        self.mode_label.grid(row=0,column=0)

        self.value_chosen = IntVar()
        self.convertTo_morse = Radiobutton(self.mode_frame,text="Text to Morse code",variable=self.value_chosen,value=1,command=self.HideInstruction)
        self.convertTo_morse.grid(row=0,column=1)

        self.convertTo_text = Radiobutton(self.mode_frame,text="Morse code to Text",variable=self.value_chosen,value=2,padx=10,command=self.DisplayInstruction)
        self.convertTo_text.grid(row=0,column=2)
        
        #instruction label
        self.instruction_label_1 = Label(self.mode_frame,text="            1.  Enter space separated morse code",fg="red")
        self.instruction_label_2 = Label(self.mode_frame,text="2.  Use '/' to give a whitespace",fg="red")
        self.instruction_label_3 = Label(self.mode_frame,text = " '/' represents whitespace", fg="red")

        # frame where the conversion will take place
        self.main_frame = Frame(root,pady=10,padx=20)
        self.main_frame.pack(fill=X)

        # text widget
        self.text_entry = Text(self.main_frame,height=5,width=64,relief=RIDGE,bd=2,fg="white",bg="#232121",wrap=WORD,font=("Consolas",14),selectbackground="orange",insertbackground="white",spacing2=5,spacing1=5)

        self.text_entry.insert(1.0,"Enter Text here...")
        self.text_entry.focus()
        self.text_entry.grid(row=0,column=0)

        # calling ScrollBar method to create scrollbar
        self.ScrollBar(self.main_frame,self.text_entry)
       
        # Buttons : convert and clear text buttons
        self.convert_button = Button(self.main_frame,text="Convert",width=20,bg="green",fg="white",command=self.Convert)
        self.convert_button.grid(row=1,column=0,sticky=W,ipady=5,pady=10)

        self.clear_button = Button(self.main_frame,text="Clear Text",width=15,bg="red",fg="white",command=self.ClearText)
        self.clear_button.grid(row=1,column=0,ipady=5)

        # Result frame: frame where result will be shown
        self.result_frame = Frame(root,padx=20)
        self.result_frame.pack(fill=X)

        self.result_text = Text(self.result_frame,height=5,width=64,relief=RIDGE,bd=2,fg="white",bg="#232121",wrap=WORD,font=("Consolas",14),selectbackground="orange",insertbackground="white",spacing2=5,spacing1=5)
        self.result_text.insert('1.0',"Result will be shown here")
        self.result_text.grid(row=0,column=0)
        self.result_text['state'] = DISABLED

        # scrollbar for result frame 
        self.ScrollBar(self.result_frame,self.result_text)
        
    def ScrollBar(self,frame,screen):
        scroll = Scrollbar(frame,orient=VERTICAL,command=screen.yview)
        scroll.grid(row=0,column=1,sticky=NS)
        screen["yscrollcommand"] = scroll.set 

    def ClearText(self):
        self.text_entry.delete(1.0,END)
    
    def DisplayInstruction(self):
        self.instruction_label_1.grid(row=2,column=0,columnspan=3)
        self.instruction_label_2.grid(row=3,column=0,columnspan=3)
        self.instruction_label_3.grid_remove()

    def HideInstruction(self):
        self.instruction_label_3.grid(row=2,column=0,columnspan=2)
        self.instruction_label_1.grid_remove()
        self.instruction_label_2.grid_remove()

    def Convert(self):
        input_string = self.text_entry.get(1.0,END).upper()
        # print(input_string)
        chosen_value = self.value_chosen.get()
        result = " "
        if(chosen_value == 1):
            for i in input_string:
                if(i == " "):
                    result += " / "
                for j in morse_code:
                    if i == j:
                        result += morse_code[j] + " "     
                          
        elif(chosen_value == 2):
            #returns list of words in the string(splits word by whitespace by default)
            input_string_list = input_string.split()
            result = ""
            for i in input_string_list:
                if(i == "/"):
                    result += " "
                for key in morse_code:
                    if(i == morse_code[key]):
                        result += key

        else:
            result = "No option chosen"
            self.result_text['fg'] = "orange"


        self.result_text['state'] = NORMAL
        self.result_text.delete(1.0,END)   # deleting previous result
        self.result_text.insert(1.0,result) # inserting latest result
        self.result_text['state'] = DISABLED # disabling the result_text widget
        

root = Tk()
root.geometry("700x520")
root.resizable(False,False)
root.title("Morse Code Translator")

obj = MorseCodeTranslator(root)

root.mainloop()
