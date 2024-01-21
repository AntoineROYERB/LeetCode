#https://leetcode.com/explore/interview/card/top-interview-questions-easy/99/others/648/
class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        total_bits = 32
        for _ in range(total_bits):
            # Décaler le résultat vers la gauche pour faire de la place pour le prochain bit inversé
            result = (result << 1) | (n & 1)
            # Décaler le nombre d'entrée vers la droite pour récupérer le prochain bit
            n = n >> 1
        return result