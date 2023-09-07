'''You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

'''



class Solution:
    
    def climbStairs(self, n: int) -> int:
        if(n<2):
                return 1
    
        array=[1,2,0]
        i=2
        while(n>2):
            array[i%3]=array[(i+1)%3]+array[(i-1)%3]
            i+=1
            n-=1
        print(array)
        return array[(i-1)%3]