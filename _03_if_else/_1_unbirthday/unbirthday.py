from tkinter import Tk, messagebox,simpledialog

window = Tk()
window.withdraw()
birthday=simpledialog.askstring(title='',prompt='what is your birthday?')
if birthday=="06/05":
    messagebox.showinfo(title="",message='happybirthday i got you a apple thats so rotten it melted :)')
else:
    messagebox.showinfo(title="",message='oh well guess im not giving my over rotten apple to you since its your unbirthday')
