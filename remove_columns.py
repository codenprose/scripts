import pandas as pd
from pathlib import Path

# define file paths
INPUT_FP = Path('')
OUTPUT_FP = Path('')

# read file
file = pd.read_csv(INPUT_FP, low_memory=False)

# add name of each column you want to keep
columns = []

# filter list of columns from original file
new_file = file[columns]

# create new csv file
new_file.to_csv(OUTPUT_FP, index=False)
