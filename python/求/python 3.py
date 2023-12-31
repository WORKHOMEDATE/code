from turtle import done


a = float(input('输入> '))
b = float(input('输入> '))
c = float(input('输入> '))
x = (-b+(b**2-4*a*c)**(1/2))/(2*a)
print(f'{x:.2f}')
done()