from configparser import ConfigParser


# Read configuration.ini file and spit out a dictionary with all the values.
def read_config_file():
    parser = ConfigParser()
    parser.read('config/configuration.ini')

    d = dict()
    d['root_path'] = parser.get('mod_folder', 'root_path')
    d['landed_titles_path'] = parser.get('mod_folder', 'landed_titles_path')
    d['localization_path'] = parser.get('localization_folder', 'localization_path')
    d['language_path'] = parser.get('localization_folder', 'language_path')
    d['titles_path'] = parser.get('localization_folder', 'titles_path')
    d['output_folder'] = parser.get('output_folder', 'output_path')
    d['title_loc_output'] = parser.get('output_folder', 'title_loc_output')

    return d
