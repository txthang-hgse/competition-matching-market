#from college import College
import math

class Student():
    def __init__(self,student_number,budget,ability):
        self.student_number = student_number
        self.budget = budget
        self.ability = ability
        self.college = None
        self.utility = 0
        self.cost = 0


    def clear(self):
        self.utility = 0
        self.cost = 0
        self.college = None
    def choose_college(self, college_set):
        self.utility = 0
        self.college = None
        for college in college_set:
            cost = 0
            if self.ability < college.intake_score < self.ability + math.log(self.budget-college.tuition):
                cost = math.exp(college.intake_score-self.ability)
            elif college.intake_score > self.ability + math.log(self.budget-college.tuition):
                cost = self.budget
            if cost < self.budget-college.tuition:
                if math.log(self.budget-college.tuition-cost) + college.utility > self.utility:
                    self.utility = math.log(self.budget-college.tuition-cost) + college.utility
                    self.college = college
                    self.cost = cost
                elif math.log(self.budget-college.tuition-cost) + college.utility == self.utility:
                    if college.utility > self.college.utility:
                        self.utility = math.log(self.budget - college.tuition - cost) + college.utility
                        self.college = college
                        self.cost = cost


        if self.college is not None:
            self.college.intake_students.append(self.student_number)

    def meritocratic_choose_college(self,colleges_set):
        self.college = None
        for college in colleges_set:
            if self.ability >= college.intake_score:
                if college.utility > self.utility:
                    self.college = college
                    self.utility = college.utility

        if self.college is not None:
            self.college.intake_students.append(self.student_number)



