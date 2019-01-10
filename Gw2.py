import csv

def open_csv():
    with open("Gradet2.csv") as f:
        reader = csv.reader(f)
        data = list(reader)
        return data

def edit(data):
    selecter_option = int(input("Select Mode [1]EDIT [2]INSERT [3]CALCULATE GPA:  "))
    if selecter_option == 1:
        choose_semeter = input("Please choose semeter : ")
        select_subject = input("Press your subject : ")
        new_subject = input("press your new subject: ")
        new_credit = input("Press your new credit: ")
        new_grade = input("Press your new grade: " )
        for i in range(len(data)):
            if choose_semeter == data[i][0]:
                if data[i][0] == '1' or data[i][0] == '2' or data[i][0] == '3' or data[i][0] == '4' or data[i][0] == '5':
                    if select_subject == str(data[i][1]):
                        data[i][1] = new_subject
                        data[i][2] = new_credit
                        data[i][3] = new_grade

        print("new data", data)
    elif selecter_option == 2:
        insert(data)

    elif selecter_option == 3:
        calculate(data)
    total_grade = 0
    total_credit = 0
    for i in range(len(data)):
        total_credit += int(data[i][2])
        total_grade = total_grade + (convert_to_num(data[i][3]) * int(data[i][2]))
    print('total_credit', total_credit)
    print('total_grade', total_grade)
    GPA = round((total_grade / total_credit),2)
    print("GPAX: ",GPA)
    select_save = input("Choose Y/N for save change?: ")
    if select_save == 'Y' or 'y':
        save(data)
    else:
        print("FINISH!!")
    return

def insert(data):
    print("ADD NEW SUBJECT!")
    #print('d1', data)
    #choose_term = int(input("Press your semeter to add new subject: "))
    add_subject = int(input("You want to add subject : "))
    for i in range(add_subject):
        New_semeter = input("Semeter: ")
        New_subject = input("Subject: ")
        New_credit = input("Credit: ")
        New_Grade = input("Grade: ")
        data.append([New_semeter,New_subject,New_credit,New_Grade])
        data.sort()
    print("add new subject: ", data)


def save(data):
    with open("newgragechange1.csv", 'w', newline="") as csvfile:
        fieldnames = ['Semeter','Subject','Credit','Grade']
        file = csv.DictWriter(csvfile, fieldnames= fieldnames)
        file.writeheader()
        for i in range(len(data)):
            file.writerow({'Semeter': data[i][0],'Subject': data[i][1], 'Credit': data[i][2], 'Grade': data[i][3]})
    print("Save newfile success!")
    return


# def calculate(data):
#     TERMGPA = 0
#     term_grade = 0
#     term_credit = 0
#     select_semeter_data = input("Please select your semeter:  ")
#     if selecter_option == 3:
#         for i in range(len(basedata)):
#             credit = basedata[i][2]
#             grade = basedata[i][3]
#             if select_semeter_data == basedata[i][0]:
#                 if basedata[i][0] == '1' or basedata[i][0] == '2' or basedata[i][0] == '3' or basedata[i][0] == '4' or basedata[i][0] == '5':
#                     term_credit += int(credit)
#                     term_grade += grade_to_num(grade) * int(credit)
#         TERMGPA = round((term_grade / term_credit),2)
#         print('GPA: ', TERMGPA)



def calculate(data):
    select_semeter_data = input("Please select your semeter for calculate GPA[Number]: ")
    total_credit = 0
    total_grade = 0
    for i in range(len(data)):
        credit = data[i][2]
        grade = data[i][3]
        if (select_semeter_data == data[i][0]):
            if data[i][0] == '1' or data[i][0] == '2' or data[i][0] == '3' or data[i][0] == '4' or data[i][0] == '5':
                total_credit = total_credit + int(credit)
                total_grade = total_grade + (convert_to_num(grade) * int(credit))
    print('term', select_semeter_data)
    print('total_credit', total_credit)
    print('total_grade', total_grade)
    print('total_credit', total_credit)
    GPA = round((total_grade / total_credit),2)
    print('GPA', GPA)
    print("##############################################")


def convert_to_num(int):
    grade = {'A': 4,
             'B+': 3.5,
             'B': 3,
             'C+': 2.5,
             'C': 2,
             'D+': 1.5,
             'D': 1,
             'F': 0}
    return grade[int]

#
# def grade_to_num (str):
#    if(str == 'A'):
#     return 4
#    elif(str == 'B+'):
#     return 3.5
#    elif(str == 'B'):
#     return 3
#    elif(str == 'C+'):
#     return 2.5
#    elif(str == 'C'):
#     return 2
#    elif(str == 'D+'):
#     return 1.5
#    elif(str == 'D'):
#     return 1
#    else:
#     return 0

def main():
    reader = open_csv()
    edit(reader)

if __name__=='__main__':
    main()



