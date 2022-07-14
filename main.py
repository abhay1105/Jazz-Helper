from display import display
from chords import get_major_triad
from note_player import play_notes
from scales import get_scale_from_root_note

triad = get_major_triad("G")
scale = get_scale_from_root_note("Bb")

temp = triad

display(temp)
play_notes(temp, 1)