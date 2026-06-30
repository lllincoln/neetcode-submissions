class Solution:
    def encode(self, strs: List[str]) -> str:
        full_str = ""

        for s in strs:
            length_prefix = str(len(s))
            length_prefix = (" " * (3 - len(length_prefix))) + length_prefix

            full_str += length_prefix + s

        return full_str

    def decode(self, s: str) -> List[str]:
        idx = 0
        strs = []

        while len(s) > idx:
            str_length = int(s[idx:idx + 3].strip())
            str_start = idx + 3
            str_end = str_start + str_length
            decoded_str = s[str_start:str_end]

            strs.append(decoded_str)
            idx = str_end
        
        return strs