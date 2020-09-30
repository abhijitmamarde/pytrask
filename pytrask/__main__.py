# when package/module called direction:
# python -m pytrask
# execute the following, ie execute pytraskgui

from pytrask.src.pytraskgui import *

# same as in pytraskgui.py
import argparse
parser = argparse.ArgumentParser()

parser.add_argument('-e', '--embedded', action='store_true', help="shows application in its own windows (versus flask web page)")
parser.add_argument('-t', '--text-editor', dest='editor', help="Choose which editor will open your trasks: {}. Default is vscode".format(list(supported_editor.keys())))
parser.add_argument('-f', '--files', dest='files', nargs='+', help="Add path of files to analyse")
parser.add_argument('-d', '--dir', dest='directory', default='.', help="Add path of directory to analyse")
parser.add_argument('-nr', '--non-recursive', dest='nonrecursive', action='store_true', help="Make directory (-d) analisys non-recursive, recursive by default")

args = parser.parse_args()

if(args.files != None):
    for file in args.files:
        trasker.register_file(file)

if(args.directory != None):
    recursive = not args.nonrecursive
    trasker.register_directory(args.directory, recursive=recursive)

if(args.embedded):
    main(True, args.editor)
else:
    main(False, args.editor)