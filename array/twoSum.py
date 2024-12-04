

#first solution

#time complexity O(n2)
def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for index, n in enumerate(nums):
            if n in dict:
                dict[n].append(index)
            else:
                dict[n] = [index]
        print(dict)


        for index, n in enumerate(nums):
            diff = target - n
            if diff in dict:
                for idx in dict[diff]:
                    if idx != index:
                        return[index, idx]
                    


#second solution
#time complexity O(n)
def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for index, num in enumerate(nums):
            diff = target - num

            if diff in dict:
                return [index, dict[diff]]

            dict[num] = index