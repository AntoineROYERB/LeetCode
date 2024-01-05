class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        maxProfit = 0

        for i in range(1, len(prices)):
            # Calcul du profit potentiel si on vend à la journée actuelle
            potential_profit = prices[i] - prices[i - 1]

            # Mise à jour du profit maximal si le profit potentiel est positif
            if potential_profit > 0:
                maxProfit += potential_profit
        print(maxProfit)
        return maxProfit