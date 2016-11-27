#--------------------------------------------------------------

# menu needed to have file contents passed into it
# otherwise it wouldn't know about it, variables
# defined in python functions are scoped to that function
def menu(file_contents):

    print("Now we have your text file, what would you like do do?\n1.Convert to ascii\n2.Close")

    # best to make sure we get a string, so we know what we're working with
    input_value = str(raw_input())

    if input_value == "1":
        ascii(file_contents)
    elif input_value == "2":
        f.close()
    else:
        print("ok")
        
#--------------------------------------------------------------

def start():

    print("please give the directory and name of text file exactly")

    # this probably depends on your version of python,
    # input() is python 3 only I think
    # raw_input achieves the same more or less in v2.x
    x = raw_input()                                     

    # this way of using %s to add variables into strings can be helpful
    print('value of x: %s' % (x))

    f = open(x, 'r')                                
                                                
    file_contents = f.read()                        
                                                
    print('file contents %s' % (file_contents))                            

    menu(file_contents)

#--------------------------------------------------------------

def ascii(file_contents):
    
    asciitime = [ord(c) for c in file_contents]
    str1 = ''.join(str(e) for e in file_contents)
    
    print(asciitime)
    print(len(asciitime))
    print(str1)
    
start()


