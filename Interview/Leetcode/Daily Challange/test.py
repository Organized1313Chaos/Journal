
def getMaxColors(prices, money):
    # Write your code here
    N = len(prices)
    l = 0
    r = 0
    output  = 0
    sm = 0
    while l<N and r<N:
        while True and r<N:
            sm += prices[r]
            if sm>money:
                break
            r += 1
            
        output = max(r-l, output)
        r+=1
        while True and l<N:
            sm -= prices[l]
            if sm<=money:
                break
            l+=1
    return output

prices = [2,3,5,1,1,2,1]
money = 7
res = getMaxColors(prices, money)
print(f"res==>{res}")