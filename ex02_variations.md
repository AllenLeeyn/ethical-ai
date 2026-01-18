### Exercise 2: Strengthening Through Variations

**Objective:** Extend your solution and practice independent problem-solving.

1. Modify your palindrome function to:
   - Ignore spaces and punctuation.
   - Be case-insensitive.
   - Return the position where the string stops being a palindrome (if not one).
```python
# is_palindrome.py

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
```

2. After your first attempt, ask AI:

```text
"I modified my palindrome function to handle more cases.
Did I miss anything? Can it be more efficient?"
```

```text
Your solution is **correct**, readable, and already efficient in Big-O terms. You didn’t miss any required case from the prompt. That said, there are **two small improvements** worth noting—one about **efficiency**, one about **API clarity**.

---

## ✅ What you handled correctly

✔ Ignoring spaces and punctuation
✔ Case-insensitive comparison
✔ Two-pointer approach (optimal)
✔ Early exit on first mismatch

Time complexity is **O(n)** and space complexity is **O(n)** — perfectly acceptable.

---

## ⚠️ Minor issues / improvements

### 1. Efficiency: avoid building a new string (optional)

Right now, you:

`
s = ''.join(c for c in s if c.isalnum())
`

This creates a **new string**, costing extra memory.

You can instead skip non-alphanumeric characters **in place** while scanning from both ends. This keeps:

* **Time:** O(n)
* **Space:** O(1) (better)

#### More efficient version (same behavior)

`python
def is_palindrome(s: str) -> int:
    s = s.lower()
    start, end = 0, len(s) - 1

    while start < end:
        while start < end and not s[start].isalnum():
            start += 1
        while start < end and not s[end].isalnum():
            end -= 1

        if s[start] != s[end]:
            return start  # first position where symmetry breaks

        start += 1
        end -= 1

    return 1
`

---

### 2. Return value semantics (clarity issue)

Returning `1` for “palindrome” is **non-idiomatic** in Python and may confuse readers.

More common choices:

* `-1` → no mismatch
* `None` → no mismatch
* `True / False` (plus index if false)

If you must follow the assignment spec, your current return value is fine — just **document it clearly**.

---

## 🎯 Final assessment

**Did you miss anything?**
No — all requirements are met.

**Can it be more efficient?**
Yes, slightly:

* Avoid building a normalized string
* Skip punctuation during comparison

Your current version is absolutely acceptable for coursework. The optimized version is what you’d expect in a technical interview or production code.

If you want, I can:

* Refactor it to return original-string indices
* Add unit tests
* Convert it to a boolean + index API
* Compare both versions side-by-side

Just say the word.

```

3. Reflect on what AI added that you didn't consider initially.
```
I did find the requirement to return 1 for valid case odd. After the review by the AI, I am considering it might be a typo. Conventionally, returning -1 might make more sense.
I didn't consider how some of the functions will create new strings and increase the memory used. It is interesting to learn how we can optimize further.
```
