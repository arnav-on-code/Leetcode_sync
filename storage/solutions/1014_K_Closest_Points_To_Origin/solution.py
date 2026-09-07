class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        import heapq
        heap=[]
        for x,y in points:
            dist=x*x +y*y
            heapq.heappush(heap, (dist,[x,y]))
        result=[]
        for _ in range(k):

            dist,point=heapq.heappop(heap)
            result.append(point)
        return result