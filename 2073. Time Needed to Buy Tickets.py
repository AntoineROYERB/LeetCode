class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        time, ticketK = 0, tickets[k]
        for i, ticket in enumerate(tickets):
            if i <= k:
                time += min(ticket, ticketK)
            else:
                time += min(ticket, ticketK - 1)
        return time