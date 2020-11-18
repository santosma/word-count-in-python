from pathlib import Path

fpath = 'C:/Users/Miguel S/Downloads'
data_folder = Path(fpath)
input_file = data_folder / "rosalind_dna.txt"
output_file = data_folder / "ouput.txt"
reader = open(input_file, 'r')
writer = open(output_file, 'w')

words = reader.read().strip()
letter_count = {}
for word in words:
    letter_count[word] = letter_count.get(word,0) + 1

reader.close()

for w in sorted(letter_count):
    writer.write(str(letter_count[w]) + " ")

writer.close()






