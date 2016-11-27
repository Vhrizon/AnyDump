#test




#--------------------------------------------------------------

def Menu():

    print("Now we have your text file, what would you like do do?\n1.Convert to ascii\n2.Close")
    if input() == "1":
        Ascii()
    elif input() == "2":
        f.close()
    else:
        print("ok")
        
#--------------------------------------------------------------

def Start():

    print("please give the directory and name of text file exactly")

    x = input()                                     
                                                
    f = open(x, 'r')                                
                                                
    file_contents = f.read()                        
                                                
    print(file_contents)                            

    Menu()

#--------------------------------------------------------------

def Ascii(file_contents):
    
    asciitime = [ord(c) for c in file_contents]
    str1 = ''.join(str(e) for e in file_contents)
    
    print(asciitime)
    print(len(asciitime))
    print(str1)
    
Start()


