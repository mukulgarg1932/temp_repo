# for i in range(10):
    # print(i)

# list(range(0,10))

prices = [7,1,5,3,6,4]
max_profit=-2424252
buy_day=-1
sell_day=-1
profit_list=[]
buy_sell_list=[]
print(list(range(0,len(prices)-1)))
for i in range(0,len(prices)-1):
    for j in range(i+1,len(prices)):
        profit=prices[j]-prices[i]
        profit_list.append(profit)
        buy_sell_list.append([i,j])
        if profit > max_profit:
            max_profit=profit
            buy_day=i
            sell_day=j



print(f"Max profit will be {max_profit} if we buy on {buy_day+1} day and sell on {sell_day+1} day")
print(profit_list)
print(buy_sell_list)
