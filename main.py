from collections import Counter

def read_file_contents(filepath: str) -> str:
    """Reads file contents and returns it as a single string

    Args:
        filepath (str): path of the file to open

    Returns:
        str: file contents as string, with no trimming or striping of characters
    """    
    with open(filepath) as f:
        return f.read()

def count_words(string: str) -> int:
    """Counts the number of words, split by space on the file contents

    Args:
        string (str): string representation of file contents

    Returns:
        int: number of words in the file
    """    
    return len(string.split())

def count_letters(string: str) -> dict[str, int]:
    """Counts character frequencies on a string and returns it and returns it as a dictionary

    Args:
        string (str): target for character counting

    Returns:
        dict[str, int]: dictionary where each key is a lowercase character, 
            and each value is the number of ocurrences
    """    
    # converts everything to lowercase
    string = string.lower()
    # create a Counter object that does the processing
    counter = Counter(string)
    return dict(counter)  # convert counter object to dictionary

def report_book_stats(file_contents: str) -> None:
    """Reports book stats

    Args:
        file_contents (str): contents of the file, as a single string
    """    
    print(f"{count_words(file_contents)} words found in the document\n")
    freq_dict = count_letters(file_contents)
    # sort dictionary contents, using a lambda function to sort by value
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
