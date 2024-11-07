listgrd = []
student_grade = 1 
while student_grade < 4:
    grdinput = int(input(f"Enter student grade {student_grade}: "))
    
    if grdinput == (1):
        break
    
    
    
    if 40 <= grdinput <=100:
      listgrd.append(grdinput)
      student_grade +=1
    else:
     print("Inavlid Grade")
    

    
average = sum(listgrd) / len(listgrd)    
passing = 0
for grdinput in listgrd:
    if grdinput >=75:
        passing += 1
  
pass_percent = (passing / len(listgrd)) * 100
print(f"Grades: ", listgrd)
print(f"Grade Average: ",average)
print(f"Passing:" ,passing)
print(f"Percentage: ", pass_percent)
    

          