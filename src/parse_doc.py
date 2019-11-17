import csv
import textract
import re
import sys

def main(doc_name, results_file):
    text = textract.process(doc_name)
    lines = text.decode('utf-8').splitlines()

    fp = open(results_file, 'w+', newline='')
    writer = csv.writer(fp)

    fields = ['iteration', 'accuracy', 'ppl', 'xent', 'lr']

    output = []

    for line in lines:
        print(line)
        temp = []
        matches = re.findall('(\d+)\/(\d+);[ ]*acc:[ ]*(\d+)\.(\d+);[ ]*ppl:[ ]*(\d+)\.(\d+);[ ]*xent:[ ]*(\d+)\.(\d+);[ ]*lr:[ ]*(\d+)\.(\d+)', line)

        if matches:
            temp.append(matches[0][0])
            temp.append('{}.{}'.format(matches[0][2],matches[0][3]))
            temp.append('{}.{}'.format(matches[0][4],matches[0][5]))
            temp.append('{}.{}'.format(matches[0][6],matches[0][7]))
            temp.append('{}.{}'.format(matches[0][8],matches[0][9]))

            output.append(temp)

    writer.writerow(fields)
    writer.writerows(output)

    fp.close()

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print('usage:\tparse_doc.py <doc_name> <result_file>')
        sys.exit(0)

    main(sys.argv[1], sys.argv[2])

