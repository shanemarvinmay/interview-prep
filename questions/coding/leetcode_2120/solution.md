m is the length of command.
If we want O(m^2) solution, that is quite stright forward, and interviewer may not be satisfied. Thus, we need to do more.

First let us think, how do we know when will the robot move out of the boundary if the robot start at current step?
We know the start position of robot, say, (x,y) means row x and col y , this is quite different than Cartesian coordinate, please get used to it.
If the robot move out of boundary, one of the four situation must happen:
1, it move up for x+1 steps
2, it move down for n-x steps
3, it move left for y+1 steps
4, it move right for n-y steps

Then, let us trace back from last command to first command
We assume that the if the robot operate all the commands to the end (whenever it starts), the final position is (0,0), notice that this is virtual position, not real, just for easy understanding.

Suppose we have the command "LURD", at time t=4, the location will be (0,0)
If the robot start at t=3, and the command will be "D", what is the initial virtual position?
(-1,0). In other words, at time t=3, the position will be (-1,0)
If the robot start at t=2, and the command will be "RD", what is the initial virtual position? (-1,-1). At time t=2, the position will be (-1,-1)
.....
We can find each virtual position at time t when the final position without bound is (0,0), we keep track of each initial vertical and horizontal position and record them in separate dictionary.
Then we can judge if we can walk until the end?
Previouly, I declare, in the future, if the robot walk up (x+1) steps, down (n-x) steps, left (y+1) steps, right (n-y) steps, it will stop.
In other words, suppose (row,col) is the position at time t, if row-(x+1), row+(n-x) appears in the horizonal dictionary, or col-(y+1), col+(n-y) appears in vertical dictionary, it will stop at that time. If multiple answer exists, find the most recent time since it happens first, and the answer will be difference between most recent dictionary time and current time.
If there is no stop time, congratulations, it will walk till final.
This is a one-pass solution, with time complexity O(m), no matter how big n is. Time is 109ms, beat 100% currently.

```
class Solution(object):
    def executeInstructions(self, n, startPos, s):
        """
        :type n: int
        :type startPos: List[int]
        :type s: str
        :rtype: List[int]
        """
        m = len(s)
        direc = {'U':[-1,0],'D':[1,0],'L':[0,-1],'R':[0,1]}
        upmost = startPos[0] + 1
        downmost = n - startPos[0]
        leftmost = startPos[1] + 1
        rightmost = n - startPos[1]
        curr_row,curr_col = 0,0    
        next_row,next_col = {0:m}, {0:m}
        ans = []
        
        for i in range(m-1,-1,-1):
            curr_row -= direc[s[i]][0]
            curr_col -= direc[s[i]][1]
            maxstep = m-i
            if curr_row - upmost in next_row:  
                maxstep = min(maxstep,  next_row[curr_row - upmost] - i - 1 )
            if curr_row + downmost in next_row:  
                maxstep = min(maxstep,  next_row[curr_row + downmost] - i - 1 )
            if curr_col - leftmost in next_col:  
                maxstep = min(maxstep,  next_col[curr_col - leftmost] - i - 1 )
            if curr_col + rightmost in next_col: 
                maxstep = min(maxstep,  next_col[curr_col + rightmost] - i - 1 )
            next_row[curr_row] = i
            next_col[curr_col] = i
            ans.append(maxstep)
            
        return ans[::-1]
```