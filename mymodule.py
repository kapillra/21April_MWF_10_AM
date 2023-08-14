# simple print
print('hello')

# check the module name
print(__name__)

# importing another module
import calculator

print(dir(calculator))

print(calculator.__name__)


print(calculator.add.__doc__)

r = calculator.add(5,9,8,7,9,6,5,4,1)

print(r)

from calculator import add

print(add(5,9,6))

from calculator import add as summation

print(summation(6,4,6))