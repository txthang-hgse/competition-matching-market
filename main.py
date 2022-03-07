import math
from college import College
from student import Student
from matching_market import Matching_market
import random
import copy

def main():
   # random.seed(2)
    total_cost = 0
    for i in range (0,60):
        colleges_dict = {}
        students_dict = {}
        for college in range(2, 4):
            colleges_dict[college] = College(college // 2, college, 25, 0, college // 2 * 20 + 100)
        for student in range(1, 70):
            students_dict[student] = Student(student, random.randrange(2000, 4000, 1), random.randrange(800, 1500, 1))
        market = Matching_market(colleges_dict,students_dict)

        market.calculate_accepted_score()

        total_cost  += market.get_cost_per_student()

    print(total_cost/(60))
 #   for college in market.colleges_set:
 #       print(college.intake_students)
 #       print(college.cutoff_score)





main()