class Student:

    stipend_hike_rate = 1.05

    def __init__(self, first_name, last_name, initial_stipend):
        self.first_name = first_name
        self.last_name = last_name
        self.initial_stipend = initial_stipend

    # @property
    def mail_id(self):
        return f"{self.first_name}.{self.last_name}@gmail.com"

    # @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def apply_hike(self):
        self.initial_stipend = self.initial_stipend * self.stipend_hike_rate
