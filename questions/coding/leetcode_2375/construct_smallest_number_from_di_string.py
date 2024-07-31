class Solution:
    def __init__(self):
        self.possible_nums = [1,2,3,4,5,6,7,8,9]
        self.pattern = ''
        self.lowest = 1
        self.highest = 9
        self.num = 999_999_999
    def smallestNumber(self, pattern: str) -> str:
        self.num = 999_999_999
        self.highest = len(pattern) + 1
        self.pattern = pattern
        for i in range(self.lowest, self.highest + 1):
            self.get_all_possible_nums(cur_nums=[i], cur_ltr=self.pattern[0])
        return f'{self.num}'

    def get_all_possible_nums(self, cur_nums, cur_num=None, cur_ltr=''):
        if cur_num is None:
            cur_num = cur_nums[0]
        if cur_ltr == '':
            num = self.list_to_num(cur_nums)
            self.num = min(self.num, num)
            return
        # Setting the inclusive range we will need to go over to find the next
        # number.
        if cur_ltr == 'D':
            start = self.lowest
            end = cur_num-1
        else:
            start = cur_num+1
            end = self.highest

        for i in range(start, end+1):
            if i in cur_nums:
                continue
            is_valid_lower = i < cur_num and cur_ltr == 'D'
            is_valid_higher = i > cur_num and cur_ltr == 'I'
            if is_valid_lower or is_valid_higher:
                cur_nums.append(i)
                nxt_ltr = ''
                if len(cur_nums) <= len(self.pattern):
                    nxt_ltr = self.pattern[len(cur_nums)-1]
                outcome = self.get_all_possible_nums(cur_nums, cur_num=i, cur_ltr=nxt_ltr)
                if outcome:
                    num = self.list_to_num(cur_nums)
                    self.num = min(self.num, num)
                cur_nums.pop()
        return []
    def list_to_num(self, l):
        s = ''.join([str(i) for i in l])
        if len(s) == 0:
            return 999_999_999
        return int(s)
