"""Python functions for JavaScript Trials 1."""


def output_all_items(items):
    for item in items:
        print(item)


def get_all_evens(nums):
    lst = []
    for num in nums:
        if num % 2 == 0:
            lst.append(num)
    return lst


def get_odd_indices(items):
    """
    >>> get_odd_indices([1, 'hello', True, 500])
    ['hello', 500]
    """
    lst = []
    for i in range(len(items)):
        if i % 2 == 1:
            lst.append(items[i])
    return lst


def print_as_numbered_list(items):
    i = 1

    for item in items:
        print(f'{i}. {item}')
        i += 1
        

def get_range(start, stop):
    """
    >>> get_range(0, 5);
    [0, 1, 2, 3, 4]
    """
    nums = []

    # init: let num = start
    num = start

    # while: num < stop 
    while num < stop:
        # action
        nums.append(num)

        # increment: num += 1 
        num += 1
    
    return nums


def censor_vowels(word):
    chars = []

    for letter in word:
        if letter in 'aeiou':
            chars.append('*')
        else:
            chars.append(letter)
    return ''.join(chars)


def snake_to_camel(string):
    """
    CamelCase according to trials.js <-- we're doing this
    camelCase according to wikipedia

    >>> snake_to_camel('hello_world')
    'HelloWorld'
    """
    camel_case = []

    for word in string.split('_'):
        camel_case.append(f"{word.title()}")
    
    return ''.join(camel_case)


def longest_word_length(words):
    longest = len(words[0])

    for word in words:
        if longest < len(word):
            longest = len(word)
    
    return longest    


def truncate(string):
    """Truncate repeating characters into one character.
    >>> truncate('aaaabbbbcccca')
    'abca'
    
    """
    result = []
    for char in string:
        if len(result) == 0 or char != result[-1]:
            result.append(char)
    return ''.join(result)
    

def has_balanced_parens(string):
    parens = 0

    for char in string:
        if char == '(':
            parens += 1
        elif char == ')':
            parens -= 1
            if parens < 0:
                return False

    return parens == 0


def compress(string):
    """
    >>> compress('aabbaabb')
    'a2b2a2b2'
    >>> compress('abc')
    'abc'
    """
    compressed = []

    curr_char = ''
    char_count = 0

    for char in string:
        if char != curr_char:
            compressed.append(curr_char)
            if char_count > 1:
                compressed.append(str(char_count))
            curr_char = char
            char_count = 0
        char_count += 1
    
    compressed.append(curr_char)
    if char_count > 1:
        compressed.append(str(char_count))
    return ''.join(compressed)
