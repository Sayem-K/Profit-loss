buying_price = 430
selling_price = 340

if buying_price < selling_price:
    profit = selling_price - buying_price
    print("You are making {} rupees profit.".format(profit))
else:
    loss = buying_price - selling_price
    print("You are making {} rupees loss.".format(loss))