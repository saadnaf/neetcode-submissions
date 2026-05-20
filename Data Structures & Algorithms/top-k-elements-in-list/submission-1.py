class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap = {}
        for n in nums:
            if n not in hashMap:
                hashMap[n] = 1
            else:
                hashMap[n] += 1
        
        arrayMap = []
        for n, c in hashMap.items():
            arrayMap.append([c, n])
        arrayMap.sort()

        result = []
        for i in range(k):
            result.append(arrayMap.pop()[1])
        return result
 
        