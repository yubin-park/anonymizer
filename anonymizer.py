import sys
import csv
import hashlib
from tqdm import tqdm

if len(sys.argv) == 1:
    print("usage: python anonymizer.py filename [$'delim']")
    sys.exit()

fn = sys.argv[1]
delim = ","
if len(sys.argv) > 2:
    delim = sys.argv[2]

fn_tokens = fn.split(".")
extension = fn_tokens[-1]
fn_noext = ".".join(fn_tokens[:-1])
fn_out = "{}_anonymized.csv".format(fn_noext)

with open(fn_out, "w") as fp_out:
    writer = csv.writer(fp_out, delimiter=",")
    with open(fn, "r", encoding="ISO-8859-1") as fp:
        reader = csv.reader(fp, delimiter=delim)
        header = next(reader)
        writer.writerow(header)
        print("Select column indices (separated by comma) to hash:")
        for i, col in enumerate(header):
            print(" {}. {}".format(i, col))
        indices = input("(column indices): ")
        try:
            indices = [int(x) for x in indices.split(",")]
        except ValueError:
            print("ERROR: Invalid indices")
            sys.exit()
        for row in tqdm(reader):
            for i in indices:
                row[i] = hashlib.md5(row[i].encode()).hexdigest()
            writer.writerow(row) 

print("INFO: Anonymized data are in {}".format(fn_out))

