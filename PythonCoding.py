from pathlib import Path

fpath = 'C:/Users/Miguel S/Downloads'
data_folder = Path(fpath)
input_file = data_folder / "rosalind_ini6.txt"
output_file = data_folder / "ouput.txt"
reader = open(input_file, 'r')
writer = open(output_file, 'w')

words = reader.read().split()
word_count = {}
for word in words:
    # get the current word key and set its value to 
    # its current value, zero if the word is not in the dictionary, 
    # and add 1
    word_count[word] = word_count.get(word,0) + 1

reader.close()

for w in word_count:
    writer.write(w + " " + str(word_count[w]) + '\n')

writer.close()






