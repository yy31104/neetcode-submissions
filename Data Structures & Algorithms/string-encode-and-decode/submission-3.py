class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded += str(len(s)) + "#" + s
        return encoded


    def decode(self, s: str) -> List[str]:
        i = 0
        length = ""
        decoded = []
        while i < len(s):
            if s[i] != "#":
                length += s[i]
                i += 1
            else:
                start = i + 1
                end = start + int(length)
                decoded.append(s[start:end])
                i = end
                length = ""
        return decoded
        
