import argparse

class CommandLine:
    filetype=-1
    filelist=[]
    rev=False
    def __init__(self):
        thehelp= "Here I need to bulid a help message"
        parser = argparse.ArgumentParser(description = "Description for my parser")
        parser.add_argument("-H", "--Help", help = "Example: Help argument", required = False, default = "")
        parser.add_argument("-s", "--SE", help = "Example: Save argument", required = False, default = "")
        parser.add_argument("-p1", "--PE1", help = "Example: Print argument", required = False, default = "")
        parser.add_argument("-p2", "--PE2", help = "Example: Print argument", required = False, default = "")
        parser.add_argument("-o", "--output", help = "Example: Output argument", required = False, default = "")
        parser.add_argument("-r", "--R", help = "If set then we will add the reverse", required = False, default = "", action='store_true')

        argument = parser.parse_args()
        status = False

        if argument.SE and (argument.PE1 or argument.PE2):
            print("The input must be eaither single end file or peire end files but not both")
            print (thehelp)
            exit(0)
        if argument.Help:
            #print("You have used '-H' or '--Help' with argument: {0}".format(argument.Help))
            status = True
        if argument.SE:
            #print("The input is Singel end file ")
            #print ("The input file name is: {0} ".format(argument.SE))
            status = True
            self.filetype=1
            self.filelist.append(argument.SE)
        if argument.PE1:
            #print("You have used '-p' or '--print' with argument: {0}".format(argument.PE1))
            status = True
            self.filetype=2
            self.filelist.append(argument.PE1)
        if argument.PE2:
            #print("You have used '-p' or '--print' with argument: {0}".format(argument.PE1))
            status = True
            self.filetype=2
            self.filelist.append(argument.PE2)

        if argument.output:
            #print("You have used '-o' or '--output' with argument: {0}".format(argument.output))
            status = True
        if argument.R:
            print("You have used '-H' or '--Help' with argument: {0}".format(argument.Help))
            status = True
            self.rev=True

        if not status:
            print("Maybe you want to use -H or -s or -p or -o as arguments ?") 



if __name__ == '__main__':
    app = CommandLine()
