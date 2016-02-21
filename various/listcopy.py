# this makes an infinite loop ...
words = ["one", "two", "three", "four"]
print(words)
for w in words:
    if len(words) < 8:
        words.append("ex")
print(words)

# but this not as we iterate over a slice copy of the words list
words = ["one", "two", "three", "four"]
print(words)
for w in words[:]:
    words.append("ex")
print(words)
