class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
    
        # count = 
        # s1 = freq.most_common()[0]

        # left,right = 0,0
        # longest = 0
        # hand = k
        # currLength = 0

        # while right < len(s):
        #     # if no we finished k replacement and current char is not most common
        #     # we try to shrink
        #     print(hand, s[left:right],s[right])

        #     while hand == 0 and s[right] != s1[0]:
        #         # if the character isolated wasn't most common
        #         # meaming it was the character we can replace 
        #         # we gained a replacement ability
        #         if s[left] != s1[0]:
        #             hand += 1
        #         # otherwise we just ignore the hand and isolate it anyway
        #         currLength -= 1
        #         left += 1
        #     # otherwise, we still have replacements and char is a
        #     # we check if the char is not most common
        #     if s[right] != s1[0]:
        #         # reduce replacements
        #         hand -= 1
        #     # whichever char most common or not, we still move left and length
        #     # as long as we can replace that char with our most common
        #     currLength += 1
        #     if hand == 0:
        #         longest = max(longest,currLength)
        #     right += 1
            
        count = defaultdict(int)
        left,right = 0,0

        max_count = 0 #count of frequency char in windown
        longest = 0

        while right < len(s):
            count[s[right]] += 1 #increase its count
            max_count = max(max_count, count[s[right]])

            # invalid
            while (right - left + 1) - max_count > k:
                # we have more replacement needed in this window
                # most common char is very less comparing to the window
                # reduce
                count[s[left]] -= 1
                left += 1
            longest = max(longest,right - left + 1)
            right += 1
        return longest
