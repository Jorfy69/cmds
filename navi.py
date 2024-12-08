import sys
import subprocess
import os



base_dir = r'D:\programming\\'
cmds = ['open', 'list']
def main():
    inputs = sys.argv[1:]
    comand_input = inputs[1]
    
    project = os.path.join(base_dir, inputs[0])

    if comand_input in cmds:
        if comand_input == 'open':
            subprocess.Popen(["powershell.exe","-Command", f"code '{project}'" ])
        
    else:
            print('Command not found')


    ## make a list of all files in the directory and its subdirectories
    
    
if __name__ == '__main__':
    main()
