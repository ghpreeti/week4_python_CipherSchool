# for loop
# name
# age
# city

import tkinter as tk
from tkinter import ttk
win = tk.Tk()
win.title('LOOP')

labels = ['what is your name :', 'age : ', 'gender : ', 'country : ', 'states : ', 'city : ']

# name_label = ttk.Label(win,text="whar is your name : ")
# name_label.grid(row=0, column=0,sticky=tk.w)

for i in range(len(labels)):
    cur_label = 'label' + str(i) #label10 , label1
    cur_label = ttk.Label(win, text = labels[i])
    cur_label.grid(row=i, column=0,sticky=tk.W)

# entry_boxex
name_var = tk.StringVar()

user_info = {
    'name':tk.StringVar(),
    'age':tk.StringVar(),
    'gender':tk.StringVar(),
    'country':tk.StringVar(),
    'state':tk.StringVar(),
    'city':tk.StringVar()
}


counter=0
for i in user_info:
    cur_entrybox= 'entry' + i # entryname,#entryage
    cur_entrybox = ttk.Entry(win, width=16, textvariable=user_info[i] )
    cur_entrybox.grid(column=1, row=counter )  
    counter += 1 


def submit():
    print(user_info['name'].get())
    print(user_info.get('age').get())
    print(user_info.get('gender').get())
    print(user_info.get('country').get())
    print(user_info.get('state').get())
    print(user_info.get('city').get())


submit_btn = ttk. Button(win,text='submit',command=submit)
submit_btn.grid(row=6, columnspan=2)


# name_entry = ttk.Entry(win, width=16, textvariable=name_var )
# name_entry.grid(row=0 , column=1)  
win.mainloop()
