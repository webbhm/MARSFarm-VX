'''
FileUtil
utilities for saving configuration files
Author: Howard Webb
Date: 2/22/2023
'''


def saveDict(name, file_name, dict):
    # Save dictionary structure
    # name is the variable, file_name is the file, dict is the structure
    #print(values)
    f = open(file_name, 'w+')
    tmp=name+'='+str(dict)
    f.write(tmp)
    f.close()
    
def test():
    print("Test FileUtil")
    struct = {"name":"Foo", "domain":"Bar"}
    saveDict("foo", "/functions/foo.py", struct)
    print("Done")
    
if __name__=="__main__":
    test()    