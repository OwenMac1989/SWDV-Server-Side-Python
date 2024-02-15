import csv
def main():
    courses = [["Python", 3],
               ["Trig", 3],
               ["Physics", 4],
               ["Yoga", 2]]
    with open("courses.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(courses)
    course_list = []
    with open("courses.csv", newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            course_list.append(row)
    for i in range(len(course_list) - 2):
        course = course_list[i]
        print(f"{course[0]} ({course[1]})")
       
main()