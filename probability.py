# Enter your code here. Read input from STDIN. Print output to STDOUT
from fractions import Fraction

def calculate_probability():
    # Initial probabilities
    P_WX = Fraction(5, 9)  # Probability of drawing a white ball from Bag X
    P_BX = Fraction(4, 9)  # Probability of drawing a black ball from Bag X
    
    # Probabilities of drawing a black ball from Bag Y given the ball transferred
    P_BY_given_WX = Fraction(6, 14)  # Probability of drawing black from Bag Y if a white ball was transferred
    P_BY_given_BX = Fraction(7, 14)  # Probability of drawing black from Bag Y if a black ball was transferred
    
    # Total probability using the law of total probability
    P_BY = P_WX * P_BY_given_WX + P_BX * P_BY_given_BX
    
    return P_BY

if __name__ == "__main__":
    probability = calculate_probability()
    print(f"{probability.numerator}/{probability.denominator}")
