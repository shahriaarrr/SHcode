from tkinter import *
from unicodedata import name

def main_program(ctx, file_name):
    my_file = open(f'./{str(file_name)}', 'w')
    my_file.write(str(ctx))
    my_file.close()

class Main():
    def __init__(self):
        self.win = Tk()
        
        #config
        self.config_title = 'notepad'
        self.config_width = 450
        self.confing_heigt = 550
        self.config_resizable = [False, False]

        self.Load_Configs()
        self.Load_objects()

        mainloop()

    def Load_Configs(self):
        self.win.title(self.config_title)
        self.win.geometry(str(self.config_width) + 'x' + str(self.confing_heigt))
        self.win.resizable(self.config_resizable[0], self.config_resizable[1])

    def get_info(self):
        ctx = self.ctx_input.get("1.0", "end-1c")
        name_input = self.name_input.get()

        main_program(ctx, name_input)
    
    def Load_objects(self):
        ctx_input = Text(
            self.win,
            background = '#FFFFFF',
            foreground = 'black',
            height = 20,
            width = 60,
        )
        self.ctx_input = ctx_input
        ctx_input.pack()

        Label(
            self.win,
            text = '     ',
            font = ('Arial', 10)
        ).pack()

        Label(
            text = "filename: ",
            foreground = 'black',
            font = ('Arial', 10) ,
        ).pack()
        name_input = Entry(
            self.win,
            background = '#FFFFFF',
            foreground = 'black',
            width = 24,
        )
        self.name_input = name_input
        name_input.pack()

        Label(
            self.win,
            text = '     ',
            font = ('Arial', 10)
        ).pack()

        send_button = Button(
            self.win,
            text = 'save',
            background = '#FFFFFF',
            foreground = 'black',
        )
        send_button.config(command = self.get_info)
        send_button.pack()


app = Main()