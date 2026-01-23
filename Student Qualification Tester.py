'''Jackson Duchow
Student Qualification Tester
This app request a GPA for a student and tests if they're are eligable for the Honor Roll and Dean's List
'''

print("Welcome to the Student Qualification Tester!\
   \nThis app will determine if a student qualifies for the Honor Roll or Dean's List based on their GPA.")
last_name = input("Please enter the student's last name: ")
while last_name != 'ZZZ':
   if gpa in range(0.0, 4.1):
      first_name = input("Please enter the student's first name: ")
   gpa = float(input("Please enter the student's GPA (0.0 - 4.0): "))
   if gpa in range(0.0, 4.1):
      print("Invalid GPA entered. Please enter a GPA between 0.0 and 4.0.")
   else:
      if gpa >= 3.5:
         print(first_name, last_name, "qualifies for the Dean's List and Honor Roll.")
      elif gpa >= 3.25:
         print(first_name, last_name, "qualifies for the Honor Roll.")
      else:
         print(first_name, last_name, "does not qualify for the Honor Roll or Dean's List.")
      last_name = input("Please enter the student's last name: ")