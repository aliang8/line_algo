from display import *

# Bresenham's Line Algorithm
# ========================
# f(x,y) = Ax + By + C
# A = dy
# B = -dx
# C = (dx)b where b is the y-intercept
# ========================

def draw_line( screen, x0, y0, x1, y1, color ):
    # switch coordinates
    if x0 > x1:
        tmp = x0
        x0 = x1
        x1 = tmp

        tmp = y0
        y0 = y1
        y1 = tmp
        
    A = y1 - y0
    B = -(x1 - x0)

    x = x0
    y = y0

    # Quadrant IV
    if y0 >= y1 and x0 <= x1:
        # Octant 7
        if abs(A) > abs(B):
            d = A - 2 * B
            while y >= y1:
                plot(screen, color, x, y)
                if d > 0:
                    x += 1
                    d += 2 * A
                y -= 1
                d -= 2 * B
        # Octant 8
        else:
            d = 2 * A - B
            while x <= x1:
                plot(screen, color, x, y)
                if d < 0:
                    y -= 1
                    d -= 2 * B
                x += 1
                d += 2 * A
    # Quadrant I
    else:
        # Octant 1
        if abs(A) < abs(B):
            d = 2 * A + B
            while x <= x1:
                plot(screen, color, x, y)
                if d > 0:
                    y += 1
                    d += 2 * B
                x += 1
                d += 2 * A
        # Octant 2
        else:
            d = A + 2 * B
            while y <= y1:
                plot(screen, color, x, y)
                if d < 0:
                    x += 1
                    d += 2 * A
                y += 1
                d += 2 * B
           
    return screen