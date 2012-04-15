Problem A Analysis
------------------

In most Google Code Jam problems, each test case is completely separate and nothing you learn from one will be useful in another. This problem was different however:

_"Googlerese is based on the best possible replacement mapping, and we will never change it. It will always be the same. In every test case."_

We meant it when we said this! There really is just one mapping, and the main challenge here is figuring out what it is. Fortunately, there is a lot we can learn from the sample input and output. For example, by looking at the first word in the first line, we know that "our" becomes "ejp" in Googlerese, so 'o' -> 'e', 'u' -> 'j', and 'r' -> 'p'. If you go through the entire text, you will that there is almost enough information to reconstruct the entire mapping:

    'a' -> 'y'
    'b' -> 'n'
    'c' -> 'f'
    'd' -> 'i'
    'e' -> 'c'
    'f' -> 'w'
    'g' -> 'l'
    'h' -> 'b'
    'i' -> 'k'
    'j' -> 'u'
    'k' -> 'o'
    'l' -> 'm'
    'm' -> 'x'
    'n' -> 's'
    'o' -> 'e'
    'p' -> 'v'
    'q' -> ???
    'r' -> 'p'
    's' -> 'd'
    't' -> 'r'
    'u' -> 'j'
    'v' -> 'g'
    'w' -> 't'
    'x' -> 'h'
    'y' -> 'a'
    'z' -> ???

We just need to figure out how to translate 'q' and 'z'. But if you read the problem statement carefully, you will notice there was one more example we gave you! "a zoo" gets translated to "y qee". This means that 'z' gets mapped to 'q'.

Next we have to figure out what 'q' gets mapped to. For this part, you need to remember that every letter gets mapped to something different. And if you look carefully, there is already a letter getting mapped to everything except for 'z'. This leaves only one possibity: 'q' must get mapped to 'z'.

And now we have the full translation mapping, and all we need to do is write a program to apply it to a bunch of text. Here is a solution in Python:

```
translate_to_english = {
    ' ': ' ', 'a': 'y', 'b': 'h', 'c': 'e', 'd': 's',
    'e': 'o', 'f': 'c', 'g': 'v', 'h': 'x', 'i': 'd',
    'j': 'u', 'k': 'i', 'l': 'g', 'm': 'l', 'n': 'b',
    'o': 'k', 'p': 'r', 'q': 'z', 'r': 't', 's': 'n',
    't': 'w', 'u': 'j', 'v': 'p', 'w': 'f', 'x': 'm',
    'y': 'a', 'z': 'q'}

for tc in xrange(1, int(raw_input()) + 1):
  english = ''.join(
      [translate_to_english[ch] for ch in raw_input()])
  print 'Case #%d: %s' % (tc, english)
```

