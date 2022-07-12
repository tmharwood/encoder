
from tkinter import *
from tkinter import ttk

# Display the changelog
def chng_click():
    chnglog = Tk()
    chnglog.title("Encoder Changelog")
    lbl2 = Label(chnglog, text="7/11/2022: \nCreated the program! Hello World!")
    lbl2.pack()
    chnglog.mainloop() 

# Function for clearing input
def clear_input():
    input_box.delete('1.0', END)

# Function for encoding
def encode_fun():
    # clear current contents
    output_box.delete('1.0', END)
    output_box.insert('1.0', input_box.get('1.0', END))
    # Remove the automatically inserted newline. Code modified from:
    # https://stackoverflow.com/questions/48220788/how-can-i-remove-newline-character-n-at-the-end-of-text-widget
    # Accessed 7/11/22
    if output_box.get('end-1c', 'end') == '\n':
        output_box.delete('end-1c', 'end')

# Function to copy contents of output box
def copy_fun():
    main.clipboard_clear()
    main.clipboard_append(output_box.get('1.0', END))
    main.update()

def export_fun():
    with open('encoded.txt', 'w', encoding='utf-8') as f:
        f.write(output_box.get('1.0', END))


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
select_encode['values'] = ('test1', 'test2', 'test3')
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

# Run the window!
main.mainloop()