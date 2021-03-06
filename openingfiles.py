fp = open("book.txt", encoding="utf8")
# print(fp.read())
# we need to read the book, line by line. Line is a variable
character = "Tom"
sum = 0
for line in fp:
    # I am on a single line inside the iteration
    # para contar por lineas print(line.count(character))
    sum = sum + line.count(character)
print(f"The character {character} shows up {sum} times")

