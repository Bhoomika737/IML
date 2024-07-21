from fractions import Fraction


white_x = 5
black_x = 4
white_y = 7
black_y = 6


total_x = white_x + black_x


total_y = white_y + black_y


P_Bx = Fraction(black_x, total_x)


P_Wx = Fraction(white_x, total_x)


P_By_given_Bx = Fraction(black_y + 1, total_y + 1)


P_By_given_Wx = Fraction(black_y, total_y + 1)

P_By = P_Bx * P_By_given_Bx + P_Wx * P_By_given_Wx


print(P_By)