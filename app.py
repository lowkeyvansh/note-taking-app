notes = []

def add_note():
    note = input("Enter your note: ")
    notes.append(note)

def view_notes():
    for i, note in enumerate(notes):
        print(f"{i + 1}. {note}")

while True:
    action = input("Choose action (add, view, exit): ").lower()
    if action == 'add':
        add_note()
    elif action == 'view':
        view_notes()
    elif action == 'exit':
        break
    else:
        print("Invalid action")
