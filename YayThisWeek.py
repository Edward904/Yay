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

# another way of more substitution to make it cleaner and more efficient when printing
funny = false
jokeOutcome = "Isn't the joke really funny? %r"
print(jokeOutcome % funny)

# We will now be adding strings together
a = "Jack and Jill went up the hill..."
b = "to fetch a pale of water"
print(a+b)

# Another example of printing and adding useless crap together
c = "1 + 2 + 3 + 4 + 5"
# I will  be solving this math problem for you