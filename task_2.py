max_bad_grades = int(input())

bad_grades_count = 0
total = 0
problems_count = 0
last_problems = None

while bad_grades_count < max_bad_grades:
    problem = input()
    if problem == "Enough":
        break
    grade = int(input())
    if grade <= 4:
        bad_grades_count += 1

    total += grade
    problems_count += 1
    last_problems = problem

if bad_grades_count == max_bad_grades:
    print(f"You need a break, {bad_grades_count} poor grades.")
else:
    average = total / problems_count
    print(f"Average score: {average:.2f}")
    print(f"Number of problems: {problems_count}")
    print(f"Last problem: {last_problems}")
