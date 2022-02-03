from student import Student


class College():
    def __init__(self,name,number,intake_limit,tuition,utility):
        self.name = name
        self.number = number
        self.intake_score = 0
        self.intake_limit = intake_limit
        self.intake_students = []
        self.intake_students_meritocratic = []
        self.tuition = tuition

        self.intake_score_min = 0
        self.intake_score_max = 0
        self.different = 0
        self.utility = utility

    def change_score(self):
        self.intake_score = self.intake_score + 10

    def clear(self):
        self.intake_students = []


    def calculate_different(self):
        self.different = (len(self.intake_students) - self.intake_limit)

    def __str__(self):
        return "No"+str(self.number) + " Score " + str(self.intake_score) + " diff " +  str(self.intake_score_max-self.intake_score_min) #+ " students " + str(self.intake_students)
