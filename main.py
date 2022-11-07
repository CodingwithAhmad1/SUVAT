# program to solve suvat questions
print("Only enter answers in lower case ")
print(" ")
SUVAT = input(
    "Enter any suvat letters that you have the value of: ")

test_1 = "v = u + at"
test_2 = "v = u + 2as"  # you don't have to include powers at this stage
test_3 = "s = u + 1/2(at)"  # displacement with positive accelaration
test_4 = "s = 1/2(v+u)t"  # displacement knowing intial and final velocity


if "s" in SUVAT:
    s = 'defined'
    s_val = int(input("What is the value for s: "))
    include = "s"
else:
    s = 'undefined'

if "u" in SUVAT:
    u = 'defined'
    u_val = int(input("What is the value for u: "))
    include = include + "u"
else:
    u = 'undefined'

if "v" in SUVAT:
    v = 'defined'
    v_val = int(input("What is the value for v: "))
    include = include + "v"
else:
    v_helper = input(
        "Does the projectile 'stop' moving at a certain point(ground) or is it still moving? ")
    if
    v = 'undefined'

if "a" in SUVAT:
    a = 'defined'
    a_val = int(input("What is the value for a: "))
    include = include + "a"
else:
    if "a" not in SUVAT:
        a_helper = input(
            "Is the projectile going 'up', 'down' or 'horizontal': ")

    if ("up" in a_helper) or ("hor" in a_helper):
        a = 9.81
    else:
        a = -9.81

if "t" in SUVAT:
    t = 'defined'
    t_val = int(input("What is the value for t: "))
    include = include + "t"
else:
    t = 'undefined'

t = len(include)
if t == 1:
    print("Not enough information")
