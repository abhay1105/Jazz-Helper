from scales import get_scale_from_root_note

def get_scale_degree(scale, degree):
    return scale[degree - 1]

def get_major_triad(root_note):
    major_scale = get_scale_from_root_note(root_note)
    major_triad_degrees = [1, 3, 5]
    major_triad = []
    for degree in major_triad_degrees:
        major_triad.append(get_scale_degree(major_scale, degree))
    return major_triad
