__version__ = '0.0.1'

import sys
RUNNING_PYTHON_2 = sys.version_info[0] == 2

# Because PyAutoGUI requires PyMsgBox but might be installed on systems
# without tkinter, we don't want a lack of tkinter to cause installation
# to fail. So exceptions won't be raised until the PyMsgBox functions
# are actually called.
TKINTER_IMPORT_SUCCEEDED = True

try:
    if RUNNING_PYTHON_2:
        from Tkinter import *
        from ttk import *
        from ScrolledText import *
    else:
        from tkinter import *
        from tkinter.ttk import *
        from tkinter.scrolledtext import ScrolledText

    rootWindowPosition = '+300+200'

    if TkVersion < 8.0 :
        raise RuntimeError('You are running Tk version: ' + str(TkVersion) + 'You must be using Tk version 8.0 or greater to use PyMsgBox.')

except ImportError:
    TKINTER_IMPORT_SUCCEEDED = False


# set up the main window
root = Tk()
root.title("Regex Seer")
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

mainframe = Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, S, E, W))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

'''
The regex form looks like this (9 rows):

    0) >>> regex = r"""                <view cheatsheet button>
    1) <regex field>
    2) """
    3) >>> haystack_string = """
    4) <haystack string field>
    5) """
    6) >>> flags = 0 | <re.I> | <re.L> | <re.M> | <re.S> | <re.U> | <re.X>
    7) >>> re.compile(regex, flags).<function>(haystack_string)
    8) <matches output>
'''

def openCheatSheet(*args):
  import webbrowser
  webbrowser.open('https://google.com') # TODO - set to html file of cheat sheet

# set up the regex form
row0Label = Label(mainframe, text='>>> regex = r"""')
row0Label.grid(column=0, row=0, sticky=(W, E))

cheatSheetBtn = Button(mainframe, text='Cheat Sheet', command=openCheatSheet)
cheatSheetBtn.grid(column=1, row=0, sticky=(W, E))

regexVar = StringVar()
regexEntry = Entry(mainframe, width=7, textvariable=regexVar)
regexEntry.grid(column=0, row=1, sticky=(W, E), columnspan=2)

row2Label = Label(mainframe, text='"""')
row2Label.grid(column=0, row=2, sticky=(W, E), columnspan=2)

row3Label = Label(mainframe, text='>>> haystack_string = r"""')
row3Label.grid(column=0, row=3, sticky=(W, E), columnspan=2)

haystackVar = StringVar()
haystackEntry = ScrolledText(mainframe, width=7, height=5)
haystackEntry.grid(column=0, row=4, sticky=(W, E), columnspan=2)

row5Label = Label(mainframe, text='"""')
row5Label.grid(column=0, row=5, sticky=(W, E), columnspan=2)

# Row 6 is the Regex Flags row
flagsFrame = Frame(mainframe, padding="3 3 12 12")
flagsFrame.grid(column=0, row=6, sticky=(W, E), columnspan=2)
flagsFrame.columnconfigure(0, weight=1)
flagsFrame.rowconfigure(0, weight=1)

row6Label = Label(flagsFrame, text=">>> flags = 0 | ")
row6Label.grid(column=0, row=0, sticky=W)

reIVar = BooleanVar()
reIVar.set(False)
reIBox = Checkbutton(flagsFrame, text="re.I", variable=reIVar, onvalue=True)
reIBox.grid(column=1, row=0, sticky=W)

row6Sep1Label = Label(flagsFrame, text="|")
row6Sep1Label.grid(column=2, row=0, sticky=W)

reLVar = BooleanVar()
reLVar.set(False)
reLBox = Checkbutton(flagsFrame, text="re.L", variable=reLVar, onvalue=True)
reLBox.grid(column=3, row=0, sticky=W)

row6Sep2Label = Label(flagsFrame, text="|")
row6Sep2Label.grid(column=4, row=0, sticky=W)

reMVar = BooleanVar()
reMVar.set(False)
reMBox = Checkbutton(flagsFrame, text="re.M", variable=reMVar, onvalue=True)
reMBox.grid(column=5, row=0, sticky=W)

row6Sep3Label = Label(flagsFrame, text="|")
row6Sep3Label.grid(column=6, row=0, sticky=W)

reSVar = BooleanVar()
reSVar.set(False)
reSBox = Checkbutton(flagsFrame, text="re.S", variable=reSVar, onvalue=True)
reSBox.grid(column=7, row=0, sticky=W)

row6Sep4Label = Label(flagsFrame, text="|")
row6Sep4Label.grid(column=8, row=0, sticky=W)

reUVar = BooleanVar()
reUVar.set(False)
reUBox = Checkbutton(flagsFrame, text="re.U", variable=reUVar, onvalue=True)
reUBox.grid(column=9, row=0, sticky=W)

row6Sep5Label = Label(flagsFrame, text="|")
row6Sep5Label.grid(column=10, row=0, sticky=W)

reXVar = BooleanVar()
reXVar.set(False)
reXBox = Checkbutton(flagsFrame, text="re.X", variable=reXVar, onvalue=True)
reXBox.grid(column=11, row=0, sticky=W)
# end Regex Flag row


# Row 7 is the match/findall/search function selection row
reFuncFrame = Frame(mainframe, padding="3 3 12 12")
reFuncFrame.grid(column=0, row=7, sticky=(W, E), columnspan=2)
reFuncFrame.columnconfigure(0, weight=1)
reFuncFrame.rowconfigure(0, weight=1)

row7Label = Label(reFuncFrame, text='>>> re.compile(regex, flags).')
row7Label.grid(column=0, row=0, sticky=(W, E))

reFuncVar = StringVar()
reFuncVar.set('search2')

# TODO - There are two 'search' strings because the first one seems to disappear after opening the menu.
reFuncDropdown = OptionMenu(reFuncFrame, reFuncVar, 'search', 'findall', 'match')
reFuncDropdown.grid(column=1, row=0, stick=(W, E))

row7EndLabel = Label(reFuncFrame, text='(haystack_string)')
row7EndLabel.grid(column=2, row=0, sticky=(W, E))
# end match/findall/search function selection row

matchesVar = StringVar()
matchesVar.set('No matches.')
matchesEntry = ScrolledText(mainframe, width=7, height=5)
matchesEntry.grid(column=0, row=8, sticky=(W, E), columnspan=2)




if __name__ == '__main__':
  if not TKINTER_IMPORT_SUCCEEDED:
    sys.exit('tkinter module must be installed to run Regex Seer')

  root.mainloop()

