class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count = 0
        if not details:
            return count
    
        for people in details:
            if int(people[11:13]) > 60:
                
                count+=1
        return count
        