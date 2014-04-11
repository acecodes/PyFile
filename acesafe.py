# AceSafe
# By Ace Eddleman, 2014

import os
import sys
import classes as c


"""Functions"""

# Welcome message
def welcome(name='Brochacho Dawg'):
    print('\nWelcome to your file management program, %s!\n' % name)
    print('What would you like to do? Press 0 to exit.\n')
    x = 1 # Starting point for iterator
    for i in welcome_choices:
        print(x, i, sep='. ')
        x += 1
    try:
        choice = int(input('\nPlease make a selection: '))
        select(choice)
    except:
        print('That is not a valid choice.')
        choice = int(input('\nPlease make a selection: '))
        select(choice)

    # UNCOMMENT FOR DEBUGGING
    # choice = int(input('\nPlease make a selection: '))
    # select(choice)

# Message confirming end of copy activity
def finished():
    print("\nAll done!  Returning to main menu...\n")
    input()
    welcome()

# Message that files are about to be copied
def copy_warn(name):
    print('\n%s files are about to be copied..' % name)
    print('Press any key to continue...\n')
    input()

# Function that executes functions (DirObject routines) in main menu
def select(selection):
    if selection == welcome_choices.index('Copy files to external hard drives')+1:
        copy_warn('External HDs')
        c.Dropbox.routine(c.Files.src, c.ExternalHD1, c.ExternalHD2, subs="Music")
        c.Files.routine(c.ExternalHD1.src, c.ExternalHD2.src, dst_sub='Files')
        c.Files.routine(c.Thumb.src, subs='Documents')
        c.Files.routine(c.Thumb.src, subs='Books\\Calibre')
        c.Files.routine(c.Thumb.src, subs='Programming')
        finished()
    elif selection == welcome_choices.index('Copy bulk files to Dropbox')+1:
        copy_warn('Dropbox')
        c.Files.routine(c.Dropbox.src, subs='Documents')
        c.Files.routine(c.Dropbox.src, subs='Books\\Calibre')
        c.Files.routine(c.Dropbox.src, subs='Programming')
        c.Files.routine(c.Dropbox.src, subs='Photos')
        finished()
    elif selection == welcome_choices.index('Copy Anki files')+1:
        copy_warn('Flashcards')
        print('\nCopying CSS file to GitHub repository...\n')
        os.system("""xcopy /I /E /Y /D "{0}" "{1}" """.format(self.src + '\\' + 'collection.media\\_CSS-Master.css', 'D:\\Files\\Programming\\Github\\AnkiCSS'))
        c.Flashcards.routine(c.Files.src, c.Dropbox.src, c.ExternalHD1.src, c.ExternalHD2.src, c.Thumb.src, dst_sub='Flashcards\\Anki')
        finished()
    elif selection == welcome_choices.index('Copy browser files')+1:
        copy_warn('Browser')
        c.Browser.routine(c.Files.src, c.Dropbox.src, c.ExternalHD1.src, c.ExternalHD2.src, c.Thumb.src, dst_sub='Browsers\\Chrome')
        finished()
    elif selection == welcome_choices.index('Copy server files')+1:
        copy_warn('Server')
        c.Server.routine(c.Files.src, c.Dropbox.src, c.ExternalHD1.src, c.ExternalHD2.src, c.Thumb.src, dst_sub='Documents\\Server')
        finished()
    elif selection == welcome_choices.index('Sync apps')+1:
        c.Apps.routine(c.Files.src, c.Dropbox.src, c.ExternalHD1.src, c.ExternalHD2.src, c.Thumb.src, dst_sub='Apps')
        finished()

# Menu choices
welcome_choices = ['Copy files to external hard drives',
           'Copy bulk files to Dropbox',
           'Copy Anki files',
           'Copy browser files',
           'Copy server files',
           'Sync apps']

"""Start of program"""
if __name__ == '__main__':
    welcome()