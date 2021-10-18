# Pangram
# Determine if a sentence is a pangram. A pangram (Greek: παν γράμμα, pan gramma,
# "every letter") is a sentence using every letter of the alphabet at least once.
# The best known English pangram is:
# > The quick brown fox jumps over the lazy dog.


alphabet = "abcdefghijklmnopqrstuvwxyz"
def is_pangram(sentence):
    if len(sentence)<26:
        return False
    else:
        result =[]
        for character in sentence.lower():
            if character in alphabet and character not in result:
                result.append(character)
        return len(result) ==26
