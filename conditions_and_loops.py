test=2
test2=1

#if 
if test != test2:
    print("test not equal test2")

#if-else
if test == test2:
    print("test not equal test2")
else:
    print("test equal test2")

#if-elif-else
if test == test2:
    print("test not equal test2")
elif test >= test2:
    print("test is greater then test2")
else:
    print("test equal test2")


word="test"
#for loop
for characters in word:
    print("test")

#while
while test >= test2:
    print("test is greater then test2")
    test2+=1

#do-while
number=0

while True:
    print(number)
    number+=1
    if not number <=10:
        break

#range 

for x in range(10):
    print("i'm ready to go!")