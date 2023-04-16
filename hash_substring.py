# python3

def read_input():
    # Function checks if input is from keyboard (I) or from a file (F)
    # Then prompts two inputs - first line is the pattern, the second line is the text
    # Returns both of those inputs to the get_occurrences function
    input_method = input()

    if input_method.__contains__("I"):
        pattern = input()
        text = input()
    
    elif input_method.__contains__("F"):
        try:
            with open("tests/06","r") as f:
                pattern = f.readline()
                text = f.readline()
        except FileNotFoundError:
            return

    else:
        print("Input error")
        return
    
    return (pattern.rstrip(), text.rstrip())

def print_occurrences(output):
    # this function should control output, it doesn't need any return
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    # this function should find the occurances using Rabin Karp alghoritm 
    prime_number = 101
    pattern_length = len(pattern)
    text_length = len(text)
    pattern_hash = sum(ord(pattern[i]) * 26**i for i in range(pattern_length)) % prime_number
    segment_hash = sum(ord(text[i]) * 26**i for i in range(pattern_length)) % prime_number
    h = 26 ** (pattern_length - 1) % prime_number
    occurrences = []

    for i in range(text_length - pattern_length +1):
        if pattern_hash == segment_hash:
            if pattern == text[i:i+pattern_length]:
                occurrences.append(i)
        if i < text_length - pattern_length:
            segment_hash = (segment_hash - ord(text[i]) * h) % prime_number
            segment_hash = (segment_hash * 26 + ord(text[i+pattern_length])) % prime_number
            segment_hash = (segment_hash + prime_number) % prime_number

    # and return an iterable variable
    return (occurrences)


# Launches the code
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

