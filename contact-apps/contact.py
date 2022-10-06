import sqlite3
from tkinter import *

root = Tk()
root.title("Simple Contact Apps")

# Database
conn = sqlite3.connect('contact_apps.db')
c = conn.cursor()

# Create table
'''
c.execute("""CREATE TABLE contact (
    name text,
    phone_number text
)""")
'''

def add():
    conn = sqlite3.connect('contact_apps.db')
    c = conn.cursor()

    # Insert into table
    c.execute("INSERT INTO contact VALUES (:name, :phone_number)",
        {
            'name' : name.get(),
            'phone_number' : phone_number.get()
        }
    )

    conn.commit()
    conn.close()

    name.delete(0, END)
    phone_number.delete(0, END)

# Query function
def query():
    conn = sqlite3.connect('contact_apps.db')
    c = conn.cursor()

    c.execute("SELECT *, oid FROM contact")
    results = c.fetchall()
    # print(results)

    show_results = ''
    for result in results:
        show_results += str(result[0]) + " "  + "\t" + str(result[1]) + " " + "\t" + str(result[2]) + "\n"

    query_label = Label(frame, text=show_results)
    query_label.grid(row=10, column=0, columnspan=3)

    conn.commit()
    conn.close()

# Update the data
def update():
    conn = sqlite3.connect('contact_apps.db')
    c = conn.cursor()

    result_id = delete_box.get()

    c.execute("""UPDATE contact SET
        name = :name,
        phone_number = :phone_number

        WHERE oid = :oid""",
        {
            'name' : name_editor.get(),
            'phone_number' : phone_number_editor.get(),
            'oid' : result_id
        })
    
    conn.commit()
    conn.close()

    editor.destroy()

def edit():
    global editor

    editor = Tk()
    editor.title("Update Data")

    conn = sqlite3.connect('contact_apps.db')
    c = conn.cursor()

    result_id = delete_box.get()
    c.execute("SELECT * FROM contact WHERE oid = " + result_id)
    results = c.fetchall()

    # Create global variables for text box names
    global name_editor
    global phone_number_editor
    
    # For frame 
    frame = LabelFrame(editor, padx=30, pady=30)
    frame.grid(padx=10, pady=10)

    # Create text box labels and entry
    name_label = Label(frame, text="Name")
    name_label.grid(row=0, column=0, sticky=W)

    name_editor = Entry(frame, width=65, borderwidth=3)
    name_editor.grid(pady=5, row=1, column=0, columnspan=3)

    phone_number_label = Label(frame, text="Phone Number")
    phone_number_label.grid(row=2, column=0, sticky=W)

    phone_number_editor = Entry(frame, width=65, borderwidth=3)
    phone_number_editor.grid(pady=5, row=3, column=0, columnspan=3)

    # Loop through results
    for result in results:
        name_editor.insert(0, result[0])
        phone_number_editor.insert(0, result[1])

    # Create a save button to save edited result
    edit_button = Button(frame, text="Save", command=update, fg="black", bg="#ffe699", padx=30, pady=10)
    edit_button.grid(row=4, column=0, columnspan=3, pady=10)

# Delete the results
def delete():
    conn = sqlite3.connect('contact_apps.db')
    c = conn.cursor()

    c.execute("DELETE FROM contact WHERE oid=" + delete_box.get())

    conn.commit()
    conn.close()

frame = LabelFrame(root, padx=30, pady=30)
frame.grid(padx=10, pady=10)

# For name column
name_label = Label(frame, text="Name")
name_label.grid(row=0, column=0, sticky=W)

name = Entry(frame, width=65, borderwidth=3)
name.grid(pady=5, row=1, column=0, columnspan=3)

# For phone number column
phone_number_label = Label(frame, text="Phone Number")
phone_number_label.grid(row=2, column=0, sticky=W)

phone_number = Entry(frame, width=65, borderwidth=3)
phone_number.grid(pady=5, row=3, column=0, columnspan=3)

# For delete id column
delete_box_label = Label(frame, text="Select ID")
delete_box_label.grid(row=6, column=0, sticky=W)

delete_box = Entry(frame, width=65, borderwidth=3)
delete_box.grid(pady=5, row=7, column=0, columnspan=3)

add_button = Button(frame, text="Add Data", fg="black", command=add, bg="#ffe699", padx=25, pady=10)
query_button = Button(frame, text="Show", fg="black", command=query, bg="#ffe699", padx=35, pady=10, anchor=CENTER)
cancel_button = Button(frame, text="Cancel", command=exit, fg="black", bg="#ffe699", padx=30, pady=10)
delete_button = Button(frame, text="Delete", command=delete, fg="black", bg="#ffe699", padx=30, pady=10)
edit_button = Button(frame, text="Edit", command=edit, fg="black", bg="#ffe699", padx=30, pady=10)

add_button.grid(row=5, column=0, padx=(20, 0), pady=5, sticky=E)
query_button.grid(row=5, column=1, padx=(20,20), pady=10, sticky=E)
cancel_button.grid(row=5, column=2, padx=(0, 20),pady=10, sticky=E)
delete_button.grid(row=8, column=1, padx=(10, 10))
edit_button.grid(row=9, column=1, pady=(10,10))

conn.commit()
conn.close()

root.mainloop()
