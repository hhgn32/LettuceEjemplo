class Calculator(object):
    def add(self, x, y):
        number_types = (int, long, float, complex)

        if isinstance(x, number_types) and isinstance(y, number_types):
            return x + y
        else:
            raise ValueError

    def minsinweeks(self, num_weeks):
  		return num_weeks * (7*24*60)


    def task_052(num):
      """
      Calcula el residuo de 2304811/ 47
      sin usar operador %
      ejemplo:
      >>> task_052(2304811)
      25
      """
      cociente = num/47
      resto = 47 - (num * cociente)
