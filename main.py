import os

def checkPass(nameIn,passwdIn,namefile):
    fr = open(namefile)
    arrayofLines = fr.readlines()
    numberofLines = len(arrayofLines)
    for line in arrayofLines:
        line = line.strip()
        listFromLine = line.split(':')
        name = listFromLine[0]
        if name == nameIn:
            urName =nameIn
            numberofLines = -1
            passwd = listFromLine[1]
            if passwd == passwdIn:
                print("\n登录成功!\n")
            else:
                print("\n请输入正确的密码!!")
    if numberofLines != -1:
        print("\n请输入正确的用户名!!!")
    fr.close()
    return urName

def signup():
    lo = input('\n你是否已注册(yes/no): ')
    if lo != 'yes' and lo != 'no':
        signup()
    if lo == 'yes':
        return 0
    else:
        nameIn = input("\n注册账户:")
        if nameIn == '':
            print("\n账户名不能为空")
            signup()
        passwdIn = input("\n注册密码:")
        if passwdIn == '':
            print("\n密码不能为空")
            signup()
        str = nameIn+':'+passwdIn+'\n'
        writefile('passwd.txt',str)

def login():
    nameIn = input("\n请输入账户:")
    if nameIn == '':
        login()
    passwdIn = input("\n请输入密码:")
    urName = checkPass(nameIn,passwdIn,'passwd.txt')
    return urName

def touchfile(urName,filename):
    cur_path = os.getcwd()
    print(cur_path)
    new_path = os.path.join(cur_path,urName)
    if os.path.exists(new_path) == False:
        os.mkdir(new_path)
    os.chdir(new_path)
    fr = open(filename,'w')
    fr.close()
    os.chdir(cur_path)

def readfile(filename):
    fr = open(filename)
    arrayofLines = fr.readlines()
    for line in arrayofLines:
        line = line.strip()
        print(line)

def writefile(filename,str):
    fo = open(filename,'r+')
    fo.seek(0,2)
    fo.write(str)

def main():
    signup()
    urName = login()
    print('welcome to the world: '+urName)
    #touchfile('test','test.txt')
    #readfile(filename)

main()