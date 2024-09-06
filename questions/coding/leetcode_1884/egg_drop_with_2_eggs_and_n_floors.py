class Solution:
    def twoEggDrop(self, n: int) -> int:
        dp = []
        # Adding n rows for each floor/step 
        for _ in range(n+1):
            step = []
            # Adding col for no eggs, one egg, and two eggs
            for _ in range(3):
                step.append(0)
            dp.append(step)
    
        step = 0
        while dp[step][2] < n:
            step += 1
            for egg in range(1, 3):
                dp[step][egg] = dp[step-1][egg-1] + dp[step-1][egg] + 1
        
        return step
