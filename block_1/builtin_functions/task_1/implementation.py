
class Value:
    def __init__(self, val):
        self.val = val
        
    def get_value(self):
        return self.val
        
    def __add__(self, other):
        return self.val + other
        
    def __sub__(self, other):
        return self.val - other
        
    def __mul__(self, other):
        return self.val * other
        
    def __truediv__(self, other):
        if other != 0:
            return self.val / other
        else:
            raise ValueError("Division by zero")
