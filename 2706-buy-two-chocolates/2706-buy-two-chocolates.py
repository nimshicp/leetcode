class Solution(object):
    def buyChoco(self, prices, money):
        prices.sort()
        first=prices[0]
        second=prices[1]
        total=first+second
        if total<= money:
            leftover=money-total
            return leftover
        else:
            return money    



        