class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        
        for word in strs:
            delimiter = "Tharack"
            encoded = delimiter + word
            result += encoded
        print(result)
        print(result.split("Tharack"))
        return result

    def decode(self, s: str) -> List[str]:

        return s.split("Tharack")[1:]


