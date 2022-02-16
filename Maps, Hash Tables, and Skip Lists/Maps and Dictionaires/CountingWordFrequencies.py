"""The following algorithm will use a dictionary to count the most frequent word appearing in
Moby Dick"""

freq = {}

# Goes through all of the words in mobydick and stores/incrememnts the count
for piece in (
    open("Maps, Hash Tables, and Skip Lists/Maps and Dictionaires/mobydick.txt")
    .read()
    .lower()
    .split()
):
    # Only consider alphabetic characters within this piece
    word = "".join(c for c in piece if c.isalpha)
    if word:  # require at least one alphabetic character
        freq[word] = 1 + freq.get(word, 0)

# Goes through our dictionary and keeps track of key with the highest value
max_word = ""
max_count = 0
for (w, c) in freq.items():
    if c > max_count:
        max_word = w
        max_count = c

print(
    f"The most frequent word in Moby Dick is: {max_word} \n which shows up {max_count} times"
)
