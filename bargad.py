import time
import sys
def print_lyrics():
    lyrics = [
        " Bargad tale jo main baithu kabhi",
        "Saaye mein bhi dikhe chehra tera",
        "Tera zikr bhi jaadu kare",
        "Hawaayein bhi laaye sandesha tera",
        "Ye deewanapan, mujhe le dooba inn lakeeron mein",
        "Tu likhi hai ya nahi?",
        "Karu naam ki teri ibaadatеin",
        "Teri galliyon ka hi hoon main aashiq baby"
    ]
    
    delays=[0.8,0.7,0.8,1.0,0.9,0.5,0.9,0.6]
    
    print("-----Bargad-----\n")
    time.sleep(1.1)
    
    for i, line in enumerate(lyrics):
        for char in line:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.06)
        print()
        time.sleep(delays[i])
print_lyrics()