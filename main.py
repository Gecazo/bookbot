def main():
    print(count_words(show_contents()))

def count_words(target):
    words = target.split()
    result = len(words)
    return result

def show_contents():
    path = "books/frankenstein.txt"
    with open(path, 'r') as f:
        return f.read()

if __name__ == "__main__":
    main()
