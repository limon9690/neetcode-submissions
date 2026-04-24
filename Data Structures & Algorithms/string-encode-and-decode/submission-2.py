class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""

        for s in strs:
            enc_str = f"{len(s)}#{s}"
            encoded += enc_str

        return encoded

        

    def decode(self, s: str) -> List[str]:
        i, n = 0, len(s)
        decoded = []

        while i < n:
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            decoded.append(s[i:j])
            i = j

        return decoded

        
