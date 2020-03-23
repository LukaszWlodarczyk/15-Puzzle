import argparse
parser = argparse.ArgumentParser(description="source file")
parser.add_argument('source_file')
args = parser.parse_args()

dupa = ""
with open(args.source_file, 'r+') as file:
    for line in file:
        dupa = line.replace('[','')
        dupa = dupa.replace(']', '')
        dupa = dupa.replace(',', '')
        dupa = dupa.replace('\'', '')

print(dupa)
with open(args.source_file, 'w') as file:
    file.write(dupa)