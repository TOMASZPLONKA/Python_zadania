ile = 0
for i in range(101):
    if i % 3 == 0 or i % 5 == 0:
        print(i)
        ile +=1
print(f'Wystąpiło {ile} liczb podzielnych przez 3 lub 5' )

