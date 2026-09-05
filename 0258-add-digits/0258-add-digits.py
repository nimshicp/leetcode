class Solution(object):
    def addDigits(self, num):
        while num >= 10:
            result = 0

            while num > 0:
                digit = num % 10
                result += digit
                num = num // 10

            num = result

        return num


s = Solution()

print(s.addDigits(38))
print(s.addDigits(0))