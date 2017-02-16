from display import *
from draw import *

s = new_screen()
c = [ 255, 255, 0 ]

XRES = 500
YRES = 500

# the sun!

draw_line(s, 0, YRES/4, XRES/2, YRES, c);
draw_line(s, XRES, YRES/4, XRES/2, YRES, c);
draw_line(s, 0, YRES/4, XRES, YRES/4, c);

c[1] = 165;
draw_line(s, 0, 3 * YRES/4, XRES/2, 0, c);
draw_line(s, XRES, 3 * YRES/4, XRES/2, 0, c);
draw_line(s, 0, 3 * YRES/4, XRES, 3 * YRES/4, c);

display(s)
save_extension(s, 'img.png')