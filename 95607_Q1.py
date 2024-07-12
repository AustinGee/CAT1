# Define the patient management system

def add_patient(name, age, illness, patient_list):
    patient = {'name': name, 'age': age, 'illness': illness}
    patient_list.append(patient)
    print(f'Patient {name} added successfully.')

def display_patients(patient_list):
    if not patient_list:
        print("No patients in the list.")
    else:
        print("List of patients:")
        for patient in patient_list:
            print(f"Name: {patient['name']}, Age: {patient['age']}, Illness: {patient['illness']}")

def search_patient(name, patient_list):
    for patient in patient_list:
        if patient['name'] == name:
            print(f"Patient {name} found - Age: {patient['age']}, Illness: {patient['illness']}")
            return
    print(f"Patient {name} not found.")

def remove_patient(name, patient_list):
    for patient in patient_list:
        if patient['name'] == name:
            patient_list.remove(patient)
            print(f"Patient {name} removed successfully.")
            return
    print(f"Patient {name} not found.")

# Main program
patients = []

while True:
    print("\nHospital Patient Management System")
    print("1. Add a new patient")
    print("2. Display all patients")
    print("3. Search for a patient by name")
    print("4. Remove a patient by name")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        name = input("Enter patient's name: ")
        age = input("Enter patient's age: ")
        illness = input("Enter patient's illness: ")
        add_patient(name, age, illness, patients)

    elif choice == '2':
        display_patients(patients)

    elif choice == '3':
        name = input("Enter patient's name to search: ")
        search_patient(name, patients)

    elif choice == '4':
        name = input("Enter patient's name to remove: ")
        remove_patient(name, patients)

    elif choice == '5':
        print("Exiting the program. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
