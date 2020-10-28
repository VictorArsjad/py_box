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


