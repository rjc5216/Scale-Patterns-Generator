"""
Todo:
- Octave stuff: need to incorporate octave numbers to follow the steps in the pattern
- slurs over each segment?
"""


from scale_class import Scale
from music21 import stream, note, meter


def display_pattern(pattern_list):
    """
    Displays the given pattern in musescore using music21.
    :param pattern_list: a list of lists, where each inner list is one segment in the pattern
    :return: None
    """
    s = stream.Stream()

    segment_length = len(pattern_list[0])
    time_sig = meter.TimeSignature(f'{segment_length}/8')
    s.append(time_sig)
    for segment in pattern_list:
        for pitch in segment:
            s.append(note.Note(pitch, quarterLength=0.5))
    s.show()


def create_user_pattern(scale_object):
    name = input('Enter pattern name: ')
    starting_note = input(f'Enter the starting note of the pattern, which must be one of the following:'
                          f'\n{" ".join(scale_object.notes)}\n').upper()
    starting_octave = int(input('Enter the starting octave number: '))
    pattern_sequence = [int(i) for i in input('Enter the pattern sequence '
                                              'as a list of space-separated integers: ').split()]
    scale_object.create_pattern(name, pattern_sequence, starting_note, starting_octave)
    pattern_list = scale_object.patterns[name]
    print(pattern_list)
    display_pattern(pattern_list)


def main():
    print('*'*90)
    print('Welcome to the scale pattern generator.\nPatterns are generated using pattern sequences, which are lists of '
          'integers that describe how many steps up or down to take at each point in the sequence.\nAvailable scale '
          'types:\n- Major\n- Minor\n- Major Pentatonic \n- Minor Pentatonic\n- Whole Half Diminished'
          '\n- Half Whole Diminished\n- Chromatic\n- Augmented')
    root = input('Enter the key/root note: ')
    tonality = input('Enter the tonality/scale type: ')
    scale_object = Scale(root, tonality)
    while True:
        create_user_pattern(scale_object)
        ans = input('Create new pattern? (enter yes or no) ')
        if ans.lower() == 'no':
            break


main()
