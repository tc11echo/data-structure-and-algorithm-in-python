print("sample module imported") # test only, module shouldn't contain this kind of statement

def func1():
    print("func1 executed")
    
def func2():
    print("func2 executed")
    
if __name__=="__main__": # this like C++ main function, only directly run sample_module.py will run this
    print("sample module main called")
