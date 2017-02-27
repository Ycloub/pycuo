import os
def read_file_lines(filename,salt=''):
    result = []
    if os.path.isfile(filename):
            try:
                file = open(filename,'r')
                for line in file.readlines():
                    line=line.strip()+salt
                    result.append(line)
            except:
                print(filename + 'file can not read .')
            finally:
                file.close()
    else:
        print(filename + 'file not found .')
        exit()
    return result