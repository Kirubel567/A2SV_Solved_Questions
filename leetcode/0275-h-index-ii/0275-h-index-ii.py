class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)

        h = 0
        for i in range(n):
            papers = n - i

            if citations[i] >= papers:
                h = papers
                break

        return h