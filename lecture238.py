import tkinter as tk
from tkinter import ttk
win = tk.Tk()
win.title('Menubar tutorial')


def func():
    print('func called')

#Menu{simple}********************************************************
# menubar = tk.Menu(win)

# menubar.add_command(label='save',command=func)
# menubar.add_command(label='save as',command=func)
# menubar.add_command(label='copy',command=func)
# menubar.add_command(label='paste',command=func)


main_menu = tk.Menu(win)
file_menu = tk.Menu(main_menu, tearoff=0)
file_menu.add_command(label='New_file',command=func)
file_menu.add_command(label='New_window',command=func)
file_menu.add_separator()#...for addind separation line
file_menu.add_command(label='Save_file',command=func)

#edit menu

edit_menu = tk.Menu(main_menu,tearoff=0)
edit_menu.add_command(label='Undo',command=func)
edit_menu.add_command(label='Redo',command=func)

main_menu.add_cascade(label='File', menu=file_menu)
main_menu.add_cascade(label='File', menu=edit_menu)


win.config(menu=main_menu)

win.mainloop()