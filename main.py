num1 = input('num 1-> ')
num2 = input('num 2-> ')
choice = input("1=Prosthesi: ,2=afairesi: ")


if choice == '1':
    print(float(num1) + float(num2))
elif choice == '2':
    print(float(num1) - float(num2))
else:
    print('Not supported.')