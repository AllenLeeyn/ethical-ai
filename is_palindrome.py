# takes a string input and returns position or 1 if palindrome
def is_palindrome(s: str) -> int:

    # Normalize the string: lowercase and remove non-alphanumeric characters
    s = str.lower(s)
    s = ''.join(c for c in s if c.isalnum())

    # the idea is to look at each ends and move to the center at each iteration
    start, end = 0, len(s) - 1

    while start < end:
        # compare the characters at each iteration
        if s[start] != s[end]:
            # if they don't match, it's not a palindrome
            return end
        start += 1
        end -= 1
    
    # if we reach here, all characters matched
    return 1

print(is_palindrome("racecar"))
print(is_palindrome("hello"))
print(is_palindrome("A man a plan a canal Panama"))

def reverse_string(s: str) -> str:
    s = list(s)
    start, end = 0, len(s) - 1

    while start < end:
        cur = s[start]
        s[start] = s[end]
        s[end] = cur
        start += 1
        end -= 1
    return ''.join(s)

print(reverse_string("hello"))