"""Python functions for JavaScript Trials 1."""


def output_all_items(items):
    # TODO: replace this line with your code
    for item in items:
        print(item)

def get_all_evens(nums):
    # TODO: replace this line with your code
    evennums = []
    for num in nums:
        if num % 2 == 0:
            evennums.append(num)
    return evennums




# // Given an array of numbers, return an array of all even numbers.
# //
# // Ex.:
# //   > getAllEvens([7, 8, 10, 1, 2, 2]);
# //   [8, 10, 2, 2]
# function getAllEvens(nums) {
#   const evenNums = [];

#   for (const num of nums) {
#     if (num % 2 === 0) {
#       evenNums.push(num);
#     }
#   }

#   return evenNums;
# }

def get_odd_indices(items):
    '''doc string'''
    result = []
    for i in len(range(items)):
        if i % 2 != 0:
            result.append(items[i])
    return result

def print_as_numbered_list(items):
    # TODO: replace this line with your code
    i = 1
    for item in items:
        print(f'{i}. {item}')
        i+=1
        
        


# // Given an array, output a numbered list.
# //
# // Ex.:
# // > printAsNumberedList([1, 'hello', true]);
# // 1. 1
# // 2. hello
# // 3. true
# function printAsNumberedList(items) {
#   let i = 1;

#   for (const item of items) {
#     console.log(`${i}. ${item}`);

#     i += 1;
#   }
# }

def get_range(start, stop):
    # TODO: replace this line with your code
    nums = []

    for num in range(start, stop):
        nums.append(num)
        num += 1
    return nums


def censor_vowels(word):
    # TODO: replace this line with your code
    chars = []
    for letter in word:
        if letter in 'aeiou':
            chars.append("*")
        else:
            chars.append(letter)
    return "".join(chars)
# // Given a string, return a string where vowels are replaced with '*'.
# //
# // Ex.:
# //   > censorVowels('hello world');
# //   'h*ll* w*rld'
# function censorVowels(word) {
#   const chars = [];

#   for (const letter of word) {
#     if ('aeiou'.includes(letter)) {
#       chars.push('*');
#     } else {
#       chars.push(letter);
#     }
#   }

#   return chars.join('');
# }

def snake_to_camel(string):
    # TODO: replace this line with your code
    camel_case = []

    for word in string.split('_'):
        camel_case.append(f'{word[0].capitalize()}{word[1:]}')
    return "".join(camel_case)

# (`${word[0].toUpperCase()}${word.slice(1)}`)

def longest_word_length(words):
    # TODO: replace this line with your code
    longest = len(words[0])
    for word in words:
        if longest < len(word):
            longest = len(word)
    return longest

    
# // Return the length of the longest word in the given array of words.
# //
# // Ex.:
# //   > longestWordLength(['hello', 'world']);
# //   5
# //
# //   > longestWordLength(['jellyfish', 'zebra']);
# //   9
# function longestWordLength(words) {
#   let longest = words[0].length;

#   for (const word of words) {
#     if (longest < word.length) {
#       longest = word.length;
#     }
#   }

#   return longest;
# }


def truncate(string):
    pass  # TODO: replace this line with your code


def has_balanced_parens(string):
    pass  # TODO: replace this line with your code


def compress(string):
    pass  # TODO: replace this line with your code
