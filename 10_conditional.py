# CONDITIONAL STATEMENTS
# if, elif, else

# if statement
# if condition proves to be True, the code block will be executed

# else statement
# if the condition proves to be False, the code block will be executed

# elif statement
# if the first condition proves to be False, the elif statement will be checked

# A restaurant wants to apply diffeerent discounts based on the amount its customer spent
bill_total = 210

discount_1 = 10
discount_2 = 20

if bill_total > 100 and bill_total < 200:
    print("Bill is greater than 100")
    bill_total = bill_total - discount_1
elif bill_total > 200:
    print("Bill is greater than 200")
    bill_total = bill_total - discount_2
else:
    print(f"Bill is less or equal to 100 or 200")

print(f"Total bill: {bill_total}")


# Light switch
# on = True
# off = False

# if
# Light is currently off
current = False

if current:
    current = False
    print("Turning light off")

if not current:
    current = True
    print("Turning light on")

    """
    De acuerdo con el ejemplo del interruptor de luz, el estado del interruptor se puede almacenar con un valor booleano de True (Verdadero) o False (Falso).

    On = Verdadero
    Off = Falso
    
    El fragmento de código anterior tiene una variable denominada current que mantiene un registro del estado de la luz, encendida o apagada. La primera sentencia if comprobará si la luz está encendida, y de estarlo, el flujo irá dentro de la condición y establecerá la variable current en False, apagando la luz. En el fragmento de código anterior, el valor de la variable current se establece inicialmente en False, por lo que esta condición no se cumple.

    La segunda sentencia if verificará si la luz está apagada y, si es así, el flujo pasará dentro de la condición y establecerá la variable current en True, encendiendo la luz. 
    """

# if else
current = False

if current:
    current = False
    print("Turning light off")
else:
    current = True
    print("Turning light on")

    """
    La sentencia else ha hecho que su código sea un poco más fácil de leer y dado que el flujo se relaciona con la misma condición, tiene más sentido combinarlos como parte de una sola unidad.
    """

# elif
"""Supongamos que quiere ofrecer un determinado descuento a los clientes si gastan más de $100. También proporcionará un descuento adicional si ese cliente forma parte de un programa de fidelización. Si el cliente no forma parte del programa de fidelización y no gastó más de $100, se aplica un cargo por servicio del 5 %.
"""
loyalty_customer = True
total_bill = 124

if loyalty_customer and total_bill > 100:
    # give 20% discount
    total_bill = total_bill - (float(total_bill)/ 100) * 20
elif total_bill > 100:
    # give 10% discount
    total_bill = total_bill - (float(total_bill)/ 100) * 10
else:
    # sorry no discount, 5% service charge applied.
    print('Sorry, no discount ...')

print('Total Bill: ', float(total_bill))

"""El fragmento de código anterior primero verifica si el cliente forma parte del programa de fidelización y si está gastando más de $100. Si se cumplen ambas condiciones, se aplica un descuento del 20% a la factura. La sentencia elif solo se ejecutará si no se cumple la primera condición if. El estado de cuenta elif solo verificará si la factura supera los $100 y si es así, aplicará un descuento del 10 % a la factura.

La sentencia else final solo se ejecuta si no se cumple ninguna de las otras dos condiciones. En este caso, se aplica un cargo del 5 % a la factura.
"""

# LOOPS
# for, while

# for loop
# check the condition and execute the code block until the condition is False

