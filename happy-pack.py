#!/usr/bin/python
import os

# zip these
MAP_NAME = "dance"
NEX_DATA_DIR = "/home/derek/.nexuiz/data/"

directories =  ['./maps', './models', './scripts', './sound', './textures', './env']

try: 
    import sys
    if sys.argv[1] == "setup":
        for d in directories:
            os.system('mkdir %s' % d)
    print "Creating directories: ", directories
except:
    print "All set."


cmd1 = "cp %s.map %s.bsp ./maps" % (MAP_NAME, MAP_NAME)
cmd2 = "zip -9rv %s.zip " %(MAP_NAME) + ' '.join(directories)
cmd3 = "mv %s.zip %s.pk3" % (MAP_NAME, MAP_NAME)
cmd4 = "ln -fs %s/%s %s" % (os.getcwd(), MAP_NAME + '.pk3', NEX_DATA_DIR)
cmd5 = "cp %s.pk3 map-ctf_%s.pk3" % (MAP_NAME, MAP_NAME)
cmd6 = "ln -fs %s/map-ctf_%s %s" % (os.getcwd(), MAP_NAME + '.pk3', NEX_DATA_DIR)
def do_cmd(cmd):
    print "-------------------------------------------------"
    print "Executing:", cmd
    print os.popen(cmd).read()

map(do_cmd, (cmd1, cmd2, cmd3, cmd4, cmd5, cmd6))


