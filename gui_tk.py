import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from str_tools import str_to_bin, bin_to_str, char_to_bin

class Application(ttk.Window):
    def __init__(self, *args, **kwargs):
        # self.title = "Binary tools"
        # self.size = (800,600)
        # self['padx'] = 20
        super().__init__(title="Binary Tools", resizable=(False, False), *args, **kwargs)
        self.create_widgets()
        # self.pack()
        
        self['padx'], self['pady'] = 10,10
        # self['background'] = "black"
        
    def create_widgets(self):
        self.str_in_lbl = ttk.Label(self, text="Text: ")
        self.str_in_lbl.grid(row=0, column=0)
        
        # ttk.Entry()
        self.str_in_txtbox = ttk.Text(self, height=5)
        self.str_in_txtbox.grid(row=0, column=1)
        self.str_in_txtbox.bind("<Return>", self.show_binary)

        self.bin_out_lbl = ttk.Label(self, text="Binary: ")
        self.bin_out_lbl.grid(row=1, column=0)

        self.bin_out_txtbox = ttk.Text(self, height=5)
        self.bin_out_txtbox.grid(row=1, column=1, pady=10)

        self.convert_btn = ttk.Button(self, text="Convert text to binary", command=self.show_binary, bootstyle=SUCCESS)
        self.convert_btn.grid(row=2, column=0, pady=10)

        self.convert_btn = ttk.Button(self, text="Convert binary to text", command=self.show_str, bootstyle=INFO)
        self.convert_btn.grid(row=2, column=2, pady=10)

        self.bin_note_lbl = ttk.Label(self, bootstyle=WARNING, text="Note: When entering the binary code to convert to text, please add 4 space characters after the corresponding binary code for each character.")
        self.bin_note_lbl.grid(row=3, column=1)

        # self.convert_btn.bind()

    def say_hi(self):
        print("hi there, everyone!")

    def show_binary(self, *args):
        str_in = self.str_in_txtbox.get("1.0", END)
        bin_array = [char_to_bin(char) for char in str_in]
        self.bin_out_txtbox.delete("1.0", END)
        self.bin_out_txtbox.insert("1.0", "    ".join(bin_array))
        return 'break'
    
    def show_str(self, *args):
        bin_in = self.bin_out_txtbox.get("1.0", END).split("    ")
        str_out = "".join([bin_to_str(bin_sequence) for bin_sequence in bin_in])
        self.str_in_txtbox.delete("1.0", END)
        self.str_in_txtbox.insert("1.0", str_out)
        return 'break'

# root = tk.Window()
app = Application(themename="superhero")
app.mainloop()

str().__contains__(o)