from pip._vendor.distlib.compat import raw_input

from clock import ping

# cheatsheet
# https://medium.com/nestedif/cheatsheet-python-for-java-developers-98f75c94a1a
# https://www.python.org/dev/peps/pep-0008/

message1 = "1. Hello World! This message does not use semicolon at the end!"
print(message1)

print("\n2. Testing out if statements")
value = 0
if 0 == value:
    print("Number is zero!")
# elif ... :
else:
    print("Message is not zero!")

print("\n3. Variables and Data Types")
number = 11
string = "This is a string!"
a, b, c, d = True, False, 1, "Good!"

if a:
    print("a is true!")

if not b:
    print("b is false!")

print(c)
print(d)

print("\n4. Value Assignment")
x = 300
x = y = "1"
print("x is formerly 300 in number, but it's now %s in string" % x)

print("\n5. Strings")
message = """you can create something like this yo!
believe it or not, this is all in one single string!"""

print(message)

print("\n6. List")
sample_list = [1, 2, 3, 4]
print(sample_list)

sample_list.append(1)
print(sample_list)

print("item on index 3 is %s" % sample_list[3])
print("list length is %s" % len(sample_list))

print("cloning needs to use list[:], since = copies reference")
list2 = sample_list
list3 = sample_list[:]
sample_list.append(2)
print("current sample list after appending the number 2: %s" % sample_list)
print("list created using = is %s" % list2)
print("list created using clone is %s" % list3)

print("\n7. Tuples")
tuple1 = (1, 2, 'Sprite')
print("tuple index 1 is %s" % tuple1[1])
print("tuple index 2 is %s" % tuple1[2])

print("\n8. Dictionary")
print("it does have to be Key: String, and Value: number! It can be anything.")
room_num = {'john': 121, 'tom': 307}
guest_names = ["john", "tom"]

for name in guest_names:
    print("%s's room is %s" % (name, room_num[name]))

print("\n9. Operators")
print("20 ** 2 is %s" % 20 ** 2)
print("20 %% 2 is %s" % (20 % 2))

print("\n10. For Loops")
for x in range(0, 3):
    print("This is loop %s!" % x)

for y in range(0, 6, 2):
    print("Increment this by 2! = %s" % y)

print("Launching in:")
for y in range(3, 0, -1):
    print(y)
print("Lift off!")

print("\n11. While Loops")
var1 = 3
while var1 < 20:
    var1 = var1 * 2
    print(var1)
print("Exit loop.")

while True:
    n = raw_input("Please enter `hello`: ")
    if n.strip() == 'hello':
        break
    else:
        print("NO DAS NOT HELLO! ")

print("\n12. Iterations")
print("iteration can be done on lists, tuples, and dictionaries")
friends = ['Among', 'Akiao', 'Aleng']
for friend in friends:
    print(friend)

tup = ('alpha', "bravo", "charlie")
for val in tup:
    print(val)

codes = {'INDIA': 'in',
         'USA': 'us',
         'UK': 'gb'}
for key in codes:
    print(key, 'corresponds to', codes[key])

for key, value in codes.items():  # Python 3
    print(key, 'corresponds to', codes[key])
