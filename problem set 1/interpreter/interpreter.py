expression=input("Expression: ")
x = float(expression.split()[0])
y = expression.split()[1]
z = float(expression.split()[2])
if y == "+":
    cul =x+z
if y=="-":
    cul =x-z
if y=="/":
    cul =x/z
if y=="*":
    cul =x*z
print(cul)
