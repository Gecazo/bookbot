def main():
    book_contents = show_contents()
    word_count = count_words(book_contents)
    print(f"Number of words: {word_count}")
    character_count = count_characters(book_contents)
    print(f"Character counts: {character_count}")

def count_words(target):
    words = target.split()
    result = len(words)
    return result

def count_characters(text):
    text = text.lower()
    char_count = {}
    for char in text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def show_contents():
    path = "books/frankenstein.txt"
    with open(path, 'r') as f:
        return f.read()

if __name__ == "__main__":
    main()

