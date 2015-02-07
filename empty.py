
# Assigning 
(alpha, beta) = (12, 56)
print alpha
print beta 

# Swapping
(alpha, beta) = (beta, alpha)
print alpha
print beta




'''
Exercise: input file output number of lines, words, and characters
'''

def file_info(infile):
    lines = list(infile)
    n_lines = 0
    n_words = 0
    n_chars = 0
    
    for elem in lines:
        n_lines += 1
        n_chars += len(elem)
        n_words += len(elem.split())
        
    return (n_lines, n_words, n_chars)

infile = open("read.txt","r")
print file_info(infile)


