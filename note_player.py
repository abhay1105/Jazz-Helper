import musicalbeeps

player = musicalbeeps.Player(volume = 0.3, mute_output = False)

def play_notes(note_array, note_duration):
    for note in note_array:
        player.play_note(note, note_duration)