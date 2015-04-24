# -*- coding: utf-8 -*-


questionBank = {
    1 : {
        1: ["what does the following code do?", "​def a(b, c, d): \n    pass", "defines a list and initializes it", "defines a function, which does nothing​", "defines a function, which passes its parameters through", "defines an empty class", 3],
        2: ["what gets printed?", "print type(1/2)", "<type 'int'>", "<type 'number'>", "<type 'float'>", "<type 'double'>", "<type 'tuple'>", 1+1],
        3: ["what is the output of the following code?", "print type([1,2])", "<type 'tuple'>", "<type 'int'>", "<type 'set'>", "<type 'complex'>", "<type 'list'>", 5+1],
        4: ["what gets printed?", "def f(): \n    pass \n    print type(f())", "<type 'function'>", "<type 'tuple'>", "<type 'NoneType'>", "<type 'str'>", "<type 'type'>", 3+1],
        5: ["what should the below code print?", "print type(1J)", "<type 'complex'>", "<type 'unicode'>", "<type 'int'>", "<type 'float'>", "<type 'dict'>", 1+1],
        6: ["what is the output of the following code?", "print type(lambda:None)", "<type 'NoneType'>", "<type 'tuple'>", "<type 'type'>", "<type 'function'>", "<type 'bool'>", 4+1],
        7: ["what is the output of the below program?", "a = [1,2,3,None,(),[],]\nprint len(a)", "syntax error", "4", "5", "6", "7", 4+1],
        8: ["what gets printed?", "print (type(1/2))", "<type 'int'>", "<type 'number'>", "<type 'float'>", "<type 'double'>", "<type 'tuple'>", 1+1],
        9: ["What gets printed?", "d = lambda p: p * 2 \nt = lambda p: p * 3 \nx = 2 \nx = d(x) \nx = t(x)\nx = d(x) \nprint x", "7", "12", "24", "36", "48", 3+1],
        10: ["What gets printed?", "x = 4.5\ny = 2\nprint x//y", "2.0", "2.25", "9.0", "20.25", "21", 1+1]},

    2 : {
        1:["What gets printed?", "nums = set([1,1,2,3,3,3,4]) \nprint len(nums)", "1", "2","4","5","7",3+1],
        2:["What gets printed?", "x = True \ny = False\nz = False \n\nif x or y and z:\n    print 'yes' \nelse:\n    print 'no'", "yes", "no", "fails to compile",1+1],
        3:["What gets printed?", "x = True\ny = False\nz = False\n\nif not x or y:\n    print 1\nelif not x or not y and z:\n    print 2\nelif not x or y or not y and x:\n    print 3\nelse:\n    print 4","1","2","3","4",3+1],
        4:["If PYTHONPATH is set in the environment, which directories are\n searched for modules?", "A) PYTHONPATH directory\n\nB) current directory\n\nC) home directory\n\nD) installation dependent default path","A only","A and D","A, B and C","A, B and D","A,B,C,D",4+1],
        5:["    In python 2.6 or earlier, the code will print error type 1 if \naccessSecureSystem raises an exception of either AccessError type or \nSecurityError type","try:\n    accessSecureSystem()\nexcept AccessError, SecurityError:\n    print 'error type 1'\n\ncontinueWork()","true","false",2+1],
        6:["The following code will successfully print the days and then the months","daysOfWeek = ['Monday', \n              'Tuesday', \n              'Wednesday', \n              'Thursday', \n              'Friday', \n              'Saturday', \n              'Sunday']\n\nmonths = ['Jan', \ \n          'Feb', \ \n          'Mar', \ \n          'Apr', \ \n          'May', \ \n          'Jun', \ \n          'Jul', \ \n          'Aug', \ \n          'Sep', \ \n          'Oct', \ \n          'Nov', \ \n          'Dec']\n\nprint 'DAYS: %s, MONTHS %s' %                     \n    (daysOfWeek, months)","true","false",2+1],
        7:["Assuming python 2.6 what gets printed?","f = None\n\nfor i in range(5):\n    with open('data.txt', 'w') as f:\n        if i > 2:\n            break\n\nprint f.closed","true","false","none",1+1],
        8:["What gets printed?","counter = 1\n\ndef doLotsOfStuff():\n\n    global counter\n\n    for i in (1, 2, 3):\n        counter += 1\n\ndoLotsOfStuff()\n\nprint counter","1","3","4","7","none of the above",3+1],
        9:["What gets printed?","print r'\\nwoow'", "new line then the string: woow","the text exactly like this: r'\\nwoow'","the text exactly like this: \\nwoow","the letter r and then newline then the text: woow","the letter r then the text like this: nwoow",3+1],
        10:["What gets printed?","print \"hello\" 'world'","on one line the text: hello world","on one line the text: helloworld","hello on one line and world on the next line","syntax error, this python program will not run",2+1]},

    3 : {
        1:['What gets printed?','print "\\x48\\x49!" ','\\x48\\x49!', '4849', '4849!','    48    49!','HI!',6],
        2:['What gets printed?','print 0xA + 0xa','0xA + 0xa','0xA 0xa','14','20', '0x20',5],
        3:['What gets printed?','class parent:\n    def __init__(self, param): \n        self.v1 = param \n\nclass child(parent): \n    def __init__(self, param): \n        self.v2 = param \n\n obj = child(11) \n print "%d %d" % (obj.v1, obj.v2) ','None None','None 11','11 None','11 11', 'Error is generated by program',6],
        4:['What gets printed?','kvps  = {"user","bill", "password"} \n\nprint kvps["password"] ','user','bill','password','Nothing. Python syntax error',5],
        5:['What gets printed?','class Account:\n    def __init__(self, id): \n        self.id = id \n        id = 666 \n\nacc = Account(123) \nprint acc.id ','None','123','666','SyntaxError, this program will not run',3],
        6:['What gets printed?','name = "snow storm" \n\nprint "%s" % name[6:8] ','st','sto','to','tor','Syntax Error',4],
        7:['What gets printed?','name = "snow storm" \n\nname[5] = "X" \n\nprint name ','snow storm','snowXstorm','snow Xtorm','ERROR, this code will not run',5],
        8:['Which numbers are printed?','for i in range(2):\n    print i\n\nfor i in range(4,6):\n    print i ','2, 4, 6','0, 1, 2, 4, 5, 6','0, 1, 4, 5', '0, 1, 4, 5, 6, 7, 8, 9','1, 2, 4, 5, 6',4],
        9:['What sequence of numbers is printed?','values = [1, 2, 1, 3]\nnums = set(values)\n\ndef checkit(num):\n    if num in nums:\n        return True\n    else:\n        return False\n\nfor i in filter(checkit, values):\n    print i ','1 2 3','1 2 1 3','1 2 1 3 1 2 1 3','1 1 1 1 2 2 3 3', 'Syntax Error',3],
        10:['What sequence of numbers is printed?','values = [2, 3, 2, 4]\n\ndef my_transformation(num):\n    return num ** 2\n\nfor i in  map(my_transformation, values):\n    print i ','2 3 2 4','4 6 4 8','1 1.5 1 2','1 1 1 2', '4 9 4 16',6]},


    4 : {
        1:["What gets printed?", "names1 = ['Amir', 'Barry', 'Charles', 'Dao'] \nloc = names1.index('Edward') \nprint loc","-1","0","4","Edward","An exception is thrown",6],
        2:["What gets printed?", "import math \n\nprint math.floor(5.5)","5","5.0","5.5","6","6.0",3],
        3:["What gets printed?", "names1 = ['Amir', 'Barry', 'Charles', 'Dao'] \nif 'amir' in names1: \n    print 1 \nelse: \n    print 2","1","2","An exception is thrown",3],
        4:["What gets printed?", "x = 'foo' \ny = 2 \nprint x + y","foo","foo foo","foo 2","2","An exception is thrown",6],
        5:["What gets printed?", "names1 = ['Amir', 'Barry', 'Charles', 'Dao'] \nnames2 = [name.lower() for name in names1] \nprint names2[2][0]","i","a","c","C","An exception is thrown",4],
        6:["What does the code below do?", "sys.path.append('/root/mods')","Changes the location that the python executable is run from","Changes the current working directory","Adds a new directory to seach for python modules that are imported","Removes all directories for mods","Changes the location where sub-processes are searched for after they are launched",4],
        7:["What gets printed?", "numbers = [1, 2, 3, 4] \nnumbers.append([5,6,7,8]) \nprint len(numbers)","4","5","8","12","An exception is thrown",3],
        8:["Which of the following print statements will print all the names in the list on a seperate line", "names = ['Ramesh', 'Rajesh', 'Roger', 'Ivan', 'Nico']","print '\\n'.join(names)","print names.join('\\n')","print names.concatenate('\\n')","print names.append('\\n')","print names.join('%s\\n', names)",2],
        9:["True or false? Code indentation must be 4 spaces when creating a code block.", "if error: \n    # four spaces of indent are used to create the block \n   print '%s' % msg","True","False",3],
        10:["Which of the following data structures can be used with the 'in' operator to check if an item is in the data structure?","in", "list","set","dictionary","None of the above","All of the above",6]}
}