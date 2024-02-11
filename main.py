from collections import Counter

def read_file_contents(filepath: str) -> str:
    with open(filepath) as f:
        return f.read()

def count_words(string: str) -> int:
    return len(string.split())

def count_letters(string: str) -> dict[str, int]:
    string = string.lower()
    counter = Counter(string)
    return dict(counter)

def report_book_stats(file_contents: str) -> None:
    print(f"{count_words(file_contents)} words found in the document\n")
    freq_dict = count_letters(file_contents)
    freq_dict = dict(sorted(freq_dict.items(), reverse=True, key=lambda x: x[1]))
    for ch, val in freq_dict.items():
        if not ch.isalpha():
            continue
        print(f"The '{ch}' character was found {val} times")

def main() -> int:
    filepath = "books/frankenstein.txt"
    file_contents = read_file_contents(filepath)
    print(file_contents)
    print(f"--- Begin report of {filepath} ---")
    report_book_stats(file_contents)
    print("--- End report ---")
    return 0

if __name__ == "__main__":
    exit(main())
