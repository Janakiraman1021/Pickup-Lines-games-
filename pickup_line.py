# Tell Your Name And I Tell The Pickup Line For You

import random as r
import time  as t 

pickup_lines = ['Excuse me, do you have a map? I keep etting lost in your eyes.',"Are you a magician? Because whenever I look at you, everyone else disappears.","You  must be a snowflake because I've fallen for you.","Do you believe in love at first sight, or should I walk by again?","Are you a shooting star? Because you just brightened up my night.","Is your name Google? Because you have everything I've been searching for.","Are you a bank loan? Because you have my interest.","If I were to write a story about us, it would be a best-seller.","Are you a time traveler? Because I can't imagine my future without you in it.","Excuse me, I just wanted to let you know that you have the most beautiful smile I've ever seen."]
pickup_lines_2 = ["If I had a star for every time I thought of you, I'd be holding the entire galaxy in my hands.","I don't believe in love at first sight, but I think I just changed my mind.","You must be a mermaid because I'm drowning in your beauty.","I'm not a photographer, but I can definitely picture us together.","I was wondering if you had an extra heart because you just stole mine.","Excuse me, but I think you dropped something – my jaw.","Do you believe in fate? Because I think we were meant to meet.","I could spend hours listening to you talk about anything and everything.","You're like a dictionary – you add meaning to my life.","Do you have a band-aid? Because I just scraped my knee falling for you."]


name = str(input("Hey Girl , I don't mean to be forward, but I just have to know Your name because  stolen my heart. Would you be willing to share it with me? \n "))
length = len(name)

if length<=10:
    print(pickup_lines_2[length-1])
    while True:
        con = str(input("Do You What To Continue ??  Type y for Continue and N for not "))
        if con == 'y'  or con == 'Y':
            name = str(input("Hey Girl , I don't mean to be forward, but I just have to know Your name because  stolen my heart. Would you be willing to share it with me? \n "))
            print(r.choice(pickup_lines_2))
        con = str(input("Do You What To Continue ??  Type y for Continue and N for not "))
        if con == 'y'  or con == 'Y':
             continue
        else:
             break


elif length > 10:
    print(r.choice(pickup_lines))
    while True:
        con = str(input("Do You What To Continue ??  Type y for Continue and N for not "))
        if con == 'y'  or con == 'Y':
            name = str(input("Hey Girl , I don't mean to be forward, but I just have to know Your name because  stolen my heart. Would you be willing to share it with me? \n "))
            print(r.choice(pickup_lines))
        con = str(input("Do You What To Continue ??  Type y for Continue and N for not "))
        if con == 'y'  or con == 'Y':
             continue
        else:
             break
