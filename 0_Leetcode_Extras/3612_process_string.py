from string import ascii_lowercase
class Solution(object):
    def processStr(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = []
        result_str = ""
        for i in s:
            if i in ascii_lowercase:
                result.append(i)
            elif i == "*":
                if result:   ## IF RESULT LIST IS EMPTY, POP GIVES ERROR
                    result.pop()
            elif i == "#":
                result += result
            elif i == "%":
                result.reverse()

        return "".join(result)
