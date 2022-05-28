# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    # [assignment] Add your code here 
    read_file = open(filename,"r")
    details = str(read_file.read())
    print(details)
    return details
    # print(details)
    # read_file.close()


def count_words():
    text = read_file_content("story.txt")
    # [assignment] Add your code here
    file_dic = dict()
    new_l = text.split()
    for w in new_l:
        if w in file_dic:
            file_dic[w] += 1
        else:
            file_dic[w] = 1
    
    return file_dic
    # return {"as": 10, "would": 20}


print(count_words())