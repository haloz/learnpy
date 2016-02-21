words = ["one", "two", "three", "four"]

# no i
for w in words:
    print(w)

# iterate with i if we need the index
for i in range(len(words)):
    print(i, words[i])

# simpler with enumerate
for i, v in enumerate(words):
    print(i, v)

