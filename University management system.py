#university management system

from abc import ABC ,abstractmethod
class person(ABC):
    def __init__(self,name ,college_name, id_no):
        self.name=name
        self.college_name=college_name
        self.id_no=id_no
        
    @abstractmethod
    def get_role(self):
       pass
    def basic_details(self):
        print(f"Name : {self.name}")
        print(f"college :{self.college_name}")
        print(f"ID :{self.id_no}")
class student(person):
    def __init__(self,name,college_name,id_no,dept):
        super().__init__(name,college_name,id_no)
        self.dept=dept

    def get_role(self):
        print(f"role  : student")
    def student_details(self):
        super().basic_details()
        self.get_role()
        print(f"dept :{self.dept}")
class teaching_staff(person):
    def __init__(self,name,college_name,id_no,dept,subject):
        super().__init__(name,college_name,id_no)
        self.dept=dept
        self.subject=subject
    def get_role(self):
        print(f"role :professor")
    def staff_details(self):
        super().basic_details()
        self.get_role()
        print(f"Dept  :{self.dept}")
        print(f"subject : {self.subject}")

class nonteaching_staff(person):
    def __init__(self,name,college_name,id_no,sport_dept):
        super().__init__(name,college_name,id_no)
        self.sport_dept= sport_dept
    
    def get_role(self):
        print(f"role :non teaching staff")
    def staff_details(self):
        super().basic_details()
        self.get_role()
        print(f"Dept  :{self.sport_dept}")
class university:
    university_name ="JNTUK"
    def __init__(self):
        self.students=[]
        self.teaching_staff=[]
        self.nonteaching_staff=[]
    def add_person(self,person):
        if isinstance(person,student):
            self.students.append(person)
        if isinstance(person,teaching_staff):
            self.teaching_staff.append(person)
        if isinstance(person,nonteaching_staff):
            self.nonteaching_staff.append(person)

    def remove_person(self,person):
        if isinstance(person,student):
            self.students.remove(person)
        if isinstance(person,teaching_staff):
            self.teaching_staff.remove(person)
        if isinstance(person,nonteaching_staff):
            self.nonteaching_staff.remove(person)
    def candiadate_details(self):
        print("***STUDENT***")
        if self.students:
            for student in self.students:
                student.student_details()
                print("============================")
        else:
            print("No subject yet")

        print("**TEACHING STAFF***")
        if self.teaching_staff:
            for staff in self.teaching_staff:
                staff.staff_details()
                print("=============================")
        else:
            print("NO staff yet")

        print("**NON TEACHING STAFF***")
        if self.nonteaching_staff:
            for staff in self.nonteaching_staff:
                staff.staff_details()
                print("=============================")
        else:
            print("NO staff yet")
            
    @classmethod
    def university_details(cls):
        print(f" university :{cls.university_name}")
    @staticmethod
    def greet():
        print("Welcome to university management System")
        
def main():
    u=university()
    u.greet()
    while True:
        print("choose any option from the following :")
        print("1.student registration : ")
        print("2.faculty registration : ")
        print("3.Non -teaching staff registration : ")
        print("4.remove candidate with te ID : ")
        print("5.candidate info : ")
        print("Exit : ")

        choice =int(input("please enter your choice : "))
        
        if choice==1:
            name=input("enter the name of the student : ")
            clg_name=input("enter the college name : ")
            id_no=input("Enter the Id number : ")
            dept=input("Enter the departement : ")
            stu=student(name , clg_name, id_no ,dept)
            
            u.add_person(stu)
            print("student enrolled successfully")
            
        elif choice==2:
            name=input("Enter the staff name : ")
            clg_name=input("enter the college name : ")
            id_no=input("Enter the Id number of staff: ")
            dept=input("Enter the departement :")
            sub=input("Enter the subject : ")
            
            staff=teaching_staff(name,clg_name,id_no,dept,sub)
            u.add_person(staff)
            print("STAFF DETAIS ADDED SUCCESSFULLY")
            
        elif choice==3:
            name=input("Enter the staff name : ")
            clg_name=input("enter the college name :")
            id_no=input("Enter the Id number of staff:")
            sport_dept=input("Enter the subject :")
            
            staff=nonteaching_staff(name,clg_name,id_no,sport_dept)
            
            u.add_person(staff)
            print("NON STAFF DETAILS SUCCESSUFULLY")
            
        elif choice==4:
            print("SELECT THE CATEGORY :")
            print("1.STUDENT")
            print("2.TEACHINF STAFF")
            print("3.NON TEACHINF STAFF")

            category =int(input("Enter your choice : "))
            if category ==1:
                input_id=input("enter the id number :")
                for i in u.students:
                      if i.id_no == input_id:
                          u.remove_person(i)
                          print("DETAILS REMOVED SUCCESSFULLY")
                          break
                      else:
                          print("NO STUDENT WITH THAT ID NUMBER :")
            if category ==2:
                input_id =input("Enter the Teaching staff ")
                for i in u.teaching_staff:
                    if i.id_no==input_id:
                        u.remove_person(i)
                        print("DETAILS REMOVED SUCCESUFFLY")
                        break
                    else:
                        print("NO STUDENT WITH THAT ID NUMBER :")
            if category ==3:
                input_id =input("Enter THE NON Teaching staff ")
                for i in u.nonteaching_staff:
                    if i.id_no ==input_id :
                        u.remove_person(i)
                        print("DETAILS REMOVED SUCCESUFFLY")
                        break
                    else:
                        print("NO STUDENT WITH THAT ID NUMBER :")
        elif choice==5:
            u.candiadate_details()
        elif choice==6:
            print("====Thank you=====")
        else:
            print("  not yet")
main()
        





        
        
        
        
