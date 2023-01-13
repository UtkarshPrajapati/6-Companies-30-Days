class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        d,ans=collections.defaultdict(list),0
        for w in words: d[w[0]].append(w)
        for c in s:
            cur=d[c]
            del d[c]
            for word in cur:
                if len(word)<=1: ans+=1
                else: d[word[1]].append(word[1:])
        return ans