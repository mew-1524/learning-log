file = open("student_notes.txt", "a")

note = input("Enter your note: ")

file.write(note + "\n")

file.close()

print("Note saved successfully!")

print("\nReading all notes...\n")

file = open("student_notes.txt", "r")

print(file.read())

file.close()