def revst(s):
        i = 0
        j = len(s)-1
        
        while i < len(s)//2:
            print(s)
            temp = s[i]
            s[i] = s[j]
            s[j] = temp
            i += 1
            j -= 1


x = ['h','e','l','l','o']

revst(x)

print(x)
