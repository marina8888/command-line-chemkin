import os

def filter_out(path_to_folder):
    for file in os.listdir(path_to_folder, "w"):
        if file.endswith(".out"):
            file = path.join(self.sol, file)"".join(contents.split('FINAL SOLUTION:')[-1].splitlines(True)[2:])
    with open('./solutions/' + file, 'w') as fd:
        fd.write(filtered)