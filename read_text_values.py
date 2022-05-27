# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    # [assignment] Add your code here
    # read the file content into a variable
    with open(filename) as f:
        read_file = f.read()
        
    return read_file
        

# print(read_file_content("story.txt"))

def count_words():
    text = read_file_content("story.txt")
    # [assignment] Add your code here
    # read file content into a string
    
    words = text.split()
    counts  = dict()
    
    # iterate through the string for len(words) times
    for word in words:
        # check occurence of a word and increment it's
        # frequency by 1 when the 'if' condition is true 
        if word in counts:
            counts[word] += 1
        # store a word in a dictionary when encoutered
        # for the first and set the 'value' to 1
        else:
            counts[word] = 1

    
    return counts



print(count_words())
