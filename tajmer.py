import time

broj = int(input('Unesite neki broj:'))
for i in range(broj, 0, -1):
    print(i)
    time.sleep(0.7)
    
print('Isteklo je vreme!')