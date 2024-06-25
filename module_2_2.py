first = 531
second = 950
third = 173

if first == second == third:
    print(3)
elif first == second or first == third or second == third:
    print(2)
elif first != second and third:
    print(0)