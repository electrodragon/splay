import os
import subprocess

playlist = ''

username = subprocess.run(['whoami'], stdout=subprocess.PIPE).stdout.decode('utf-8').replace('\n','')

arg_file_path = "/home/"+username+"/.config/.splay/sfile.txt"
arg_file_content = subprocess.run(['cat', arg_file_path], stdout=subprocess.PIPE).stdout.decode('utf-8').replace('\n','')

conf_file_path = "/home/"+username+"/.config/.splay/sconf.txt"
conf_file_content = subprocess.run(['cat', conf_file_path], stdout=subprocess.PIPE).stdout.decode('utf-8').replace('\n','')

os.system("find . | grep -i '{}' > {}".format(arg_file_content,arg_file_path))

content = open(arg_file_path, 'r').read().split("\n")[:-1]

if len(content) == 0:
    print("Nothing Found !")
else:
    for c in content:
        playlist = playlist+("\'"+c+"\' ")
    
    if conf_file_content == 'a':
        os.system('mpv --no-video '+playlist)
    else:
        os.system('mpv '+playlist)

quit()
