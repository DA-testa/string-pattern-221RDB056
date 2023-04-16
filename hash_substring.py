# python3

def read_input():
    # this function needs to aquire input both from keyboard and file
    # as before, use capital i (input from keyboard) and capital f (input from file) to choose which input type will follow
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
    # after input type choice
    # read two lines 
    # first line is pattern 
    # second line is text in which to look for pattern 
    
    # return both lines in one return
    
    # this is the sample return, notice the rstrip function
    return (pattern.rstrip(), text.rstrip())

def print_occurrences(output):
    # this function should control output, it doesn't need any return
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    # this function should find the occurances using Rabin Karp alghoritm 

    # and return an iterable variable
    return (pattern,text)


# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

