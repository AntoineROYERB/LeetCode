class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)  # Pour gérer le cas où k est plus grand que la longueur de la liste
        firstPart = nums[-k:]  # Prend les k derniers éléments de la liste
        del nums[-k:]  # Supprime les k derniers éléments de la liste
        nums[:0] = firstPart  # Insère les k éléments au début de la liste