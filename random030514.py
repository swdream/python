import random

languages = ['C', 'HTML', 'java', 'python', 'android']

for i in range(5):
    # random.randint(a, b)
    # return a integer N : a<N<b
    print languages[random.randint(0,4)]

# random.choice(seq)
# return a random element from a non-empty sequence seq. if seq is empty, raise IndexError
print random.choice(languages)

#  random.shuffle(x[, random])
# Shuffle the sequence x in place
print random.shuffle(languages)

# random.sample(seq, n)
# return a new sequence has n elements; n < len(seq)
print random.sample(languages, 3)