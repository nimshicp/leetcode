class Solution(object):
    def calPoints(self, operations):
        arr = []

        for i in operations:
            if i.lstrip("-").isdigit():
                arr.append(int(i))

            elif i == "C":
                arr.pop()

            elif i == "D":
                arr.append(arr[-1] * 2)

            elif i == "+":
                arr.append(arr[-2] + arr[-1])

        total = 0
        for j in arr:
            total += j

        return total


s = Solution()
print(s.calPoints(["5", "-2", "4", "C", "D", "9", "+", "+"]))