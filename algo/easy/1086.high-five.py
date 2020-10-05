class Solution(object):
    def highFive(self, items):
        """
        :type items: List[List[int]]
        :rtype: List[List[int]]
        """
        items = sorted(items, key=lambda x: x[1], reverse = True)
        items = sorted(items,key=lambda x: x[0])
        
        res = []
        scores = 0
        avg_score = 0
        count = 0
        ID = items[1][0]
        for i in range(len(items)):
            if items[i][0] == ID and count <= 5:
                scores += items[i][1]
                count += 1
            elif items[i][0] != ID:
                ID = items[i][0]
                count = 1
                scores = items[i][1]
            if count == 5:
                avg_score = scores // 5
                res.append([items[i][0], avg_score])
            else:
                pass
        return res