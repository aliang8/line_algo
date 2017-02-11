from display import *
from draw import *

screen = new_screen()
color = [ 0, 255, 0 ]

draw_line(screen, 0, 0, 500, 250, color)
display(screen)
save_extension(screen, 'img.png')
