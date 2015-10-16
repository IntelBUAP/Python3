#! /usr/bin/python3

import validapass as vp
import validauser as vu

if (vu.vuser() and vp.vpass()):
    print ("exito", end='\n')
