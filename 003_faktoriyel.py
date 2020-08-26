"""
5! = 1*2*3*4*5
kaç faktöriyel : 5!
integer
5! = 120
"""
f = 1
sayi = int(input("Kaç faktöriyel:"))
for i in range(1, sayi + 1):
    f = f * i

print("{}!= {}".format(sayi, f))
