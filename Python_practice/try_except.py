
try:
    numerator = int(input("Ender number to devide "))
    denominator = int(input("Enter a number to divide by "))
    result = numerator / denominator
    
except ZeroDivisionError as e:
    print(e)
    print("You can't divide by zero  !")

except ValueError as e:
    print(e)
    print("Ender only number idiota !")

except Exception as e:   # <-- Kady błąd do ktorego nie ma konkretnego excepta takiego jak powyżej zostanie obsłóżony przez ten except Exception:
    print(e)
    print('Something went wrong')
else:   # <--- Wykona sie gdy nie wystapi żaden except
    print(result)
finally:    # <--- Zawsze sie wykona
    print("This will  always execute")


'''
cac = {'Poland': 'warsaw'}
try:
    print(cac['Poland'])
except KeyError:
    print('klucz nie zostal znaleziony')
except ZeroDivisionError:
    print('Nie mozna dzielic przez 0')
finally:
    print("kkk")


'''
    