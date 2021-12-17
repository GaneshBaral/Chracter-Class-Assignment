#Character class assignment - Ganesh Baral 

# Create Class
class Character:
    def __init__(self, name, phrase1, phrase2,):
        self.name = name
        self.phrase1 = phrase1
        self.phrase2 = phrase2
        self.level = 0

    def speak(self, phraseNum):
        if phraseNum == 1:
            print(self.phrase1)
        elif phraseNum == 2:
            print(self.phrase2)

    def setLevel(self, newLevel):
        self.level = newLevel
        print("Level: " + str(self.level))


# Character Objects
JohnWick = Character("John Wick", "IT WASN'T JUST A PUPPY.", "YOU WANTED ME BACK. I'M BACK.")
Thanos = Character("Thanos", "I AM INEVITABLE.", "PERFECLY BALANCED, AS ALL THINGS SHOULD BE.")


# Object Method Call
JohnWick.speak(1)
Thanos.setLevel(2) 
Thanos.speak(2)


