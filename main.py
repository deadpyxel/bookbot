def count_words(string: str) -> int:
    return len(string.split())

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print(file_contents)
        print(f"Word count: {count_words(file_contents)}")

if __name__ == "__main__":
    main()
