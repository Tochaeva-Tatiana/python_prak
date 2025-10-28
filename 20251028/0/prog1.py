class Rectangle:
    count = 0
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        Rectangle.count += 1
        setattr(self, f"rect_{Rectangle.count}", Rectangle.count)

    def __str__(self):
        return  f"{Rectangle.count}, ({self.x1}, {self.y1}), ({self.x1}, {self.y2}), ({self.x2}, {self.y2}), ({self.x2}, {self.y1})"
    
    def sqar(self):
        return (abs(self.x2 - self.x1) * abs(self.y1 - self.y2))

    def __lt__(self, other):
        return self.sqar() < other.sqar()
    
    def __eq__(self, other):
        return self.sqar() == other.sqar()
    
    def __mul__(self, other):
        x1 = self.x1 * other
        y1 = self.y1 * other
        x2 = self.x2 * other
        y2 = self.y2 * other
        return self.__class__(x1, y1, x2, y2)
    
    __rmul__ = __mul__

    def list(self):
        li = [(self.x1, self.y1), (self.x1, self.y2), (self.x2, self.y2), (self.x2, self.y1)]
        return li
        
    # def __getitem__(self, idx):
    #     return self.list()[idx]

    def __iter__(self):
        return ((self.x1, self.y1), (self.x1, self.y2), (self.x2, self.y2), (self.x2, self.y1))
    
    def __bool__(self):
        return self.sqar() > 0
    
    def __del__(self):
        print("deeeelllllll")


a = Rectangle(1, 2, 3, 4)
print(a)