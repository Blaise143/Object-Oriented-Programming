from human import Human

class Student(Human):
    
    def __init__(self, name : str, age : int, height : int, grade : int):
        super().__init__(name, age, height)
        self.grade=grade
        
    def get_grade(self) -> int:
        return self.grade
        
    def set_grade(self, grade : int) -> None:
        self.grade = grade