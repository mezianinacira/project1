import random

colors = ["yellow", "blue", "red", "green", "pink"]

colors  = random.sample(colors, 5)
#print(colors)


for x in range(5):
    codebreaker = input("Enter your chosen colors: ")

    codebreaker = codebreaker.split(" ")

    win = 0
    lose = 0
    for color , guess in zip(colors,codebreaker):
        if color ==guess:
            pass
            win = win+1
            print(color)
            
      
            pass
        else:
            lose = lose+1
            pass
    print(win)
    
    print(lose)
    if lose ==0:
        break

            
    
