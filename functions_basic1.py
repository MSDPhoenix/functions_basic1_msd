# For each of the following code snippets, first predict the output (what you will see printed to the terminal). Once you've made a prediction, run the code snippet to see if you are correct!

#1
def a():
    return 5
print(a())

# PREDICTED OUTPUT: 5

# ACTUAL OUTPUT: 5

# PREDICTION: CORRECT


#2
def a():
    return 5
print(a()+a())

# PREDICTED OUTPUT: 10

# ACTUAL OUTPUT: 10

# PREDICTION: CORRECT


#3
def a():
    return 5
    return 10
print(a())

# PREDICTED OUTPUT: 5

# ACTUAL OUTPUT: 5

# PREDICTION: CORRECT


#4
def a():
    return 5
    print(10)
print(a())

# PREDICTED OUTPUT: 5

# ACTUAL OUTPUT: 5

# PREDICTION: CORRECT


#5
def a():
    print(5)
x = a()
print(x)

# PREDICTED OUTPUT: 5, undefined

# ACTUAL OUTPUT: 5, None

# PREDICTION: PRETTY CLOSE


#6
def a(b,c):
    print(b+c)
print(a(1,2) + a(2,3))

# PREDICTED OUTPUT: None

# ACTUAL OUTPUT: 3,5, Error

# PREDICTION: INCORRECT


#7
def a(b,c):
    return str(b)+str(c)
print(a(2,5))

# PREDICTED OUTPUT: "25"

# ACTUAL OUTPUT: 25

# PREDICTION: MOSTLY CORRECT


#8
def a():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(a())

# PREDICTED OUTPUT: 100,10

# ACTUAL OUTPUT: 100,10

# PREDICTION: CORRECT


#9
def a(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(a(2,3))
print(a(5,3))
print(a(2,3) + a(5,3))

# PREDICTED OUTPUT: 7,14,21

# ACTUAL OUTPUT: 7,14,21

# PREDICTION: CORRECT


#10
def a(b,c):
    return b+c
    return 10
print(a(3,5))

# PREDICTED OUTPUT: 8

# ACTUAL OUTPUT: 8

# PREDICTION: CORRECT


#11
b = 500
print(b)
def a():
    b = 300
    print(b)
print(b)
a()
print(b)

# PREDICTED OUTPUT: 500,500,300,500

# ACTUAL OUTPUT: 500,500,300,500

# PREDICTION: CORRECT


#12
b = 500
print(b)
def a():
    b = 300
    print(b)
    return b
print(b)
a()
print(b)

# PREDICTED OUTPUT: 500,500,300,300,500

# ACTUAL OUTPUT: 500,500,300,500

# PREDICTION: INCORRECT


#13
b = 500
print(b)
def a():
    b = 300
    print(b)
    return b
print(b)
b=a()
print(b)

# PREDICTED OUTPUT: 500,500,300,300

# ACTUAL OUTPUT: 500,500,300,300

# PREDICTION: CORRECT


#14
def a():
    print(1)
    b()
    print(2)
def b():
    print(3)
a()

# PREDICTED OUTPUT: 1, Error

# ACTUAL OUTPUT: 1,3,2 [Note: Terminal won't run this code]

# PREDICTION: INCORRECT


#15
def a():
    print(1)
    x = b()
    print(x)
    return 10
def b():
    print(3)
    return 5
y = a()
print(y)

# PREDICTED OUTPUT: 1,3,5,10

# ACTUAL OUTPUT: 1,3,5,10

# PREDICTION: CORRECT