import os
import tempfile
import json
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--key', help='key')
parser.add_argument('--value', help='value')
args = parser.parse_args()

dict1 = dict()
storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')

def reading():
    with open(storage_path, 'r') as f:
        first = f.readline()
        if first != '':
            return json.loads(first)
        else:
            return {}

def key_val(key,val):
    if key in dict1:
        dict1[key] = val

    with open(storage_path, 'w') as f:
        f.write(json.dumps(dict1))

def main():
    if args.key != '' and args.val != 0:
        print(key_val(args.key, args.val))
    else:
        return(None)