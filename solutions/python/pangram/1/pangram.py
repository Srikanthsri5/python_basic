def is_pangram(sentence):
    stc = sentence.lower()
    letters = [ch for ch in stc if ch.isalpha()]
    lls = set(letters)
    return len(lls) == 26
