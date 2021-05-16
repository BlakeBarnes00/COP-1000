# Land Calculation
# Ask for an amount of land in square feet, then see how many acres that could make
# An acre is roughly 43,560 sqft.

ACRE = 43560

userAmount = float(input("How many square feet do you want converted to acres? "))
print(userAmount/ACRE)