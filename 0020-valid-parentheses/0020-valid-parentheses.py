class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        d = {
            "(": ")",
            "[": "]",
            "{": "}"
        }
        stack = []
        for char in s:
            if char in ["(", "[", "{"]:
                stack.append(d[char])
            else:
                # Check there is a element in stack
                if len(stack) == 0:
                    return False
                out = stack.pop()
                if char != out:
                    return False
        # Assert we finish
        return len(stack) == 0