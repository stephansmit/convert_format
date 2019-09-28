from convert import FormatConverter
import os
convert = FormatConverter()
inputf_n = 'circle.eps'
outputf_n = 'circle.wmf'
bind_dir = os.getcwd()
convert.convert(inputf_n, outputf_n, bind_dir)
