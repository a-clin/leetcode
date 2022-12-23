class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u']
        output = [""]* len(s)
        l, r = 0, len(s)-1

        while l <= r:
            while r > l and s[r].lower() not in vowels:
                output[r] = s[r]
                r -= 1
            if s[r].lower() in vowels and s[l].lower() in vowels:
                output[l] = s[r]
                output[r] = s[l]
                r -= 1
            else:
                output[l] = s[l]
            
            l += 1

        return "".join(output)