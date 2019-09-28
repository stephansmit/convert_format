from singularity_runner.sinexecuter import *
import os  

class format_converter(object):
    def __init__(self, picture, work_dir):
       self.picture = picture
       self.format = picture.split(".")[-1]
       self.image_url = 'shub://stephansmit/inkscape_containers:latest'
       self.image_name = 'inkscape_containers_latest.sif'
       self.image_dir = os.path.join(os.path.realpath(__file__), 'images')

    def convert(self,inputf_n, outputf_n, bind_dir):
       runner = Runner(self.image_name, self.image_url, self.image_dir)
       cmd = ['inkscape' '--file' ,inputf, '--export-emf', outputf]
       runner.run(cmd,bind_dir)


