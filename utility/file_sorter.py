def sort_loc_file(file, sort_type):
    file_read = open(file, 'r', encoding='utf8')
    file_lines = file_read.readlines()

    sortable_lines, unsortable_lines = find_sortable_unsortable_lines(file_lines)
    file_read.close()

    if sort_type == 'sort_by_title_type':
        sortable_lines = sort_by_title_type(sortable_lines)
    else:
        sortable_lines = sort_alphabetically(sortable_lines)

    file_write = open(file, 'w', encoding='utf8')

    writable_lines = sortable_lines
    for line_key in unsortable_lines.keys():
        writable_lines.insert(unsortable_lines.get(line_key), line_key)

    file_write.writelines(writable_lines)
    file_write.close()


def find_sortable_unsortable_lines(file_lines):
    unsortable_lines = {}

    for line in file_lines:
        if 'l_english:' in line:
            unsortable_lines[line] = file_lines.index(line)
            file_lines.remove(line)

    return file_lines, unsortable_lines


def sort_alphabetically(file_lines):
    return sorted(file_lines)


def sort_by_title_type(file_lines):
    title_hierarchy = {
        'e': 1,
        'k': 2,
        'd': 3,
        'c': 4,
        'b': 5,
    }
    return sorted(file_lines, key=lambda word: [title_hierarchy.get(c, ord(c)) for c in word])
