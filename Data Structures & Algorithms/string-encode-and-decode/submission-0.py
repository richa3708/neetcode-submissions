class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded += str(len(s)) + "#" + s
        return encoded

    def decode(self, s: str) -> List[str]:
        i = 0
        decoded = []
        while i < len(s):
            # 1. Read length prefix until '#'
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])

            # 2. Extract the string of that length
            word = s[j+1 : j+1+length]
            decoded.append(word)

            # 3. Move pointer forward
            i = j + 1 + length
        return decoded

