class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded += str(len(s)) + "#" + s
        return encoded
            

    def decode(self, s: str) -> List[str]:
        decoded = []
        length = []
        i = 0
        while i < len(s):
            if s[i] == "#":
                num = int("".join(length))
                start = i + 1
                end = start + num
                decoded.append(s[start:end])
                length = []
                i = end
                continue
            else:
                length.append(s[i])
            i += 1
        return decoded
     
    


