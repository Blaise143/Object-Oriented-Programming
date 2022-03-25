class Human:
    def __init__(self, name : str, age : int, height : int) -> None:
        self.age = age
        self.name = name
        self.height = height
        
    def get_name(self) -> str:
        return self.name
    
    def get_age(self) -> int:
        return self.age
    
    def get_height(self) -> int:
        return self.height

