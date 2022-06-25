class Student:

    COLLEGE = "GIST"

    def __init__(self, sur_name, first_name, last_name):
        self.sur_name = sur_name
        self.first_name = first_name
        self.last_name = last_name

    def full_name(self):
        return f"{self.sur_name}.{self.first_name} {self.last_name}"

    def mail_id(self):
        return f"{self.first_name}.{self.last_name}@gmail.com"

