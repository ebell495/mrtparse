#!/usr/local/bin/python3
import atheris
import sys
import io
import os

with atheris.instrument_imports():
    import mrtparse

@atheris.instrument_func
def TestOneInput(data):
    # This throws KeyErrors too often
    try:
        for r in mrtparse.Reader(io.BytesIO(data)):
            pass
    except KeyError:
        pass


atheris.Setup(sys.argv, TestOneInput)
# atheris.instrument_all()
atheris.Fuzz()