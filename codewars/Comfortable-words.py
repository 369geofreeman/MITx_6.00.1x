# Comfortable words

# A comfortable word is a word which you can type always alternating the hand you type with (assuming you type using a QWERTY keyboard and use fingers as shown in the image below).
# 
# That being said, create a function which receives a word and returns true/True if it's a comfortable word and false/False otherwise.
# 
# The word will always be a string consisting of only ascii letters from a to z.
# 
# 
# 
# To avoid problems with image availability, here's the lists of letters for each hand:
# 
# Left: q, w, e, r, t, a, s, d, f, g, z, x, c, v, b
# Right: y, u, i, o, p, h, j, k, l, n, m



def comfortable_word(word):
    l=['q', 'w', 'e', 'r', 't', 'a', 's', 'd', 'f', 'g', 'z', 'x', 'c', 'v', 'b']
    r=['y', 'u', 'i', 'o', 'p', 'h', 'j', 'k', 'l', 'n', 'm']
    if word[0] in r:
        for i,v in enumerate(word):
            if i%2==0 and v not in r: return False
            if i%2>0 and v not in l: return False
    else:
        for i,v in enumerate(word):
            if i%2==0 and v not in l: return False
            if i%2>0 and v not in r: return False
    return True


print(comfortable_word('yams'))
# >>> True
print(comfortable_word('their'))
# >>> True
print(comfortable_word('test'))
# >>> False
