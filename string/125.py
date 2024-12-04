class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = '' 

        for i in s:
            if i.isalnum():
                string += i

        string = string.upper()

        print(string)

        return string == string[::-1]      



class Solution:
    def check(self, string):
        left = 0
        right = len(string) - 1

        while left <= right:
            if string[left] != string[right]:
                return False
            left += 1
            right -= 1

        return True


    def isPalindrome(self, s: str) -> bool:
        string = '' 

        for i in s:
            if i.isalnum():
                string += i

        string = string.upper()
        return self.check(string)

       