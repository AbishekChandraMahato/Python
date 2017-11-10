


def comm(file1,file2):
    """
    Mahato Abishek
    Metropolia University of Applied Sciences
    Assignment 6: Files
    03.02.2017
    """
    c=0
    if(file1.split('.')[-1]=='py' and file2.split('.')[-1]=='py'):
        handl1=open('EX5_MahatoAbishek.py','r')
        handl2=open('Ex4_MahatoAbishek.py','w')
        for line in handl1:
            if(line.startswith('#')):
                handl2.write(line)
                c=c+1
        handl1.close()
        handl2.close()
        return ("Number of comments written:%d"%(c))
    else:
        return (" Error:%d, \".py file not found\""%(-1))    
        
            
    
    
    
    
    
    
    
    
    
    
    
    
    
    
a=comm('EX5_MahatoAbishek.p','Ex4_MahatoAbishek.py')
print(a)