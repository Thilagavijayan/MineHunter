from tkinter import *
from cell import Cell
import settings
import utils


root = Tk()
# Override the setting of window
root.configure(bg="black")
root.geometry(f'{settings.WIDTH}x{settings.HEIGHT}') # To reshape the size of window
root.title("MineHunter Game") # To change the name of the window
root.resizable(False, False) # Maximize disabled

# header
top_frame  =  Frame(
    root,
    bg= "black", # change later to black
    width = settings.WIDTH,
    height = utils.height_percent(25)
    )
top_frame.place(x = 0,y=0) # To leave space in header

# Sidebar
left_frame = Frame (
    bg= 'black',# change later to black
    width = utils.width_percent(25),
    height = utils.height_percent(75)
)
left_frame.place(x = 0,y = utils.height_percent(25))

# Centerframe
center_frame = Frame(
    root,
    bg = 'black', # change later to black
    width = utils.width_percent(75),
    height= utils.height_percent(75)
)
center_frame.place(
    x = utils.width_percent(25),
    y = utils.height_percent(25),
)

for x in range(settings.GRID_SIZE):
    for y in range(settings.GRID_SIZE):
        c = Cell(x, y)
        c.create_btn_object(center_frame)
        c.cell_btn_object.grid(
            column = x,row= y
        )

# Run the window
root.mainloop()
