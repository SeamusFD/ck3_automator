from pick import pick

from utility.config_initializer import read_config_file
from localizer.landed_titles_localizer import localize_landed_titles


def init():
    print('------------------------------------------------------------------------')
    print('---------------------CK3 Automation Tool v0.1.--------------------------')
    print('------------------------------------------------------------------------')

    title = 'Please choose localization option: '
    options = ['Landed Titles', 'Character Names (History)', 'Character Names (Culture)', 'Duplicate Notifier']

    option, index = pick(options, title)

    print('')
    print('------------------------------------------')
    print('--------------' + option + '--------------')
    print('------------------------------------------')
    print('')

    config = read_config_file()

    if option == 'Landed Titles':
        localize_landed_titles(config)


init()
