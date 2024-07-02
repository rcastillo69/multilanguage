def climbingLeaderboard(ranked, player):
    result = []
   
    unique_ranks = sorted(set(ranked), reverse=True)
  
    i = len(unique_ranks) - 1
    
    for score in player:
        while i >= 0 and score >= unique_ranks[i]:
            i -= 1
        result.append(i + 2)  
        
    return result


ranked = [100, 90, 90, 80]
player = [70, 80, 105]
print(climbingLeaderboard(ranked, player))  # Output: [4, 3, 1]
