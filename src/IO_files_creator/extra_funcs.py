import os

def filter_sol_folder(path_to_folder):
    for file in os.listdir(path_to_folder):
        if file.split('.')[-1] != "out":
            continue
        with open(path_to_folder+'/'+file, 'r') as fd:

            contents = fd.read()
            filtered = "".join(contents.split('FINAL SOLUTION:')[-1].splitlines(True)[2:])

            with open(path_to_folder+'/solutions/'+file, 'w') as fd:
                fd.write(filtered)