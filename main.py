def main():
    file_path = 'books/frankenstein.txt'
    words = None
    characters_in_book = {}
    with open(file_path) as f:
        file_content = f.read()
        splited_content = file_content.split()
        words = len(splited_content)
        for word in splited_content:
            if word.isalpha():
                for letter in  word.lower():
                    if letter in characters_in_book:
                        characters_in_book[letter] += 1
                    else:
                        characters_in_book[letter] = 1

    print(f'--- Begin report of {file_path} ---')
    print(f'{words} words found in the document')
    print("")
    for char in characters_in_book:
        print(f"The '{char}' character was found {characters_in_book[char]} times")
    print("--- End report ---")

main()