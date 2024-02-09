#  simple function

def fun():
    print(" Welcome TO The Python Programming")

fun()


print("$$$$$$$$$$$$$$$$$$$$")


# FUction with arguments

def sum(a,b):
    print(a+b)
sum( 20,30)    

# another method
def sub(a,b):
    print(a-b)
n = 40
n1 = 60
sub(n,n1)


# by default set argument

def sub(a,b = 5):
    print(a-b)
sub(20)  # 20 is a = 20  and b = 5 by default

# ovverwite default argument
def sub(a,b = 5):
    print(a-b)
sub(20, 10) # now overwrite b = 10 
print("$$$$$$$$$$$$$$$$$$$$")



# Return type function when return keyword is used according to me print the value
def div(a,b=5):
    c = a/b
    return c
n = div(10,2)
print(n)

print("$$$$$$$$$$$$$$$$$$$$")

def add_student_record(records, name, grade):
    """
    Add a student record to the records dictionary.

    Parameters:
    - records (dict): Dictionary containing student records.
    - name (str): Name of the student.
    - grade (int): Grade of the student.

    Returns:
    - None
    """
    records[name] = grade

def print_all_records(records):
    """
    Print all student records in a nice format.

    Parameters:
    - records (dict): Dictionary containing student records.

    Returns:
    - None
    """
    print("Student Records:")
    for name, grade in records.items():
        print(f"Name: {name}, Grade: {grade}")

# Example usage:
student_records = {}
add_student_record(student_records, "Alice", 85)
add_student_record(student_records, "Bob", 90)
add_student_record(student_records, "Charlie", 78)

print_all_records(student_records)
