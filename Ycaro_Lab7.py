name = input("Enter name:")
sec = input("Enter section:")
pre = int(input("Enter prelim grade: "))
mid = int(input("Enter midterm grade:"))
fin = int(input("Enter finals grade:"))
finals = pre + mid + fin
new_average = finals // 3
if(new_average <=40 and new_average >=100):
    print("Error")
else:
    if  new_average >=97:
       gpa = "1.00"
    elif new_average >=94:
       gpa = "1.25"
    elif new_average >=91:
       gpa = "1.50"
    elif new_average >=88:
       gpa = "1.75"
    elif new_average >=85:
       gpa = "2.00"
    elif new_average >=82:
       gpa = "2.25"
    elif new_average >=80:
       gpa = "2.50"
    elif new_average>=78:
       gpa = "2.75"
    elif new_average>=75:
       gpa = "3.00"
    else:
       gpa = "5.00"
    print(f"Final Grade: {new_average} Gpa: {gpa} ")
    
    


    
        
    
    

                         

