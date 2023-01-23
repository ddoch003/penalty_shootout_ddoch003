import time
import random
home_team_result=0
home_team_potential=5
away_team_result=0
away_team_potential=5
home_team_score=[True,False]
away_team_score=[True,False]
round=1

print("90 minutes and an extra time could not determine the winner. It is time for a penalty shootout!\n")

while round<=5:
    time.sleep(2)
    print(f"Round {round}")
    time.sleep(2)
    print("Home team shoots...")
    time.sleep(1)
    goal_home=random.choice(home_team_score)
    if goal_home:
        print("Home team scores!")
        home_team_result+=1
        time.sleep(1)
        print(f"The result is now {home_team_result} : {away_team_result}\n")
        if home_team_result>away_team_potential:
            time.sleep(1)
            print("Home team wins!")
            break
    else:
        print("Home team misses!")
        time.sleep(1)
        print(f"The result is still {home_team_result} : {away_team_result}\n")
        home_team_potential-=1
        if away_team_result>home_team_potential:
            print("Away team wins!")
            break
    time.sleep(2)
    print("Away team shoots...")
    time.sleep(1)
    goal_away=random.choice(away_team_score)
    if away_team_score:
        print("Away team scores!")
        away_team_result+=1
        time.sleep(1)
        print(f"The result is now {home_team_result} : {away_team_result}\n")
        if away_team_result>home_team_potential:
            time.sleep(1)
            print("Away team wins!")
            break
    else:
        print("Away team misses!")
        time.sleep(1)
        print(f"The result is still {home_team_result} : {away_team_result}\n")
        away_team_potential -= 1
        if home_team_result > away_team_potential:
            print("Home team wins!")
            break
    round+=1
else:
    time.sleep(2)
    print("Sudden death!")
    while True:
        time.sleep(2)
        print("Home team shoots...")
        goal_home=random.choice(home_team_score)
        if goal_home:
            time.sleep(1)
            print("Home team scores!")
            time.sleep(1)
            home_team_result+=1
            print(f"The result is now {home_team_result} : {away_team_result}\n")
        else:
            time.sleep(1)
            print("Home team misses!")
            time.sleep(1)
            print(f"The result is still {home_team_result} : {away_team_result}\n")
        goal_away=random.choice(away_team_score)
        if goal_away:
            time.sleep(1)
            print("Away team scores!")
            away_team_result+=1
            print(f"The result is now {home_team_result} : {away_team_result}\n")
        else:
            time.sleep(1)
            print("Away team misses!")
            time.sleep(1)
            print(f"The result is still {home_team_result} : {away_team_result}\n")
        if home_team_result>away_team_result:
            time.sleep(2)
            print("Home team wins!")
            break
        elif home_team_result<away_team_result:
            time.sleep(2)
            print("Away team wins!")
            break