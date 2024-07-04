def main():
    book_contents = show_contents()
    word_count = count_words(book_contents)
    character_count = count_characters(book_contents)
    print_report(word_count, character_count, "books/frankenstein.txt")

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

def print_report(word_count, character_count, file_path):
    report = []
    report.append(f"--- Begin report of {file_path} ---")
    report.append(f"{word_count} words found in the document\n")
    
    sorted_characters = sorted(character_count.items(), key=lambda item: item[1], reverse=True)
    for char, count in sorted_characters:
        if char.isalpha():
            report.append(f"The '{char}' character was found {count} times")
    
    report.append("--- End report ---")
    print("\n".join(report))

if __name__ == "__main__":
    main()
