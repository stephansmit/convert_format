try:
    from .singularity_runner.sinexecuter import *
except:
    from singularity_runner.sinexecuter import *

import os  

class FormatConverter(object):
    def __init__(self):
       self.image_url = 'shub://stephansmit/inkscape_containers:latest'
       self.image_name = 'inkscape_containers_latest.sif'
       self.image_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)),'images')

    def convert_to_wmf(self,inputf_n, outputf_n, bind_dir):
       runner = SinExecuter(self.image_name, self.image_url, self.image_dir)
       cmd = ['inkscape','--file' ,inputf_n, '--export-wmf', outputf_n]
       output = runner.run(cmd,bind_dir)
       for line in output:
           print(line)


