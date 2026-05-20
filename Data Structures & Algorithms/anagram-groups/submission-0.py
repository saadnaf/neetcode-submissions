class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = {}
        for st in strs:
            lt = [0] * 26

            for s in st:
                lt[ord(s) - 97] += 1

            if tuple(lt) not in hashMap:
                hashMap[tuple(lt)] = [st]
            else:
                hashMap[tuple(lt)].append(st)

        return list(hashMap.values())