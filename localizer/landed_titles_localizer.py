from pick import pick

from utility.file_sorter import sort_loc_file
from utility.localizer_utility import select_loc_keys, sort_duplicate_loc_keys, generate_loc_statements


def localize_landed_titles(config):
    duplicate_choice_title = 'Do you want to check for duplicates (will output a large amount of data probably):'
    duplicate_choice_options = ['Yes (Preferred method)',
                                'No (Dangerous if you choose to output statements to mod files)']
    duplicate_choice_option, duplicate_choice_index = pick(duplicate_choice_options, duplicate_choice_title)

    sort_choice_title = 'Do you want to sort the generated loc keys (will sort according to de jure hierarchy):'
    sort_choice_options = ['Yes (Preferred method)', 'No (Manual insertion and sorting will be needed)']
    sort_choice_option, sort_choice_index = pick(sort_choice_options, sort_choice_title)

    output_title = 'Choose your output method:'
    output_options = ['Output statements to ' + config.get('titles_path'),
                      'Output statements to '
                      'an output file',
                      'Exit']
    output_option, output_index = pick(output_options, output_title)

    files = dict()
    files['landed_titles_file'] = config.get('root_path') + config.get('landed_titles_path')
    files['titles_loc_file'] = config.get('root_path') + config.get('localization_path') + config.get(
        'language_path') + config.get('titles_path')
    files['titles_loc_ext_file'] = config.get('output_folder') + config.get('title_loc_output')

    landed_titles_file = open(files.get('landed_titles_file'), encoding='utf8')
    titles_loc_file = open(files.get('titles_loc_file'), encoding='utf8')

    new_loc_keys = select_loc_keys(landed_titles_file, r'(\b(b_|c_|d_|k_|e_)\w+\b)')
    old_loc_keys = select_loc_keys(titles_loc_file, r'(\b(b_|c_|d_|k_|e_)\w+\b)')

    loc_statements = generate_loc_statements(sort_duplicate_loc_keys(new_loc_keys,
                                                                     old_loc_keys)) \
        if duplicate_choice_index == 0 else generate_loc_statements(
        new_loc_keys)
    print('You have titles present in ' + config.get('landed_titles_path') + ' that are not in '
                                                                             'localization. The '
                                                                             'generated '
                                                                             'localization '
                                                                             'statements are as '
                                                                             'follows:'
          if duplicate_choice_index == 0 else 'Did not check duplicates in the localization files, loc statements '
                                              'generated are:')
    print(loc_statements)
    print('')
    print(output_option + ' ----------------------------->')

    titles_loc_file.close()
    if output_index == 0:
        titles_loc_output_file = open(files.get('titles_loc_file'), 'a', encoding='utf8')
        titles_loc_output_file.writelines(loc_statements)
        titles_loc_output_file.close()
        if sort_choice_index == 0:
            sort_loc_file(files.get('titles_loc_file'), 'sort_by_title_type')
        print('Successfully outputted ' + str(len(loc_statements)) + 'localization statements to ' + files.get(
            'titles_loc_file'))

    if output_index == 1:
        titles_loc_output_file = open(files.get('titles_loc_ext_file'), 'w', encoding='utf8')
        titles_loc_output_file.writelines(loc_statements)
        titles_loc_output_file.close()
        if sort_choice_index == 0:
            sort_loc_file(files.get('titles_loc_ext_file'), 'sort_by_title_type')
        print('Successfully outputted ' + str(len(loc_statements)) + ' localization statements to ' + files.get(
            'titles_loc_ext_file'))
