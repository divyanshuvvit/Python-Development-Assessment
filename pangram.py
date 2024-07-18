def fun(s):
    li =[0]*26
    for x in s:
        li[ord(x) - ord('a')] = li[ord(x) - ord('a')]+1
    ans = True
    for i in range(0,26):
        if li[i]==0:
            ans=False
            break
    return ans

s = "abcdefghijklmnopqrstuvwxyzab"
temp = fun(s)
if(temp):
    print("Pangram")
else:
    print("Not Pangram")