def summ(a, b):
  print (a + b)

def div(a, b):
  print (a / b)

def mult(a, b):
  print (a * b)

def sub(a, b):
  print (a - b)

def allert(x):
  operands = ['+', '-', '*', '/']
  if x not in operands:
    print('Ошибка!')     


def main_menu():
  operands = ['+', '-', '*', '/']
  print('''
  | ========================================================
  | Польская нотация (запись), также известна как префиксная 
  | нотация (запись), это форма записи логических, 
  | арифметических и алгебраических выражений. Характерная  
  | черта такой записи — оператор располагается слева от 
  | операндов. Например, выражение, которое в традиционной 
  | инфиксной нотации записывается:
  | (5 − 6) * 7
  | в префиксной может быть записано как:
  |  * − 5 6 7
  | ========================================================
  ''')
  while True:
    operation = input('Введите выражение: ').split()
    assert len(operation) <= 3, 'Введите только два числа'
    num1 = int(operation[1])
    num2 = int(operation[2])
    if operation[0] == '+':
      summ(num1, num2)
    elif operation[0] == '-':
      sub(num1, num2)
    elif operation[0] == '*':
      mult(num1, num2)
    elif operation[0] == '/':
      try:
        div(num1, num2)
      except ZeroDivisionError:
        print('На ноль делить нельзя!')
      except TypeError:
        print('Проверьте, что формат данных')
      
    assert operation[0] in ['+', '-', '*', '/'], 'Используйте: "+", "-", "*", "/"'

  

main_menu()

operands = ['+', '-', '*', '/']

