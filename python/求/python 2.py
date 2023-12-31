from turtle import done


a = float(input('第一个角> '))
b = float(input('第二个角> '))
c = float(input('第三个角> '))
cri = a+b+c
s = (a+b+c)/2
area = (s*(s-a)*(s-b)*(s-c))**(1/2)
print(f'周长={cri:.2f}')
print(f'面积={area:.2f}')
done()