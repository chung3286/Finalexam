def return_m(i):
    mi=0.0
    for num in range(1, i+1):
        mi += ((-1)**(num+1))/(2*num-1)
    return 4*mi

print(round(return_m(1),4))
print(round(return_m(101),4))
print(round(return_m(201),4))
print(round(return_m(301),4))
print(round(return_m(401),4))
#...
print(round(return_m(901),4))