class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        answer = []
        for index in range(1, n + 1):
            match index:
                case _ if index % 3 == 0 and index % 5 == 0:
                    answer.append("FizzBuzz")
                case _ if index % 3 == 0:
                    answer.append("Fizz")
                case _ if index % 5 == 0:
                    answer.append("Buzz")
                case _:
                    answer.append(str(index))
        return answer
