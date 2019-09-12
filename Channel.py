from tkinter import Y , Listbox

import Tempfile
from venv.Framescreen import F


def New_listscreen() :
    scroll1 = Tempfile.Scrollbar ( F )
    scroll1.pack ( side = Tempfile.RIGHT , fill = Y )
    ## List box with scroll on right side ##
    Lb: Listbox = Tempfile.Listbox ( Tempfile.F , width = 40 , height = 10 , borderwidth = 2 ,
                                     yscrollcommand = scroll1.set )
    for i in range ( 1 , 100 ) :
        Lb.insert ( Tempfile.END , "        " )
    Lb.pack ( side = Tempfile.RIGHT , fill = Tempfile.BOTH )
    scroll1.config ( command = Lb.yview )
