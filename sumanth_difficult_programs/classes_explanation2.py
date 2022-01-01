class Civil:

    NAME = "Civil Branch"

    def __init__(self):
        self.subject = "surveying"
        self.lab = "strength of materials"
        self.mech = self.Mechanical()
        print("These are college branches details")

    def subject_info(self):
        print(f"{self.subject} tells about how to survey land")
        self.mech.subject_info()

    def lab_info(self):
        print(f"In {self.lab} lab we wre conducting tests on concrete")
        self.mech.lab_info()

    class Mechanical:

        NAME = "Mechanical Branch"

        def __init__(self):
            self.subject = "fluid mechanics"
            self.lab = "machines"
            print("These are college branches details")

        def subject_info(self):
            print(f"{self.subject} tells about fluid flows")

        def lab_info(self):
            print(f"In {self.lab} lab we wre conducting tests on machines")

    # mech = Mechanical()
    # print(Mechanical.NAME)
    # print(mech.subject)
    # print(mech.lab)
    # mech.subject_info()
    # mech.lab_info()
    # print()


civ = Civil()
# print(Civil.NAME)
# print(civ.subject)
# print(civ.lab)
# civ.subject_info()
# civ.lab_info()


