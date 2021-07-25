# Program to buy stocks from somewhere and then sell them for another price
# and find out if that transaction was profitable. (TO THE MOON)

shares = int(input("Enter number of shares:"))
purchasePrice = float(input("Enter purchase price:"))
salePrice = float(input("Enter sale price:"))

BROKER_FEE = 0.03

# Get the total price, and then account for the brokers cost
totalAmountPaid = shares * purchasePrice
totalAmountPaid = totalAmountPaid + (totalAmountPaid * BROKER_FEE)

totalAfterSale = shares * salePrice
totalAfterSale = totalAfterSale - (totalAfterSale * BROKER_FEE)

totalReturn = totalAfterSale - totalAmountPaid

if totalAmountPaid < totalAfterSale:
    print("After the transaction, you gained {0} dollars.".format(totalReturn))
elif totalAmountPaid > totalAfterSale:
    print("After the transaction, you lost {0} dollars.".format(totalReturn * - 1))
else:
    print("You broke even.")
