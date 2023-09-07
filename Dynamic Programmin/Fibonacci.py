class Solution:
    def fib(self, n: int) -> int:
        array = [1, 1, 0]
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 1

        for i in range(2, n):
            array[(i) % 3] = array[(i-1) % 3]+array[(i+1) % 3]

        return array[(i % 3)]
