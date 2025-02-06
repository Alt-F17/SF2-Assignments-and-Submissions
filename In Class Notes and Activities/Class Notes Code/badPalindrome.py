from loguru import logger

def isPalindrome (lst):
    '''
    return True if the list forms a palindrome; False otherwise
    :param lst: list
    :return: bool
    '''
    temp = lst[:]
    temp.reverse()
    print(temp, lst)
    return temp == lst

def silly(n):
    '''
    get n inputs from the user. Print 'yes' if the sequence of inputs froms a palindrome; no otherwise
    :param n: int > 0
    :return: None
    '''
    result = []
    for i in range(n):
        element = input('enter element: ')
        result.append(element)
    if isPalindrome(result):
        print('yes')
    else:
        print('no')

silly(2)

