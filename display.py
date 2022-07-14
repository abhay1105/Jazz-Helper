def display(note_arrray):
    for note in note_arrray:
        note = note.replace("#", "♯").replace("b", "♭")
    print("\n" + str(note_arrray) + "\n")