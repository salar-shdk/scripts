from subprocess import PIPE, Popen
import os 

def cmdline(command):
    process = Popen(
        args=command,
        stdout=PIPE,
        shell=True
    )
    return process.communicate()[0]

def write_catch(current_dir):
    file_data = open(file_path,"r")
    catch =''
    for line in file_data:
        line = line.strip()
        line_arr = line.split('>')
        print(line_arr)
        if len(line_arr) == len(current_dir) + 2  and line[-1] == '>' :
            print(line[-2])
            currect_dir = True
            for dir, target_dir in zip(line_arr[:-1], current_dir):
                if dir != target_dir :
                    current_dir = False
            if not currect_dir : continue
            catch += f'>{line_arr[-2]}>\n'
            
    file_data = open(file_path,"r")
    for line in file_data:
        line_arr = line.split('>')
        
        if len(line_arr) > len(current_dir) + 1 : 
            
            continue
        currect_dir = True
        for dir, target_dir in zip(line_arr[:-1], current_dir):
            if dir != target_dir :
                current_dir = False
        if not currect_dir : continue
        new_line = f'>{line_arr[-1]}'
        
        catch += new_line 

    catch_file = open(catch_path,'w')
    catch_file.write(catch)

def generate_path(target, current_dir):
    key = ''
    for i in current_dir:
        key += f'>{i}'
    key += target
    return key
        
def delete(target, current_dir):
    key = generate_path(target, current_dir)
    file_data = open(file_path,"r")
    data = ''
    for line in file_data:
        if key not in line:
            data += line
    file_data = open(file_path,"w")
    file_data.write(data)

def mkdir(target, current_dir):
    print(target)
    key = generate_path(target, current_dir) + '>\n'
    print(key)
    file_data = open(file_path,"r")  
    duplicate = False
    for line in file_data:
        if key in line:
            duplicate = True
            break
    if not duplicate:
        file_data = open(file_path,"a")
        file_data.write(key)


file_path = '/home/salar/.todo'
catch_path = '/home/salar/.todo_catch'
prompt = 'add/remove task : '


current_dir = ['']

write_catch(current_dir)

height = int(cmdline(f'wc -l {catch_path}').decode().split(' ')[0])

output = cmdline(f'dmenu -l {height} -p \"{prompt}\" < {catch_path}')
while(output):
    output = output.decode().strip()
    print(output)
    if output[:6] == 'mkdir ':
        print(1)
        mkdir(output[6:],current_dir)
        write_catch(current_dir)

    elif output.startswith('rm '):
        delete(output[3:],current_dir)
        write_catch(current_dir)

    elif output == 'cd' :
        current_dir = ['']
        write_catch(current_dir)
    else:
        key = generate_path(output[1:], current_dir)
        file_data = open(file_path,"r")
        new_file = ''
        directory = False
        seen = False
        for line in file_data:
            line = line.strip()
            print(key)
            if key.strip() == line:
                seen = True
                if key[-1] == '>':
                    directory = True
                    current_dir.append(output[1:].split('>')[-2])
                    write_catch(current_dir)
                    #output = cmdline(f'dmenu -l {height} -p \"{prompt}\" < {catch_path}')                    
                else:
                    continue
            else:
                new_file += (line + '\n')
        print(seen,directory)
        if not directory:
            if not seen:
                new_file += key
                height+=1
            file_data = open(file_path,"w")
            file_data.write(new_file)
            file_data.close()
            write_catch(current_dir)


    output = cmdline(f'dmenu -l {height} -p \"{prompt}\" < {catch_path}')

