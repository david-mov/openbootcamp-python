import tkinter as tk
from tkinter import ttk

def main():
    root = tk.Tk()

    root.title('Exercise with Radio Buttons')
    root.geometry("350x200")

    label = ttk.Label(text='Choose an option: ')
    label.pack(fill='x', padx=5, pady=5)

    options = (('Option 1', 'Value 1'), 
            ('Option 2', 'Value 2'), 
            ('Option 3', 'Value 3'))

    selected = tk.StringVar()

    def reset_selection():
        selected.set('')

    for option in options:
        r = ttk.Radiobutton(
            root,
            text=option[0],
            value=option[1],
            variable=selected
        )
        r.pack(fill='x', padx=5, pady=5)

    button = ttk.Button(
        root,
        text='Reset selection',
        command=reset_selection)

    button.pack(fill='x', padx=5, pady=5)

    root.mainloop()

if __name__ == '__main__':
    main()