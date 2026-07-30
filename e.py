class Employee:
    def __init__(self):
        print("Employee hired!")
    def __del__(self):
        print("UH OH THE GRIM REAPER HAS CALLED AND HE IS ASKING FOR THE EMPLOYEE :O")

def create_obj():
        print("Asking employee to work on project...")
        obj = Employee()
        print("Employee finishes project. Project end...")
        return obj

print("Calling employee function...")
obj = create_obj()
print("*phone starts ringing*")