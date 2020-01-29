import os
import hashlib
from  conf import setting
class User:
    def __init__(self,name):
        self.name=name
        self.home=os.path.join(setting.home_path,name)
        self.cur_path=self.home
        self.disk_space=setting.space
        self.file_size=0


