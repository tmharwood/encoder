# Author: Tyler Harwood
# Class: CS361
# Description: Encoder! This will let the user pick an encoding method and encode plaintext

from tkinter import *
from tkinter import ttk
import time, hashlib, base64

# Display the changelog
def chng_click():
    chnglog = Tk()
    chnglog.title("Encoder Changelog")
    lbl2 = Label(chnglog, text="7/11/2022: \nCreated the program! Hello World!")
    lbl3 = Label(chnglog, text="7/23/2022: \nCreated microservice!")
    lbl4 = Label(chnglog, text="8/6/2022: \n Added ability to use partner's microservice.")
    lbl5 = Label(chnglog, text="8/7/2022: \n Added b64, sha256, md5, scrollbar.")
    lbl5.pack()
    lbl4.pack()
    lbl3.pack()
    lbl2.pack()
    chnglog.mainloop() 

# Function for clearing input
def clear_input():
    input_box.delete('1.0', END)

# Function for encoding
def encode_fun():

    # clear current contents
    output_box.delete('1.0', END)

    ptext = input_box.get('1.0', END)
    ptext = ptext.strip('\n')
    ptext = ptext.encode('ascii')
    if select_encode.get() == "Base64":
        b64_enc(ptext)
    elif select_encode.get() == "MD5":
        md5_enc(ptext)
    elif select_encode.get() == "Sha256":
        sha256_enc(ptext)


# Encode to base 64
def b64_enc(ptext):
    output = base64.b64encode(ptext)
    output_box.insert('1.0', output)

# Encode to md5
def md5_enc(ptext):
    output = hashlib.md5()
    output.update(ptext)
    output_box.insert('1.0', output.hexdigest())

# Encode to SHA256
def sha256_enc(ptext):
    output = hashlib.sha256()
    output.update(ptext)
    output_box.insert('1.0', output.hexdigest())

# Function to copy contents of output box
def copy_fun():
    main.clipboard_clear()
    main.clipboard_append(output_box.get('1.0', END))
    main.update()

# Export output box to file
def export_fun():
    with open('encoded.txt', 'w', encoding='utf-8') as f:
        f.write(output_box.get('1.0', END))

# Use partner's Microservice to get input
def microservice():
    clear_input()
    with open("service.txt", "w") as f:
        f.write("Start")
    time.sleep(10)
    with open("userOutput.txt", "r", encoding="utf-8") as f2:
        mes = f2.read()
        input_box.insert("1.0", mes)


# Set up the main window
main = Tk()
main.title("Tyler Harwood's Encoder")
main.geometry('820x640')

# Instructions!
lbl = Label(main, text="Enter the text you want to encode below")
lbl.grid(column=2, row=0)

# Create the changelog button
changelog_button = Button(main, text = "Changelog", command=chng_click)
changelog_button.grid(column=0, row=0, padx=10, pady=10)

# Create input box
input_box = Text(main, height=10, width=70, padx=10, pady=10)
input_box.grid(column=1, row=1, columnspan=3)

# Create combobox
selection = StringVar()
select_encode = ttk.Combobox(main, width=25, textvariable=selection)
select_encode['values'] = ('Base64', 'MD5', 'Sha256')
select_encode['state'] = 'readonly'
select_encode.grid(column=2, row=2)
select_encode.set('Select Encoding Method')

# Clear input button
clear1 = Button(main, text = "Clear", command=clear_input, height=1, width=10, pady=10)
clear1.grid(column=1, row=2)

# Encode Button
encode_button = Button(main, text="Encode", command=encode_fun, width=10, pady=10)
encode_button.grid(column=3, row=2)

# Output box
output_box = Text(main, height=10, width=70, pady=10, padx=10)
output_box.grid(column=1, row=3, columnspan=3)

# Copy Button
cpy_button = Button(main, text="Copy Output", command=copy_fun, width=10, padx=10, pady=10)
cpy_button.grid(column=1, row=4)

# Export Button
export_button = Button(main, text="Export Output", command=export_fun, padx=10, pady=10)
export_button.grid(column=3, row=4)

# Microservice Button
micro_button = Button(main, text="Run Microservice", command=microservice, padx=10, pady=10)
micro_button.grid(column=3, row=0)

# Input scrollbar
input_scroll = ttk.Scrollbar(main, orient='vertical', command=input_box.yview)
input_scroll.grid(row=1, column=4, sticky=NS)
input_box['yscrollcommand'] = input_scroll.set

# Output scrollbar
output_scroll = ttk.Scrollbar(main, orient='vertical', command=output_box.yview)
output_scroll.grid(row=3, column=4, sticky=NS)
output_box['yscrollcommand'] = output_scroll.set

# Run the window!
main.mainloop()