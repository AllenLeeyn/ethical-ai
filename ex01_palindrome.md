### Exercise 1: The Palindrome Challenge

**Objective:** Experience the difference between using AI as a shortcut and using it as a learning tool.

#### Step 1 - Do it yourself

1. Write pseudocode for a function that checks if a string is a palindrome.
```
fn is_palindrome(string) -> bool {
    string.to_lowercase()
    string.remove_non_alphabetic()

    look at characters from start and end moving to center
    if characters don't match return false
    else true
}
```

2. Implement your solution in Python.
```python
# is_palindrome.py

# takes a string input and returns a boolean
def is_palindrome(s: str) -> bool:

    # Normalize the string: lowercase and remove non-alphanumeric characters
    s = str.lower(s)
    s = ''.join(c for c in s if c.isalnum())

    # the idea is to look at each ends and move to the center at each iteration
    start, end = 0, len(s) - 1

    while start < end:
        # compare the characters at each iteration
        if s[start] != s[end]:
            # if they don't match, it's not a palindrome
            return False
        start += 1
        end -= 1
    
    # if we reach here, all characters matched
    return True
```

3. Test with examples like `"racecar"`, `"hello"`, and `"A man a plan a canal Panama"`.
`python3 .\is_palindrome.py`

4. Add comments explaining your reasoning.

#### Step 2 - Use AI to learn

Now that your function works, use AI to go deeper:

```text
"I wrote a palindrome function. Here's my code:
[insert your code]

What's the time complexity?
What edge cases might I miss?
Are there better approaches?"
```

#### Step 3 - Reflection

- What did you learn from solving it before asking AI?
```
I learned the different steps to reach the desired outcome.
Understanding what is the requirement (what is palindrome) and how we can breakdown the problem into smaller steps (normalization, effective comparison).

By understaning the definition of palindrome, we understand what kind of normalization is needed.

I was thinking of reversing the string and comparing it to the original string after normalization. But the current approach is more efficient
```

- How is your understanding different now?
```
It is good I think...
We have attempted this problem in the checkpoint exercise before. So I have some idea of how to tackle it.
Even though the programming language is different, the logic and concepts are the same.
```

- Could you now write similar functions (e.g., reverse a string) without help?
```python
#Yeah, I hope to think I can.
def reverse_string(s: str) -> str:
    s = list(s)
    start, end = 0, len(s) - 1

    while start < end:
        cur = s[start]
        s[start] = s[end]
        s[end] = cur
        start += 1
        end -= 1
    return s.join('')
```
