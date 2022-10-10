import re

from loc_value_func import translate_loc_key_to_values, strip_title_type_modifier


def construct_loc_statement(loc_key):
    return ' ' + loc_key + ':0 "' + translate_loc_key_to_values(strip_title_type_modifier(loc_key)) + '"\n'


def generate_loc_statements(loc_keys):
    loc_statements = []

    for loc_key in loc_keys:
        loc_statements.append(construct_loc_statement(loc_key))

    return loc_statements


def select_loc_keys(unsearched_file, regex_expr):
    lines = unsearched_file.read()
    matches = re.findall(regex_expr, lines)

    return list(zip(*matches))[0]


def sort_duplicate_loc_keys(new_loc_keys, old_loc_keys):
    return set([i for i in new_loc_keys if i not in old_loc_keys])