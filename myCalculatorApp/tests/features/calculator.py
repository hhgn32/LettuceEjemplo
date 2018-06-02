class Calculator(object):
    def add(self, x, y):
        number_types = (int, long, float, complex)
 
        if isinstance(x, number_types) and isinstance(y, number_types):
            return x + y
        else:
            raise ValueError

    def minsinweeks(self, num_weeks):
  		return num_weeks * (7*24*60)