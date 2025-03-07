class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        #get all primes from [0, right]
        tracker = [True for i in range(right+1)]
        
        primes = []
        for i in range(2,right+1):
            if tracker[i]:
                multiple = i*i
                while multiple <= right:
                    tracker[multiple] = False
                    multiple += i
        primes = []
        for i in range(max(2,left), right+1):
            if tracker[i]:
                primes.append(i)
        
        closestpair = [-1, -1]

        for i in range(len(primes)-1):
            if closestpair[0] < 0 or primes[i+1]-primes[i] < closestpair[1]-closestpair[0]:
                closestpair[0], closestpair[1] = primes[i], primes[i+1]
        return closestpair
            

                
            
            
