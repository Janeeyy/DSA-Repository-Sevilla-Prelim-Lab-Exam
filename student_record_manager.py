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
        self.size_value = 0
        self.array = [None] * self.capacity

    def resize(self):
        old_capacity = self.capacity
        self.capacity = self.capacity * 2

        new_array = [None] * self.capacity

        for i in range(self.size_value):
            new_array[i] = self.array[i]

        self.array = new_array

        print("Array is full.")
        print("Capacity increased from", old_capacity, "to", self.capacity)

    def add(self, student):
        if self.size_value == self.capacity:
            self.resize()

        self.array[self.size_value] = student
        self.size_value += 1

        print("Student added successfully.")

    def get(self, index):
        if index < 0 or index >= self.size_value:
            return None

        return self.array[index]

    def search(self, student_id):
        for i in range(self.size_value):
            if self.array[i].student_id == student_id:
                return self.array[i]

        return None

    def update(self, student_id):
        student = self.search(student_id)

        if student is None:
            print("Student not found.")
            return

        print("\nEnter new information:")

        student.student_name = input("Student Name: ")
        student.course = input("Course: ")
        student.year_level = input("Year Level: ")

        print("Student updated successfully.")

    def remove(self, student_id):
        index = -1

        for i in range(self.size_value):
            if self.array[i].student_id == student_id:
                index = i
                break

        if index == -1:
            print("Student not found.")
            return

        # Shift elements to the left
        for i in range(index, self.size_value - 1):
            self.array[i] = self.array[i + 1]

        self.array[self.size_value - 1] = None
        self.size_value -= 1

        print("Student removed successfully.")

    def display(self):
        if self.size_value == 0:
            print("No students found.")
            return

        print("\n===== STUDENT RECORDS =====")

        for i in range(self.size_value):
            print("\nStudent", i + 1)
            self.array[i].display()

    def size(self):
        return self.size_value

    def display_info(self):
        print("\n===== ARRAY INFORMATION =====")
        print("Number of Students:", self.size_value)
        print("Array Capacity:", self.capacity)


def main():
    students = DynamicArray()

    while True:
        print("\n================================")
        print("     STUDENT RECORD MANAGER")
        print("================================")
        print("1. Add Student")
        print("2. Display Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Remove Student")
        print("6. Display Array Information")
        print("7. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            print("\n===== ADD STUDENT =====")

            student_id = input("Student ID: ")
            student_name = input("Student Name: ")
            course = input("Course: ")
            year_level = input("Year Level: ")

            student = Student(
                student_id,
                student_name,
                course,
                year_level
            )

            students.add(student)

        elif choice == "2":
            students.display()

        elif choice == "3":
            student_id = input("\nEnter Student ID to search: ")

            student = students.search(student_id)

            if student is not None:
                print("\n===== STUDENT FOUND =====")
                student.display()
            else:
                print("Student not found.")

        elif choice == "4":
            student_id = input("\nEnter Student ID to update: ")
            students.update(student_id)

        elif choice == "5":
            student_id = input("\nEnter Student ID to remove: ")
            students.remove(student_id)

        elif choice == "6":
            students.display_info()

        elif choice == "7":
            print("\nThank you for using Student Record Manager!")
            break

        else:
            print("Invalid choice. Please try again.")


main()