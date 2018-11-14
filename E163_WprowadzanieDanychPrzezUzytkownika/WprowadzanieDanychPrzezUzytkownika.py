#################################################
exNumber = 1
print("-" * 5, exNumber, "-" * 30)
# Code:

print('This application calculates distinct roots of quadratic equation.\n')

def check_int(s):
    if s[0] in ('-', '+'):
        return s[1:].isdigit()
    return s.isdigit()

while True:

    aStr = input('Enter the coefficient a: ')
    bStr = input('Enter the coefficient b: ')
    cStr = input('Enter the coefficient c: ')
        
    if not (check_int(aStr) and check_int(bStr) and check_int(cStr)):

        print('One of coefficients is not integer! Please try again.\n')
        
    else:

        a = int(aStr)
        b = int(bStr)
        c = int(cStr)

        if a == 0:
            
            print('It is not quadratic equation (a = 0)!')
            break
            
        else:
            
            discriminant = (b ** 2) - (4 * a * c)

            if discriminant < 0:

                print('This quadratic equation has not got distinct roots! (D < 0)')
                break

            if discriminant == 0:

                x1 = -b / (2 * a)
                print('The distinct root of the quadratic equation is', x1)
                break

            if discriminant > 0:

                x1 = (-b - (discriminant ** 0.5))/ (2 * a)
                x2 = (-b + (discriminant ** 0.5))/ (2 * a)
                print('The distinct roots of the quadratic equation are: \
                        \nx1 = {:.2f} \
                        \nx2 = {:.2f}'.format(x1, x2))
                break
            
#################################################
