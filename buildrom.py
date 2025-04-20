import itertools
import sys
import csv 

if __name__ == '__main__':
    words = []
    for x in range(515):
        words.append(0)

  
    with open('tt.csv', 'r') as file:
        iter = itertools.islice(file, 2, None)
        csv_reader = csv.DictReader(iter)
        for row in csv_reader:
            words[int(row["ibin"], 2)] = int(row["obin"], 2)
       
    # Write output to control.rom file
    with open('control.rom', 'w') as outfile:
        outfile.write("v2.0 raw\n")
        for x in range(int(512/16)):
            line = ""
            for y in range(16):
                line += f"{words[(x*16)+y]:0>4x} "
            line = line[:-1]  # Remove trailing space
            outfile.write(line + '\n')