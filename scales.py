MAJOR_SCALE_DICTIONARY = {

    "C_MAJOR_SCALE": ["C", "D", "E", "F", "G", "A", "B", "C"],
    "G_MAJOR_SCALE": ["G", "A", "B", "C", "D", "E", "F♯", "G"],
    "D_MAJOR_SCALE": ["D", "E", "F♯", "G", "A", "B", "C♯", "D"],
    "A_MAJOR_SCALE": ["A", "B", "C♯", "D", "E", "F♯", "G♯", "A"],
    "E_MAJOR_SCALE": ["E", "F♯", "G♯", "A", "B", "C♯", "D♯", "E"],

    "F_MAJOR_SCALE": ["F", "G", "A", "B♭", "C", "D", "E", "F"],
    "B_FLAT_MAJOR_SCALE": ["B♭", "C", "D", "E♭", "F", "G", "A", "B♭"],
    "E_FLAT_MAJOR_SCALE": ["E♭", "F", "G", "A♭", "B♭", "C", "D", "E♭"],
    "A_FLAT_MAJOR_SCALE": ["A♭", "B♭", "C", "D♭", "E♭", "F", "G", "A♭"]

}

def get_scale_from_root_note(root_note):
    for scale_title in MAJOR_SCALE_DICTIONARY:
        if root_note + "_" in scale_title:
            return MAJOR_SCALE_DICTIONARY[scale_title]