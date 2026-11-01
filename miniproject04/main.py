#create a record
records={}
def student_record(std_id,name,marks):
    records[std_id] = {
        'name':name,
        'marks':marks
    }
    return dict(records)


#add an valid record
def add_record():
    num = int(input("enter number of student: "))
    student_ids = []
    for i in range(num):
        std_id=input("\nstudent id: ")
        student_ids.append(std_id)
        #to input name 
        name=input("enter name: ")
        #to input python marks btw 0,100
        num_sub = int(input("enter number of subjects: "))
        marks = []
        for num in range(num_sub):
            mark = int(input("enter marks: "))
            while True:
                if 0 <= mark <= 100:
                    break
                else:
                    mark = int(input("invalid marks please re-enter mark: "))
            marks.append(mark)
        records = student_record(std_id,name,marks)
    return records


#for calculate total marks
def calc_total(marks):
    return sum(marks)


#for calculate average of marks
def calc_avg(marks):
    return sum(marks)/len(marks)


#grade calculator
def get_grade(average):
    if average >= 75:
        result = "Distinction"
    elif average >= 60:
        result = "First Division"
    elif average >= 40:
        result = "Pass"
    else:
        result = "Fail"
    return result

#for the use for default arguments
def get_top_performer(records,minimum=75):
    top_performer = []
    for record in records.values():
        marks = record['marks']
        average = sum(marks)/len(marks)
        if average >= minimum:
            top_performer.append(record['name'])
    return top_performer


#to return student record
def std_record():
    for std_id,record in records.items():
        print(f"\n{std_id} | name:{record['name']} | marks:{record['marks']}")
        marks = record['marks']
        total = calc_total(marks)
        avg = calc_avg(marks)
        grade = get_grade(avg)
        print(f"total: {total} | average: {avg} | grade: {grade}")


#filter high performance
#map(lambda)
def class_average(records):
    averages = list(map(lambda student: calc_avg(student['marks']),records.values()))
    class_avg = sum(averages)/len(averages)
    print(f"Class average: {class_avg}")
#filter(lambda)
def get_high_performer(records):
    high_performer_std = list(filter(lambda student: calc_avg(student['marks']) >= 75,records.values()))
    high_performer = list(map(lambda student: student['name'],high_performer_std))
    print(f"High performers (Average >= 75): {high_performer}")


#flexible class summary
#use of (*args)
def average_by_args(*args):
    average = sum(args)/len(args)
    return average

#use of (**kwargs)
#

#recursion
def recursive_sum(n):
    if n <= 0:
        return 0
    return n + recursive_sum(n-1)


#scope demonstration
def print_scope():
    message = "this is local variable"
    print(message)


#main program
records = add_record()
std_record()
print()
#filter(lambda)
#filter high performance
get_high_performer(records)
#map(lambda)
class_average(records)
#argument styles
#positional argument
print()
avg = average_by_args(20,36,40,15)
print("average using positional argument: ",avg)
#keyword argument
avg = calc_avg(marks = [20,36,40,15])
print("Average using keyword argument: ",avg)
#default argument
top_Student = get_top_performer(records)
print(f"top performer by default argument of minimum: {top_Student}")
#recursion
print()
print("recursive sum from 1 to 5",recursive_sum(5))
print("recursive sum from 1 to 7",recursive_sum(7))
print("recursive sum from 1 to 15",recursive_sum(15))
#local variable
print()
print_scope()