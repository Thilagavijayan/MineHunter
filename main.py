from tkinter import *

root = Tk()
# Override the setting of window
root.configure(bg="black")
root.geometry('1440x720') # To reshape the size of window
root.title("MineHunter Game") # To change the name of the window
root.resizable(False, False) # Maximize disabled

# header
top_frame  =  Frame(
    root,
    bg= "red", # change later to black
    width = 1440,
    height = 180
    )
top_frame.place(x = 0,y=0) # To leave space in header

# Sidebar
left_frame = Frame (
    bg= 'blue',
    width = 360,
    height = 540
)
left_frame.place(x = 0,y = 180)

# Run the window
root.mainloop()
