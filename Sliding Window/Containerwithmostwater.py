class Solution:
    def maxArea(self, height: List[int]) -> int:
        ptr1=0
        ptr2=len(height)-1
        area=0
        while(ptr1<=ptr2):
            x=min(height[ptr1],height[ptr2])*(ptr2-ptr1)
            if(x>area):
                area=x
            if(height[ptr1]>height[ptr2]):
                ptr2-=1
            else:
                ptr1+=1
        return area