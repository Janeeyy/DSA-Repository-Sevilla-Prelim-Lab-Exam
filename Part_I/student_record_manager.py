class Student:
    def __init__(self, student_id, student_name, course, year_level):
        self.student_id = student_id
        self.student_name = student_name
        self.course = course
        self.year_level = year_level

    def display(self):
        print("Student ID:", self.student_id)
        print("Student Name:", self.student_name)
        print("Course:", self.course)
        print("Year Level:", self.year_level)


class DynamicArray:
    def __init__(self):
        self.capacity = 5
        self.count = 0
        self.array = [None] * self.capacity

    def resize(self):
        old_capacity = self.capacity
        new_capacity = old_capacity * 2

        new_array = [None] * new_capacity

        for i in range(self.count):
            new_array[i] = self.array[i]

        self.array = new_array
        self.capacity = new_capacity

        print("Array is full.")
        print("Increasing capacity...")
        print("New capacity:", self.capacity)

    def add(self, student):
        if self.count == self.capacity:
            self.resize()

        self.array[self.count] = student
        self.count += 1

    def get(self, index):
        if index < 0 or index >= self.count:
            return None

        return self.array[index]

    def set(self, index, student):
        if index < 0 or index >= self.count:
            return False

        self.array[index] = student
        return True

    def search(self, student_id):
        for i in range(self.count):
            if self.array[i].student_id == student_id:
                return i

        return -1

    def remove(self, student_id):
        index = self.search(student_id)

        if index == -1:
            return False

       
        for i in range(index, self.count - 1):
            self.array[i] = self.array[i + 1]

        self.array[self.count - 1] = None
        self.count -= 1

        return True

    def size(self):
        return self.count

    def display(self):
        if self.count == 0:
            print("\nNo students found.")
            return

        print("\n===== STUDENT RECORDS =====")

        for i in range(self.count):
            print("\nStudent", i + 1)
            self.array[i].display()

    def display_info(self):
        print("\n===== ARRAY INFORMATION =====")
        print("Number of students:", self.count)
        print("Array capacity:", self.capacity)


def add_student(students):
    print("\n===== ADD STUDENT =====")

    student_id = input("Enter Student ID: ")
    student_name = input("Enter Student Name: ")
    course = input("Enter Course: ")
    year_level = input("Enter Year Level: ")

    if students.search(student_id) != -1:
        print("Student ID already exists.")
        return

    student = Student(
        student_id,
        student_name,
        course,
        year_level
    )

    students.add(student)

    print("Student added successfully.")


def search_student(students):
    print("\n===== SEARCH STUDENT =====")

    student_id = input("Enter Student ID: ")

    index = students.search(student_id)

    if index == -1:
        print("Student not found.")
    else:
        print("\nStudent found:")
        students.get(index).display()


def update_student(students):
    print("\n===== UPDATE STUDENT =====")

    student_id = input("Enter Student ID: ")

    index = students.search(student_id)

    if index == -1:
        print("Student not found.")
        return

    print("\nEnter new information.")

    student_name = input("Enter Student Name: ")
    course = input("Enter Course: ")
    year_level = input("Enter Year Level: ")

    updated_student = Student(
        student_id,
        student_name,
        course,
        year_level
    )

    students.set(index, updated_student)

    print("Student updated successfully.")


def remove_student(students):
    print("\n===== REMOVE STUDENT =====")

    student_id = input("Enter Student ID: ")

    if students.remove(student_id):
        print("Student removed successfully.")
    else:
        print("Student not found.")


def show_menu():
    print("\n================================")
    print("      STUDENT RECORD MANAGER")
    print("================================")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Remove Student")
    print("6. Display Array Information")
    print("7. Exit")
    print("================================")


def main():
    students = DynamicArray()

    while True:
        show_menu()

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student(students)

        elif choice == "2":
            students.display()

        elif choice == "3":
            search_student(students)

        elif choice == "4":
            update_student(students)

        elif choice == "5":
            remove_student(students)

        elif choice == "6":
            students.display_info()

        elif choice == "7":
            print("\nThank you for using Student Record Manager!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()