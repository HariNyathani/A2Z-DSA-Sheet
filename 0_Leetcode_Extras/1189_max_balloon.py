class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """
        frequency = {"a":0,"b":0,"n":0,"l":0,"o":0}
        Ones = 0
        twos = 0
        for i in text:
            if i in frequency:
                frequency[i] += 1
        if frequency["a"] == frequency["b"] == frequency["n"]: 
            ones = frequency["a"]
        else:
            ones = min(frequency["a"], frequency["b"], frequency["n"])
        
        if frequency["o"] == frequency["l"]:
            twos = frequency["o"]
        else:
            twos = min(frequency["o"], frequency["l"])

        
        return min(ones, twos//2)
