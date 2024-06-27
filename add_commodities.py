# Define the input and output file names
file_A = 'global_swapped.ini'
file_B = 'global_en.ini'
file_output = 'global_added.ini'

# Read the content of file A
with open(file_A, 'r', encoding='utf-8') as f:
    lines_A = f.readlines()

# Read the content of file B and store the relevant lines in a dictionary
translations = {}
with open(file_B, 'r', encoding='utf-8') as f:
    lines_B = f.readlines()
    for line in lines_B:
        if 'items_commodities' in line and '_desc' not in line:
            key = line.split('=')[0].strip()
            translations[key] = line.strip()

# Replace the lines in file A with the corresponding lines from file B
new_lines = []
for line in lines_A:
    if 'items_commodities' in line and '_desc' not in line:
        key = line.split('=')[0].strip()
        if key in translations:
            new_lines.append(line.strip('\n') + '[' + translations[key].split('=')[1] + ']' + '\n')
        else:
            new_lines.append(line)
    else:
        new_lines.append(line)

# Write the modified content to the output file
with open(file_output, 'w', encoding='utf-8') as f:
    f.writelines(new_lines)

print("save to:", file_output)
