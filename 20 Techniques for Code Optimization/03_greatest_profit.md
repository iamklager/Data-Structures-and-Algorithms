# Chapter 20

## Exercise 03

You're working on some more stock-prediction software. The function you're writing accepts an array of predicted prices for a particular stock over the course of time.  

YOur function should calculate the greatest profit that could be made from a single "buy" transaction followed by a single "sell transaction.  

Your job is to optimize the code so that the function clocks in at just $O(N)$.

```python
p = [10, 7, 5, 8, 11, 2, 6]

def GreatestProfit(prices):
    price_lowest = prices[0]
    profit = 0

    for price in prices:
        if price < price_lowest:
            price_lowest = price
        elif price - price_lowest > profit:
            profit = price - price_lowest
    
    return profit
    

print(GreatestProfit(p))
```