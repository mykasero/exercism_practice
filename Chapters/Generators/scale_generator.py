SHARP_PITCHES = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]
FLAT_PITCHES = ["A", "Bb", "B", "C", "Db", "D", "Eb", "E", "F", "Gb", "G", "Ab"]
SHARP_TONICS = ["C", "G", "D", "A", "E", "B", "F#", "a", "e", "b", "f#", "c#", "g#", "d#"]
FLAT_TONICS = ["F", "Bb", "Eb", "Ab", "Db", "Gb", "d", "g", "c", "f", "bb", "eb"]
INTERVALS = {"m": 1, "M": 2, "A": 3}

def validate_interval_steps(intervals: str):
    return all(char in INTERVALS for char in intervals)

def validate_intervals_length(intervals: str):
    return len(intervals) <= 8

def get_pitches(tonic: str):
    if tonic in SHARP_TONICS:
        return SHARP_PITCHES

    elif tonic in FLAT_TONICS:
        return FLAT_PITCHES

    return None
    
class Scale:
    def __init__(self, tonic: str):
        self.tonic = tonic
        self.tonic_capitalized = tonic.capitalize()
        self.pitches = get_pitches(self.tonic)

    def chromatic(self):
        tonic_idx = self.pitches.index(self.tonic_capitalized)
        return self.pitches[tonic_idx:] + self.pitches[:tonic_idx]

    def interval(self, intervals: str):
        if not validate_interval_steps(intervals):
            raise ValueError('The supported intervals are "m", "M" and "A"')

        elif not validate_intervals_length(intervals):
            raise ValueError("Maximum number of intervals is 8")

        else:
            # Shift the scale
            scale = self.chromatic() + [self.tonic_capitalized]
            curr_idx = 0
            result = [self.tonic_capitalized]

            for interval in intervals:
                curr_idx += INTERVALS[interval]
                result.append(scale[curr_idx])

            return result

'''
Instructions
Chromatic Scales
Scales in Western music are based on the chromatic (12-note) scale. This scale can be expressed as the following group of pitches:

A, A♯, B, C, C♯, D, D♯, E, F, F♯, G, G♯

A given sharp note (indicated by a ♯) can also be expressed as the flat of the note above it (indicated by a ♭) so the chromatic scale can also be written like this:

A, B♭, B, C, D♭, D, E♭, E, F, G♭, G, A♭

The major and minor scale and modes are subsets of this twelve-pitch collection. They have seven pitches, and are called diatonic scales. 
The collection of notes in these scales is written with either sharps or flats, depending on the tonic (starting note). 
Here is a table indicating whether the flat expression or sharp expression of the scale would be used for a given tonic:

Key Signature	Major	Minor
Natural	C	a
Sharp	G, D, A, E, B, F♯	e, b, f♯, c♯, g♯, d♯
Flat	F, B♭, E♭, A♭, D♭, G♭	d, g, c, f, b♭, e♭
Note that by common music theory convention the natural notes "C" and "a" follow the sharps scale when ascending and the flats scale when descending.
For the scope of this exercise the scale is only ascending.

Task
Given a tonic, generate the 12 note chromatic scale starting with the tonic.

Shift the base scale appropriately so that all 12 notes are returned starting with the given tonic.
For the given tonic, determine if the scale is to be returned with flats or sharps.
Return all notes in uppercase letters (except for the b for flats) irrespective of the casing of the given tonic.
Diatonic Scales
The diatonic scales, and all other scales that derive from the chromatic scale, are built upon intervals. An interval is the space between two pitches.

The simplest interval is between two adjacent notes, and is called a "half step", or "minor second" (sometimes written as a lower-case "m"). 
The interval between two notes that have an interceding note is called a "whole step" or "major second" (written as an upper-case "M"). 
The diatonic scales are built using only these two intervals between adjacent notes.

Non-diatonic scales can contain other intervals. An "augmented second" interval, written "A", has two interceding notes (e.g., from A to C or D♭ to E) or a 
"whole step" plus a "half step". There are also smaller and larger intervals, but they will not figure into this exercise.

Task
Given a tonic and a set of intervals, generate the musical scale starting with the tonic and following the specified interval pattern.

This is similar to generating chromatic scales except that instead of returning 12 notes, you will return N+1 notes for N intervals. 
The first note is always the given tonic. Then, for each interval in the pattern, the next note is determined by starting from the previous note and skipping 
the number of notes indicated by the interval.

For example, starting with G and using the seven intervals MMmMMMm, there would be the following eight notes:

Note	Reason
G	Tonic
A	M indicates a whole step from G, skipping G♯
B	M indicates a whole step from A, skipping A♯
C	m indicates a half step from B, skipping nothing
D	M indicates a whole step from C, skipping C♯
E	M indicates a whole step from D, skipping D♯
F♯	M indicates a whole step from E, skipping F
G	m indicates a half step from F♯, skipping nothing
'''
# These tests are auto-generated with test data from:
# https://github.com/exercism/problem-specifications/tree/main/exercises/scale-generator/canonical-data.json
