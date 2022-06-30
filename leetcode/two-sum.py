class Solution(object):
    def twoSum(self, nums, target):
        save = {}
        for i in range(len(nums)):
            if nums[i] in save and (target == nums[i] + nums[i]):
                return [save[nums[i]], i]
            else:
                save[nums[i]] = i

        # for key, value in save.items():
        #     print(key, ' : ', value)

        for x in range(len(nums)):
            for key in save.keys():
                sub = target - key
                if sub in save and key != sub:
                    return [save[key], save[sub]]
                    
                



def main():
    s = Solution()
    nums = [2,7,11,15]
    target = 9
    print(s.twoSum(nums, target))
   
    nums = [3,2,4]
    target = 6
    print(s.twoSum(nums, target))
   
    nums = [3,3]
    target = 6
    print(s.twoSum(nums, target))

if __name__ == "__main__":
    main()