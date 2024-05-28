# Chapter 20

## Exercise 01

You are to write a function that accepts two arrays of players and returns an array of the players who play in both sports. In this case, that would be:  

["Jull Huang", "Wanda Vakulskas"]  

While there are players who share first names and players who share last names, we can assume there's only one person who has a particular full name (meaning first and last name).  

We can use a nested-loops appraoch, comparing each player from one array against each player from the other array, but this would have a runtime of $O(N\cdot M)$. Your job is to optimize the function so that it can run in just $O(N + M)$.

```python
basketball_players = [
    {"first_name": "Jill", "last_name": "Huang", "team": "Gators"},
    {"first_name": "Janko", "last_name": "Barton", "team": "Sharks"},
    {"first_name": "Wanda", "last_name": "Vakulskas", "team": "Sharks"},
    {"first_name": "Jill", "last_name": "Moloney", "team": "Gators"},
    {"first_name": "Luuk", "last_name": "Watkins", "team": "Gators"}
]
football_players = [
    {"first_name": "Hanzla", "last_name": "Radostil", "team": "32ers"},
    {"first_name": "Tina", "last_name": "Watkins", "team": "Barleycorns"},
    {"first_name": "Alex", "last_name": "Patel", "team": "32ers"},
    {"first_name": "Jill", "last_name": "Huang", "team": "Barleycorns"},
    {"first_name": "Wanda", "last_name": "Vakulskas", "team": "Barleycorns"}
]

def PlayBothSports(players1, players2):
    d = {}
    res = []

    for player in players1:
        d[player["first_name"] + ' ' + player["last_name"]] = True
    for player in players2:
        if player["first_name"] + ' ' + player["last_name"] in d:
            res.append(player["first_name"] + ' ' + player["last_name"])
    
    return res


print(PlayBothSports(football_players, basketball_players))
```