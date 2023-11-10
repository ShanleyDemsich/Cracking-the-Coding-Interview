def is_unique(string):
    """Implement an algorithm to determine if a string has all unique characters
    What if you cannot use additional data structures?"""
    alpha_dict = dict()
    for char in string.lower():
        if char in alpha_dict:
            return False
        alpha_dict[char] = 1
    return True


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(is_unique('abcdefghijklmnopqrstuvwxyz'))
    print(is_unique('abcdfffghh'))
