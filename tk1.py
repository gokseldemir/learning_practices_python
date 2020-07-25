from tkinter import *


# player controls
def p1_move_N(self):
    global p1_y
    canvas.create_line(p1_x, p1_y, p1_x, (p1_y-line_length), width=line_width, fill=p1_colour)
    p1_y = p1_y - line_length
def p1_move_S(self):
    global p1_y
    canvas.create_line(p1_x, p1_y, p1_x, p1_y+line_length, width=line_width, fill=p1_colour)
    p1_y = p1_y + line_length
def p1_move_E(self):
    global p1_x
    canvas.create_line(p1_x, p1_y, p1_x + line_length, p1_y, width=line_width, fill=p1_colour)
    p1_x = p1_x + line_length
def p1_move_W(self):
    global p1_x
    canvas.create_line(p1_x, p1_y, p1_x - line_length, p1_y, width=line_width, fill=p1_colour)
    p1_x = p1_x - line_length
def erase_all(self):
    canvas.delete(ALL)
##### main:
window = Tk()
window.title("MyEtchASketch")
canvas = Canvas(bg=canvas_colour, height=canvas_height, width=canvas_width, highlightthickness=0)
canvas.pack()
# bind movement to key presses
window.bind("<Up>", p1_move_N)
window.bind("<Down>", p1_move_S)
window.bind("<Left>", p1_move_W)
window.bind("<Right>", p1_move_E)
window.bind("u", erase_all)
window.mainloop()
