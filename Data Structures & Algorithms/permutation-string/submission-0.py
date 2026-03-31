class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # We can use fixed sliding window of size len(s1)
        # this allows us to get all substrings

        # we also need to use frequencies
        # here I choose frequency array: already know how to use frequency map
        # use ord to calculate character index in the array

        # This is a problem of frequencies because a string is a permutations of another string if and only if they have same frequencies of characters
        s1_counter = [0] * 26
        s2_counter = [0] * 26

        # size
        k = len(s1)
        # get first window
        window = s2[:k]

        # s1 frequency update
        for char in s1:
            idx = ord(char) - ord('a')
            s1_counter[idx] += 1
        # fill first window frequencies
        for char in window:
            idx = ord(char) - ord('a')
            s2_counter[idx] += 1

        # all windows
        for i in range(len(s2) - k):
            idx = ord(s2[i]) - ord('a')
            next_idx = ord(s2[i + k]) - ord('a')
            # compare each window with s1, if are the same, return True automatically
            if s1_counter == s2_counter:
                return True
            # remove s2[i] and add s2[i + k]
            s2_counter[idx] -= 1
            s2_counter[next_idx] += 1
        
        # return the comparison if the last window and our s1
        return s1_counter == s2_counter

            



        