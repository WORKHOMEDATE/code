from turtle import done


i = 1
while i <= 5:
    if i == 3:
        print(f'大虫子，第{i}个不吃了')
        i += 1
        continue
    print(f'吃了第{i}个苹果')
    i += 1
done()