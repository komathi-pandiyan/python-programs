def check_starts_ends_with_gfg(s):
    lower_s = s.lower()
    if lower_s.startswith('gfg') and lower_s.endswith('gfg'):
        return 'Yes'
    else:
        return 'No'
input_str = 'gFgabcdEGfG'
output = check_starts_ends_with_gfg(input_str)
print(output)
