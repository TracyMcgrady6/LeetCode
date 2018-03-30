class Solution:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) == 0:
            return ''
        list_s = list(s)
        i = 0
        j = len(list_s) - 1
        while i < j:
            tmp = list_s[i]
            list_s[i] = list_s[j]
            list_s[j] = tmp
            i += 1
            j -= 1
        return ''.join(list_s)

    def reverseString2(self, s):
        return s[::-1]


a = "hello"
print(Solution().reverseString(a))
