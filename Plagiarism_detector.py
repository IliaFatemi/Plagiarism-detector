'''
Program purpose: This program takes two files as input and returns the similarity between the two. This can be determined to see if a text is plagarized.

Author: Ilia Fatemi

Date created: 2019-11-13

Date modified: 2019-11-14
'''


#File input 
def read_file(file_input):
    '''Reading a text file and returning the content of the document as a string.'''
    with open(file_input, 'r') as text_file:
        return text_file.read()


#Shingling a string 
def shingling_string(sentence, shingle_size):
    '''
    Taking a string and a shingle size as input and returning a set of a list that contains 
    differs characters.
    '''
    shingles = []
    for char in range(len(sentence) - shingle_size + 1):
        shingles.append(sentence[char:char + shingle_size].translate({ord('\n'):None}).translate({ord(' '):None}))
    return set(shingles)


#Jacquards similarity of two sets of different lists
def Jacquards_similarity(shingle_A, shingle_B):
    '''Taking two different sets of shingles and returning a percentage of they're similarities.'''
    return len(shingle_A.intersection(shingle_B))/len(shingle_A.union(shingle_B))


def main():
    '''
    Text files located in directory: 
    
    "blues_medal_capilanou.txt", "rents_cbc.ca_nov_28_changed.txt", "rents_cbc.ca_nov_28.txt
    '''

    file_input1 = input("Enter the first text file (with .txt at the end): ")
    file_input2 = input("Enter the second text file (with .txt at the end): ")
    shingle_size = int(input("Enter a shingle size: "))

    A = shingling_string(read_file(file_input1), shingle_size)
    B = shingling_string(read_file(file_input2), shingle_size)
    print("\nThe files are {} percent similar.".format(round(Jacquards_similarity(A, B)*100, 2)))
main()