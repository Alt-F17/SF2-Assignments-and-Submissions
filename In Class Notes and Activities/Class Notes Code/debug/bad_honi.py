# '''
# HONI block

# Consider a series of four consecutive letters of some word that make up the 
# subword HONI (case sensitive) is called the HONI-block. 

# Given a string by the user, throw out as many letters as you want (it might be
# none), so that in the end there are as many HONI-blocks as possible in the word.  

# upgrade to: 
# --> where HONI-block is not case sensitive.  
# --> let user provide any sub-block
# '''


# Solution 1:

word = input('enter string: ') 
sub_block = 'HONI'              
block_count = 0 
index = 0
current_letter = ''

while index < len(word):
    for letter in sub_block:
        if word[index] == letter:
            current_letter += word[index]
            if current_letter == sub_block:
                block_count += 1
                current_letter = ''
    index += 1
print(f'number of HONI-blocks: {block_count}')


# Solution 2:

word = input('enter string: ') 
sub_block = 'HONI'              
block_count = 0 
i = j = 0  

while i < len(word):
    if word[i] == sub_block[j]:   
        if j!= len(sub_block):    
            j = j + 1               
        else:                 
            block_count = block_count + 1
            j = 0
    i = i + 1              
print(f'number of HONI-blocks: {block_count}')