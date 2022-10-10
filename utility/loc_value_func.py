import re

key_to_val_table = {
    'a__a__': 'â',
    'e__e__': 'ê',
    'i__i__': 'î',
    'o__o__': 'ô',
    'u__u__': 'û',
    'A__A__': 'Â',
    'E__E__': 'Ê',
    'I__I__': 'Î',
    'O__O__': 'Ô',
    'U__U__': 'Û',
    '__AE__': 'Æ',
    '__ae__': 'æ',
    'o__': 'ð',
    'p__': 'Þ',
    'P__': 'þ',
    '__a': 'á',
    '__e': 'é',
    '__i': 'í',
    '__o': 'ó',
    '__u': 'ú',
    '__A': 'Á',
    '__E': 'É',
    '__I': 'Í',
    '__O': 'Ó',
    '__U': 'Ú',
    '__a__a': 'ä',
    '__e__e': 'ë',
    '__i__i': 'ï',
    '__o__o': 'ö',
    '__u__u': 'ü',
    '__A__A': 'Ä',
    '__E__E': 'Ë',
    '__I__I': 'Ï',
    '__O__O': 'Ö',
    '__U__U': 'Ü',
    '_': ' ',
}

value_to_key_table = {v: k for k, v in key_to_val_table.items()}


# This will strip the title type from the loc keys and capitalize them, so we can then search for diacritics
def strip_title_type_modifier(loc_key):
    return re.sub(r'^(b_|c_|d_|k_|e_)', '', loc_key).capitalize().title()


def translate_loc_key_to_values(loc_key):
    # Unholy creation to sub the key/value table values with each other. It hurts me
    return re.sub('({})'.format('|'.join(map(re.escape, key_to_val_table.keys()))),
                  lambda m: key_to_val_table[m.group()], loc_key)


def translate_loc_values_to_keys(loc_value):
    # I need spiritual cleansing after this code, help.
    return re.sub('({})'.format('|'.join(map(re.escape, key_to_val_table.keys()))),
                  lambda m: value_to_key_table[m.group()], loc_value)
