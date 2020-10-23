
#!/usr/bin/env python

import logging
import uproc
import os,pwd # for main:mkdir

class Uproc_cb(object):
    callbacks_dict = None

    def __init__(self):
        # "filename":calbback dictionary
        self.callbacks_dict = { 
            '/state' : self.cb_state, 
            '/file1' : self.cb_file1,
            '/file2' : self.cb_file2
        } 

    def cb_state(self, arg , mode="read"):
        if mode == "read":
            return str.encode("this is read command\n")
        elif arg=="1":
            print("update state to 1")
        elif arg=="2":
            print("update state to 2")
        else:
            print("invalide state opcode")

    def cb_file1(self, arg,mode="read"):
        print ("cb_file1: ",arg)

    def cb_file2(self, arg,mode="read"):
        print ("cb_file2: ",arg)


if __name__ == '__main__':
    print ("uproc_cb example main file")
    logging.basicConfig(level=logging.INFO)
    # os.mkdir( "/var/u1", 0o0755 )
    file_path = '/var/u0'
    if not os.path.exists(file_path):
        os.makedirs(file_path) # creates with default perms 0777
        # uid, gid =  pwd.getpwnam().pw_uid, pwd.getpwnam().pw_gid
        os.chown(file_path, os.getuid(), os.getgid()) 

    fuse = uproc.FUSE(uproc.Memory(), file_path, foreground=True, allow_other=True)
