# strings and tests
# the lines right here use % as type of substitution with the proper letters
x = "There are %d types of animals" % 10
binary = "binary"
doNot = "please don't"
y = "Those who are familiar with %s and those who %s" % (binary, doNot)

print(x)
print(y)

# These require and use quotations and sentences
print("He said: %r.:" % x)
print("He also said: '%s'. " % y)

# another way of more substitution to make it cleaner and more efficient when printing
hilarious = False
jokeOutcome = "Isn't the joke really funny? %r"
print(jokeOutcome % hilarious)

# We will now be adding strings together
a = "Jack and Jill went up the hill..."
b = "to fetch a pale of water"
print(a+b)

# Another example of printing and adding useless crap together
c = "1 + 2 + 3 + 4 + 5 --->"
# I will  be solving this math problem for you
d = "3 + 3 + 4 + 5 --->"
e = "6 + 4 + 5 --->"
f = "10 + 5 --->"
g = "15"
# Wow I just solved a math problem on Python
print(c+d)
print(d+e)
print(e+f)
print(f+g)
print(g)
# Omg we just solved a math problem im so proud of myself

# Lets put strings together to write a poem
a = "Roses are red"
b = "Violets are blue"
c = "I like poodles"
d = "And so should you"
print(a)
print(b)
print(c)
print(d)
# Yay we created a poem using strings