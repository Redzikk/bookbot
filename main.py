content_dictionary= {}
title = "--- Begin report of books/frankenstein.txt ---"
count_chars = 0
with open('./books/frankenstein.txt', 'r') as file:
    file_contents = file.read().lower()
    count_chars = len(file_contents.split())
    for letter in file_contents.lower().replace(' ', ''):
        if letter.isalpha():
            if letter in content_dictionary:
                content_dictionary[letter] += 1
            else:
                content_dictionary[letter] = 1

def compare_by_value(item):
    return item[1]
sorted_content = sorted(list(content_dictionary.items()), key=compare_by_value, reverse=True)


print(title)
print(f"{count_chars} words found in the document")

for item in sorted_content:
    print(f"The '{item[0]}' character was found {item[1]} times")

print('--- End report ---')

