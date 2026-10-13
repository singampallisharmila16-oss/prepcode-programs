class Solution:
    def isLeapYear(self, Year: int) -> bool:
        if Year % 4 == 0:
            return True
        elif Year % 100 == 0:
            return False
        elif Year % 4 ==  0:
            return True
        else:
            return False
        
obj = Solution()
print(obj.isLeapYear(2024))
print(obj.isLeapYear(3000))


