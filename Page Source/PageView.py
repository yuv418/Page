
from Page import Page


import sys
def view(page):
    """View multiple Pages."""

    path = page
    path = str(path)
    print(path)
    x = Page(path)
    x.disp()
    input()

for item in sys.argv[1:]:
    view(item)

    
