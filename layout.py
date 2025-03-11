import tkinter as tk
from tkinter.font import Font

COLORS = {
    'left':'lightblue',
    'right':'yellow',
    'text-color':'black',
    'entry-bg-color':'white',
    'correct-answear':'green',
    'bad-answear':'red'
}

PARAMETERS = {
    'font-size':24,
    'bind-check-button':'<Return>',
    'bind-check-keycode':13
}


class Layout:
    def __init__(self):
        self.__root = None
        self.__cn_left = None
        self.__cn_right = None
        self.__left_label = None
        self.__right_frame = None
        self.__right_label = None
        self.__right_entry = None

    def define_layout(self):
        self.__root = tk.Tk()
        self.__root.geometry("1000x500")

        # set grid
        self.__root.grid_columnconfigure((0, 1), weight=1, uniform='a')
        self.__root.grid_rowconfigure(0, weight=1)

        # set two poles
        self.__cn_left = tk.Canvas(bg=COLORS['left'], highlightthickness=0)
        self.__cn_right = tk.Canvas(bg=COLORS['right'], highlightthickness=0)
        self.__cn_left.grid(row=0, column=0, sticky='NSWE')
        self.__cn_right.grid(row=0, column=1, sticky='NSWE')

        # set left label
        self.__left_label = tk.Label(
            text='sample',
            bg=COLORS['left'],
            font=Font(family='Times New Roman Bold', size=PARAMETERS['font-size']),
            foreground=COLORS['text-color']
        )
        self.__left_label.grid(row=0, column=0)

        # split right side in two rows
        self.__right_frame = tk.Frame(self.__root)
        self.__right_frame.config(bg=COLORS['right'])
        self.__right_frame.grid(row=0, column=1, sticky='NSWE')
        self.__right_frame.grid_rowconfigure((0, 1), weight=1, uniform='c')
        self.__right_frame.grid_columnconfigure(0, weight=1)
        # content in right side
        self.__right_label = tk.Label(
            self.__right_frame,
            text='przykład',
            bg=COLORS['right'],
            font=Font(family='Times New Roman Bold', size=PARAMETERS['font-size']),
            foreground=COLORS['text-color']
        )
        self.__right_label.grid(row=0, column=0, pady=20, sticky='S')
        self.__right_entry = tk.Entry(
            self.__right_frame,
            bg=COLORS['entry-bg-color'],
            font=Font(family='Times New Roman Bold', size=PARAMETERS['font-size']),
            foreground=COLORS['text-color'],
            justify='center'
        )
        self.__right_entry.grid(row=1, column=0, pady=20, sticky='N')
        self.__right_entry.focus()

    def display_layout(self):
        self.__root.mainloop()

    def change_right_bg_color(self, color):
        self.__right_frame.config(bg=color)
        self.__right_label.config(bg=color)

    def change_right_text(self, word):
        self.__right_label.config(text=word)

    def change_entry_text(self, word):
        self.__right_entry.config(textwrap=word)

    def bind_entry(self, bind_type, bind_function):
        self.__right_entry.bind(bind_type,bind_function)

    def get_entry_text(self)->str:
        return self.__right_entry.get()


class GameLayout(Layout):
    def __init__(self, after_push_key_function):
        super().__init__()
        self.define_layout()
        self.bind_entry(PARAMETERS['bind-check-button'], after_push_key_function)

    def correct_answear(self, text):
        self.change_right_bg_color(COLORS['correct-answear'])

    def bad_answear(self):
        self.change_right_bg_color(COLORS['bad-answear'])

    def new_question(self, new_text):
        self.change_right_bg_color(COLORS['right'])
        self.change_right_text(new_text)
        self.change_entry_text('')
