class Solution:
    def encode(self, strs: List[str]) -> str:
        encoded_string = ""

        for s in strs:
            encoded_string += str(len(s)) + "#" + s

        return encoded_string

    def decode(self, s: str) -> List[str]:
        decoded_string = []
        i = 0

        while i < len(s):
            j = i

            # tìm dấu #
            while s[j] != "#":
                j += 1

            size = int(s[i:j])

            start = j + 1
            end = start + size

            decoded_string.append(s[start:end])

            i = end

        return decoded_string