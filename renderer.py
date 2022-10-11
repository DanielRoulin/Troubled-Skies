import numpy as np


class HUSCIIRenderer:
    def __init__(self, width=80, height=25, bg_char=".", dtype="S1"):
        """The one and only HUSCII renderer"""
        self.WIDTH = width
        self.HEIGHT = height
        self.BG = bg_char
        self.dtype = dtype # "S1" for ASCII only, str for Unicode support
        self.clear_chars()


    def clear_chars(self):
        """Resets the screen to its background char"""
        self.chars = np.full((self.HEIGHT, self.WIDTH), self.BG, dtype=self.dtype)


    def draw(self):
        """Prints the scene."""
        new_lines = np.full((self.HEIGHT, 1), "\n", self.dtype)
        chars = np.hstack((self.chars, new_lines))
        screen = "".join(chars.flatten().astype(str))[:-1]
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
        """Sets the point (x, y) to the character char."""
        if x >= 0 and y >= 0 and x < self.WIDTH and y < self.HEIGHT:
            self.chars[y, x] = char


    @round_inputs
    def rect(self, x, y, w, h, char):
        """Draws a rectangle whose top left corner is at (x, y) and of width w and height h."""
        if x < 0:
            w = max(w + x, 0)
            x = 0
        if y < 0:
            h = max(h + y, 0)
            y = 0
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
        if y >= 0 and y < self.HEIGHT and x < self.WIDTH and x > -len(s):
            start = -x if x < 0 else 0
            stop = self.WIDTH - x if x > self.WIDTH-len(s) else len(s)
            self.chars[y, max(0, x):min(x + len(s), self.WIDTH)] = list(s[start:stop])
        

    @round_inputs
    def sprite(self, x, y, chars):
        """Draws the 2d array of chars on the screen, (x, y) determines the top left location."""
        maxw = max(len(line) for line in chars)
        chars = np.array([list(line.ljust(maxw)) for line in chars], dtype = self.dtype)
        h, w = chars.shape
        if y > -h and y < self.HEIGHT and x < self.WIDTH and x > -w:
            start_x = -x if x < 0 else 0
            stop_x = self.WIDTH - x if x > self.WIDTH-w else w
            start_y = -y if y < 0 else 0
            stop_y = self.HEIGHT - y if y > self.HEIGHT-h else h
            self.chars[max(0, y):min(y + h, self.HEIGHT), max(0, x):min(x + w, self.WIDTH)] = chars[start_y:stop_y, start_x:stop_x]
        
    

# if __name__ == "__main__":
    # r = HUSCIIRenderer()
    # # r.rect(40, 10, 50, 10, "O")
    # # r.ellipse(40, 12, 20, 5, "O")
    # # r.text(60,20,"Hello World!")
    # # r.line(3, 5, 70, 20, "O")
    # r.sprite(0, 30, [" O O ",
    #                  "\   /",
    #                  " --- "])
    # # r.text(75, 24, "ABCDEFGHIJ")
    # # r.rect(-15, -25, 10, 10, "A")
    # r.draw()
