# Define the input and output file names
file_A = 'global.ini'
file_B = 'global_en.ini'
file_output = 'global_out.ini'

# Read the content of file A
with open(file_A, 'r', encoding='utf-8') as f:
    lines_A = f.readlines()

# Read the content of file B and store the relevant lines in a dictionary
translations = {}
with open(file_B, 'r', encoding='utf-8') as f:
    lines_B = f.readlines()
    for line in lines_B:
        if 'item_Name' in line or 'Item_Name' in line or 'item_name' in line or 'vehicle_Name' in line or 'vehicle_name' in line or 'flightHUD_Label' in line or ('operatorMode_' in line and 'ui_controlhint_ships' not in line) or 'hud_countermeasure_decoy' in line or 'hud_countermeasure_smokescreen' in line or 'hud_gimbal_mode' in line or 'hud_gyro' in line or 'hud_flt' in line:
            key = line.split('=')[0].strip()
            translations[key] = line.strip()

# Replace the lines in file A with the corresponding lines from file B
new_lines = []
for line in lines_A:
    if 'item_Name' in line or 'Item_Name' in line or 'item_name' in line or 'vehicle_Name' in line or 'vehicle_name' in line or 'flightHUD_Label' in line or ('operatorMode_' in line and 'ui_controlhint_ships' not in line) or 'hud_countermeasure_decoy' in line or 'hud_countermeasure_smokescreen' in line or 'hud_gimbal_mode' in line or 'hud_gyro' in line or 'hud_flt' in line:
        key = line.split('=')[0].strip()
        if key in translations:
            new_lines.append(translations[key] + '\n')
        else:
            new_lines.append(line)
    else:
        new_lines.append(line)

# Write the modified content to the output file
with open(file_output, 'w', encoding='utf-8') as f:
    f.writelines(new_lines)

print("save to:", file_output)
