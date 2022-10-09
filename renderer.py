import numpy as np


class HUSCIIRenderer:
    def __init__(self, width=80, height=25, bg_char="."):
        """The one and only HUSCII renderer"""
        self.WIDTH = width
        self.HEIGHT = height
        self.BG = bg_char
        self.clear_chars()


    def clear_chars(self):
        """Resets the screen to its background char"""
        self.chars = np.full((self.HEIGHT, self.WIDTH), self.BG, dtype='S1')


    def draw(self):
        """Prints the scene."""
        new_lines = np.full((self.HEIGHT, 1), "\n", "S1")
        chars = np.hstack((self.chars, new_lines))
        screen = "".join(chars.flatten().astype(str))
        print(screen)
        self.clear_chars()

    def round_inputs(f):
        """Decorator, rounds all float functions parameters to int."""
        def wrapper(*args, **kwargs):
            r_args = []
            for arg in args:
                if isinstance(arg, float):
                    arg = round(arg)
                r_args.append(arg)

            r_kwargs = {}
            for key, arg in kwargs.items():
                if isinstance(arg, float):
                    arg = round(arg)
                r_kwargs[key] = arg

            f(*r_args, **r_kwargs)
        return wrapper


    @round_inputs
    def point(self, x, y, char):
        """Sets the point x, y to the character char."""
        if x >= 0 and y >= 0 and x < self.WIDTH and y < self.HEIGHT:
            self.chars[y, x] = char

    @round_inputs
    def rect(self, x, y, w, h, char):
        """Draws a rectangle whose top left corner is at <x, y> and of width w and height h."""
        self.chars[y:y+h, x:x+w] = char

    @round_inputs
    def ellipse(self, x, y, w, h, char):
        """
        Draws an ellipse of center (x, y) and of width h and height h.
        """
        # Source: https://stackoverflow.com/questions/10322341/simple-algorithm-for-drawing-filled-ellipse-in-c-c
        hh = h * h
        ww = w * w
        hhww = hh * ww
        x0 = w
        dx = 0
        for i in range(-w, w):
            self.point(x + i, y, char)
        for j in range(1, h):
            x1 = x0 - (dx - 2)
            while True:
                x1 -= 1
                if (x1*x1*hh + j*j*ww <= hhww):
                    break
            dx = x0 - x1 
            x0 = x1
            for i in range(-x0, x0):
                self.point(x + i, y - j, char)
                self.point(x + i, y + j, char)


    @round_inputs
    def line(self, x1, y1, x2, y2, char):
        """Draws a line between the two points (x1, y1) (x2, y2)."""
        # Source: https://github.com/daQuincy/Bresenham-Algorithm
        dx = abs(x2 - x1)
        dy = abs(y2 - y1)
        m = dy/dx
        flag = True
        
        self.point(x1, y1, char)
        
        step = 1
        if x1 > x2 or y1 > y2:
            step = -1

        mm = False   
        if m < 1:
            x1, x2 ,y1 ,y2 = y1, y2, x1, x2
            dx = abs(x2 - x1)
            dy = abs(y2 - y1)
            mm = True
            
        p0 = 2*dx - dy
        x = x1
        y = y1
        for i in range(abs(y2-y1)):
            if flag:
                x_previous = x1
                p_previous = p0
                p = p0
                flag = False
            else:
                x_previous = x
                p_previous = p
            if p >= 0:
                x = x + step

            p = p_previous + 2*dx -2*dy*(abs(x-x_previous))
            y = y + 1
            if mm:
                self.point(y, x, char)
            else:
                self.point(x, y, char)

    @round_inputs
    def text(self, x, y, s):
        """Write the text s statring at the x, y location on the screen."""
        self.chars[y, x:x + len(s)] = list(s[:max(self.WIDTH - x, 0)])
    

if __name__ == "__main__":
    r = HUSCIIRenderer()
    # r.rect(40, 10, 50, 10, "O")
    # r.ellipse(40, 12, 10, 5, "O")
    # r.text(60,20,"Hello World!")
    r.line(3, 5, 70, 20, "O")
    r.draw()