import math
from college import College
from student import Student
from matching_market import Matching_market
import random
import copy

def main():
    random.seed(2)
    colleges_dict = {}
    students_dict = {}
    for college in range(2, 4):
        colleges_dict[college] = College(college // 2, college, 2, 0, college // 2 * 20 + 100)
    for student in range(1, 7):
        students_dict[student] = Student(student, random.randrange(2000, 4000, 1), random.randrange(800, 1500, 1))
    market = Matching_market(colleges_dict,students_dict)
 #   student_list1 = market.get_intake_student_lists()
    print(colleges_dict)
    for college in market.colleges_set:
        print(college.number)


    market.calculate_accepted_score()
    print(market.get_cost_per_student())

    colleges_dict2 = {}
    for college in range(2, 4):
        colleges_dict2[college] = College(college // 2, college, 2, 0, college // 2 * 20 + 100)


    market2 = Matching_market(colleges_dict2,students_dict)
    print(colleges_dict2)

    print(market2.colleges_set)

    for college in market.colleges_set:
        print(college.number)
    market2.calculate_accepted_score()

    print(market2.get_cost_per_student())
    student_list2 = market2.get_intake_student_lists()

  #  print("check")
  #  for i in range (0,1):
  #      college_intake1 = student_list1[i*2] + student_list1[i*2+1]
  #      print(college_intake1)
   #     college_intake2 = student_list2[i * 2] + student_list2[i * 2 + 1]
   #     print(college_intake2)

   #     print(set(college_intake1) - set(college_intake2) )







main()