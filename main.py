import sys
def sort_on(dict):
    return dict["num"]
def main() -> int:
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    words = file_contents.split()
    print(f"Number of total words: {len(words)}")
    file_contents_lower = file_contents.lower()

    alphabet = "abcdefghijklmnopqrstuvwxyz "
    letter_counts = {letter: 0 for letter in alphabet}
    for letter in file_contents_lower:
        if letter in letter_counts:
            letter_counts[letter] += 1

    list_of_counts = []
    for k, v in letter_counts.items():
        list_of_counts.append({'char': k, 'num': v})
    list_of_counts.sort(reverse=True, key=sort_on)

    #code to go through each letter in the alphabet and print f"you have {x} counts of the letter {letter} in the text"
    for item in list_of_counts:
        char = item['char']
        num = item['num']
        description = "spaces" if char == " " else f"the letter '{char}'"
        print(f"You have {num} counts of {description} in the text.")

    

if __name__ == '__main__':
    sys.exit(main()) 