class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        a=set(secret)
        b=set(guess)
        l=[0]*10
        m=[0]*10
        for i in range(len(guess)):
            if secret[i]==guess[i]:
                l[int(secret[i])]+=1
        c=sum(l)
        for i in range(10):
            m[i]=min(secret.count(str(i)),guess.count(str(i)))-l[i]
        d=sum(m)
        return str(c)+"A"+str(d)+"B"