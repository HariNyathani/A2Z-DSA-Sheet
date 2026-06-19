class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        current = 0
        highest = 0
        for i in range(len(gain)):
            current += gain[i]
            if highest < current:
                highest = current
        return highest
