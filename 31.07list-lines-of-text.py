from os import system


text_lines = [
    'Python is a high-level, interpreted, general-purpose programming' ,
    'language. Its design philosophy emphasizes code readability with the use' ,
    'of significant indentation.'
]


system ('cls')

text_lines.append(input("Add line: "))
text_lines.append(input("Add line again: "))

system ('cls')

print()
for i in range(len(text_lines)):
    print(i,text_lines[i])

print()