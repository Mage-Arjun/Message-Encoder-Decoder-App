import tkinter as tk
import random
import string

class MessageEncoderDecoder:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Message Encoder/Decoder")#the title of ur application

        self.input_label = tk.Label(self.root, text="Enter your message:")#title of the input box
        self.input_entry = tk.Entry(self.root)#where you can get the message 
        self.encode_button = tk.Button(self.root, text="Encode", command=self.encode_message)#encode button
        self.decode_button = tk.Button(self.root, text="Decode", command=self.decode_message)#decode button
        self.output_text = tk.Text(self.root, height=6, width=40)#text section

       #activation of the butttons
        self.input_label.pack()
        self.input_entry.pack()
        self.encode_button.pack()
        self.decode_button.pack()
        self.output_text.pack()

    def encode_message(self):
        message = self.input_entry.get()#to get user input to ur logic
        words=message.split(" ")
        # Your existing encoding logic here
        nwords=[]
        for word in words:#encoding logic
            if(len(word)>=3):
            # choosing random characters
                r1=''.join(random.choices(string.ascii_letters, k=3)) 
                r2=''.join(random.choices(string.ascii_letters, k=3))
            # combining
                stnew=r1+word[1:]+word[0]+r2
            # adding to nwords
                nwords.append(stnew)
            else:
                nwords.append(word[::-1])
        encoded_message ="ENCODED: "+ " ".join(nwords)
        self.output_text.insert(tk.END, encoded_message + "\n")
        
    def decode_message(self):
        message = self.input_entry.get()
        # Your existing decoding logic here
        words=message.split()
        nwords=[]
    # decoding logic
        for word in words:
            if(len(word)>=3):
            #    removing the random part
                stnew=word[3:-3]
            # recorrecting the first letter part   
                stnew=stnew[-1] + stnew[:-1]
                nwords.append(stnew)
            else:
                nwords.append(word[::-1])
        decoded_message = "DECODED: "+" ".join(nwords)
        self.output_text.insert(tk.END, decoded_message + "\n")
    



    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = MessageEncoderDecoder()
    app.run()


