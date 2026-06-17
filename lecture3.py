""" where = input("You are lost in the forest. Go left or right ")
while where == "right":
    where = input("you are lost in the forest. Go left or right ")
print("Your got out of the forest! \o/")

n = int (input("Enter a non-negative integer: "))
while n > 0:
    print('x')
    n = n - 1 
# while True:
#  print("Thanks") """




"""
n = 0 
where = input("Go left or right? ")
while where == "right":
    n = n + 1
    if n > 2:
        print(":(")
    where = input("Go left or right ")
print("You go out! ")"""


"""
i  = 1, 2, 3, 4
print()

j = 1,4,2

mysum = 0
start = 3
end = 5
for i in range (start, end):
    print('i', i)
    mysum += i
    print(mysum) """



x = 4
i = 1
factorial = 1
while i <= x:
    factorial *= i
    i += 1
print(f'{x} factorial is {factorial}')