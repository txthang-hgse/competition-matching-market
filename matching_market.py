import math


import random
import copy

class Matching_market():
    def __init__(self,colleges_dict,students_dict):
        self.tax = 4

        self.colleges_dict = colleges_dict
        self.colleges_set = set()
        self.students_dict = students_dict
        self.students_set = set()
        self.cutoff_score_max = 0
        self.set_up()
        self.first_turn()


        ### Policy: Taxation:



    def set_up(self):
        for college in self.colleges_dict:
            self.colleges_set.add(self.colleges_dict[college])
        for student in self.students_dict:
            self.students_set.add(self.students_dict[student])

    def check_equilibrium(self):
        check = True
        for college in self.colleges_set:
            if college.different != 0:
                check = False
        return check
    def get_cost_per_student(self):
        cost = 0
        for student in self.students_set:
            cost += student.cost
        return cost/len(self.students_set)

    def get_intake_student_lists(self):
        list = []
    #    for i in range (1,len(self.colleges_set)/2+1):
        for college in self.colleges_set:
            print(college.intake_students)
            list.append(college.intake_students)
        return list





    def run_matching(self):
        for college in self.colleges_set:
            college.clear()
        for student in self.students_set:
            student.clear()
        for student in self.students_set:
            student.choose_college( self.colleges_set, self.tax)
        for college in self.colleges_set:
            college.calculate_different()


    ''' Matching without the influence of income inequality (strict meritocratic)'''
    def meritocratic_matching_Gale_Shapley(self):
        for college in self.colleges_set:
            college.clear()
        for student in self.students_set:
            student.choose_college(self.colleges_set,self.tax)
        for college in self.colleges_set:
            college.calculate_different()

    '''Start of method 2 '''
    def first_turn(self):
        self.cutoff_score_max = 1500 + math.sqrt(4000)

        for college in self.colleges_set:
            college.cutoff_score = self.cutoff_score_max / 2
            college.cutoff_score_max = self.cutoff_score_max

        self.run_matching()



    def find_max_diff(self):
        '''get the college with highest difference'''

        college_max = None
        diff_max = 0

        for college in self.colleges_set:
            if abs(college.different ) > diff_max and college.cutoff_score_max - college.cutoff_score_min > 0.1:
                college_max = college
                diff_max = abs(college.different)

        for college in self.colleges_set:
            if college_max is None:
                if abs(college.different) > diff_max:
                    college_max = college
                    diff_max = abs(college.different)

        return college_max

    def calculate_accepted_score(self):
        count = 0
        while not self.check_equilibrium() and count < 5000:
            college_max = self.find_max_diff()
            if college_max.different < 0:
                temp_score = copy.deepcopy( college_max.cutoff_score)
                college_max.cutoff_score = college_max.cutoff_score_min
                self.run_matching()

                while college_max.different < 0:
                    college_max.cutoff_score_min = college_max.cutoff_score_min -10
                    college_max.cutoff_score = college_max.cutoff_score_min
                    self.run_matching()



                college_max.cutoff_score_max = temp_score
                college_max.cutoff_score = 1/4*college_max.cutoff_score_max + 3/4*college_max.cutoff_score_min
                self.run_matching()
            else:
                temp_score = copy.deepcopy(college_max.cutoff_score)
                college_max.cutoff_score = college_max.cutoff_score_max
                self.run_matching()

                while college_max.different > 0:
                    college_max.cutoff_score_max = college_max.cutoff_score_max +10
                    college_max.cutoff_score = college_max.cutoff_score_max
                    self.run_matching()

                college_max.cutoff_score_min = temp_score
                college_max.cutoff_score = (college_max.cutoff_score_max + college_max.cutoff_score_min) / 2
                self.run_matching()

            count += 1

