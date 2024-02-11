def read_file_contents(filepath: str) -> str:
    with open(filepath) as f:
        return f.read()

def count_words(string: str) -> int:
    return len(string.split())

def main():
    file_contents = read_file_contents("books/frankenstein.txt")
    print(file_contents)
    print(f"Word count: {count_words(file_contents)}")

if __name__ == "__main__":
    main()
