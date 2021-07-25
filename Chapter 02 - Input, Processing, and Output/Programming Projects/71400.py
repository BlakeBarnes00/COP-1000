# 1.5 Cups of Sugar, 1 Cup of Butter, 2.75 Cups of Flour make 48 Cookies

# To get constants I devided by the initail amount of cookies disclosed.
SUGAR_CONST = 1.5 / 48
BUTTER_CONST = 1 / 48
FLOUR_CONST = 2.75 / 48

cookiesWanted = int(input("Enter number of cookies:"))

sugar = SUGAR_CONST * cookiesWanted
butter = BUTTER_CONST * cookiesWanted
flour = FLOUR_CONST * cookiesWanted

print("You need {0} cups of sugar, {1} cups of butter, and {2} cups of flour.".format(sugar, butter, flour))