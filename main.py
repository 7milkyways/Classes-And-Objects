class Student:
    # [assignment] Skeleton class. Add your code here
    
    def __init__(self, name: str, age: int, tracks: list, score: float):
        self.name = name
        self.age = age
        self.tracks = tracks
        self.score = score

    def change_name(self, name):
        self.name = name

    
    def change_age(self, age):
        self.age = int(age)

    
    def add_track(self, new_track):
        self.tracks.append(new_track)

    
    def get_score(self, score):
         self.score = score

         return score




Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)



# Expected methods
Bob.change_name("Peter")
Bob.change_age(36)
Bob.add_track("Full Stack")
Bob.get_score(83)

print(Bob.score)