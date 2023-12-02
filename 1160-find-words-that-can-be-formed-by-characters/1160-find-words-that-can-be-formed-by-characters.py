class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        c = Counter(chars)
        ans = 0
        for word in words:
            temp = Counter(word)
            good = True
            for key, val in temp.items():
                if c[key] < val:
                    good = False
                    break
            if good: ans += len(word)
        return ans