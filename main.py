import string


class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self,name,age,tracks,score):
        self.name = name
        self.age = int(age)
        self.tracks = tracks
        self.score = float(score)
        pass

    def change_name(self,new_n):
        self.name = new_n
        print("Your new name is "+self.name)

    def change_age(self,new_a):
        self.age = int(new_a)
        return self.age

    def add_track(self,new_t):
        tracks = self.tracks.append(new_t)
        pass

    def get_score(self):
        print(self.score)
    


Bob = Student("Bob",26,["FE","BE","PE","SE"],20.90)

# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
print(Bob.tracks)
Bob.get_score()
print(Bob.age)
print(Bob.name)
print (Bob.name +" is "+str(Bob.age)+" years  old. He has "+str(Bob.tracks)+" as tracks and his score is "+str(Bob.score))
