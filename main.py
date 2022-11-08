import time

a = int(input("Valor de A: "))
b = int(input("Valor de B: "))
c = int(input("Valor de C: "))

def delta(a,b,c):
    return((b**2) - 4 * a * c)

delta_calc = delta(a,b,c) ** 0.5

def calc():
  def x1():
    return(((- b + delta_calc) / (2 * a)))
  x1_calc = x1()

  def x2():
      return(((- b - delta_calc) / (2 * a)))
  x2_calc = x2()

  def calc_print():
    print("\n")
    print("Calculando Delta...")
    time.sleep(2)
    print("b**2 -4*a*c")
    time.sleep(1)
    print("{}**2 -4*{}*{}".format(b,a,c))
    time.sleep(1)
    print("{} + {}".format(b**2,-4*a*c))
    time.sleep(1)
    print("Delta = {}".format(delta(a,b,c)))
    time.sleep(1)
    print("\n")
    print("Calculando Bhaskara...")
    time.sleep(2)
    print("(-b +- raiz(delta)) / 2*a")
    time.sleep(1)
    print("(-{} +- raiz({})) / 2*{}".format(b,delta(a,b,c),a))
    time.sleep(1)
    print("\n")
    print("-{} + {} / {}".format(b,delta_calc,2*a))
    time.sleep(1)
    print("{} / {}".format(b + delta_calc,2*a))
    time.sleep(1)
    print("{}".format(x1_calc))
    time.sleep(1)
    print("\n")
    print("-{} - {} / {}".format(b,delta_calc,2*a))
    time.sleep(1)
    print("{} / {}".format(b + delta_calc,2*a))
    time.sleep(1)
    print("{}".format(x2_calc))
    time.sleep(1)
    print("\n")
    print("x1 = {}".format(x1_calc))
    print("x2 = {}".format(x2_calc))
    time.sleep(1)
    input("\nPressione <enter> para encerrar!")
    time.sleep(1)
  calc_print()

if delta(a,b,c) > 0:
  calc()
else:
  print("\nDelta é imaginario!")
  input("\nPressione <enter> para encerrar!")
  time.sleep(1)