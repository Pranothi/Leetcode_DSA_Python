"""
Given a string expression representing an expression of fraction addition and subtraction,
return the calculation result in string format. The final result should be an irreducible fraction.
If your final result is an integer, change it to the format of a fraction that has a denominator 1.
So in this case, 2 should be converted to 2/1.

Example:
    Input: expression = "-1/2+1/2+1/3"
    Output: "1/3"
"""
from fractions import Fraction

class Solution:
    def fractionAddition(self, expression: str) -> str:
        # Convert the expression into a list of Fraction objects
        res = sum(map(Fraction, expression.replace('+', ' +').replace('-', ' -').split()))

        # Return the result as a string in the form "numerator/denominator"
        return str(res.numerator) + '/' + str(res.denominator)


# Create an instance of the Solution class
solution = Solution()

# Define test cases
expression = "-1/2+1/2"
result = solution.fractionAddition(expression)

print(result)
