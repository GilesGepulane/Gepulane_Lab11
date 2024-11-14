grade_list = []
counter = 1
passed = 0
total = 0

while True:
    grades = input(f"Student Grade {counter}: ")
    if grades == "done":
        break
    elif grades.isalpha():
        print("Must be a number")
        continue
    else:
        if int(grades) > 39 and int(grades) < 101:
            grade_list.append(grades)
            counter +=1
            if int(grades) >= 75:
                passed +=1
        else:
            print("Grade is not valid")
            break

for num in grade_list:
    total += int(num)

if len(grade_list) != 0:
    print("Average Grade:", round(total/len(grade_list), 2))
    print("Passed:", passed)
    print(f"Passing %: {passed/len(grade_list) * 100}%")
    print("Grades:",grade_list)