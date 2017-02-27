class Page():
    """Presentations in the command line with interactive elements using a markup
        language called pg."""
    def __init__(self,filename):
        import sys
        """Open the file and create the Page, stored in an array"""
        #Store the filename in a string.
        self.filename  = filename
        #Create a temporary Page in array with incorrect formatting
        self.tmppage = []
        #Create the empty Page.
        self.page = []
        #Try to open the file, and read lines to temporary array.
        try:
            with open(self.filename) as f_obj:
                self.tmppage = f_obj.readlines()
                #Clean temp page and write to the real page.
                for line in self.tmppage:

                    self.page.append(line.rstrip())
        #Catch a bunch of errors.
        except FileNotFoundError:
            import sys
            sys.stderr.write("Page: ERROR: the filename doesn't exist.")
            quit()
        except EOFError:
            sys.stderr.write('Page: ERROR: there is a SyntaxERROR in file.')
            quit()
        except IOError:
            sys.stderr.write('Page: Something went wrong with the file.')
            quit()
        except Exception:
            sys.stderr.write('Page: An unknown ERROR occured.')
            quit()

    def disp(self):
        """Display the page. This is the parser for pg markup langauge."""
        import platform
        import os
        import sys
        #Clear the console.
        if platform.system() == 'Darwin' or platform.system() == "Linux":

            os.system('clear')
            os.system(self.page[0])
            self.page.pop(0)
        if platform.system() == "Windows":
            os.system('cls')
            os.system(self.page[0])
            self.page.pop(0)
        #Loop through each list element.
        for line in self.page:
            #If the program has a line in it,
            if line:
                #Find system cmds and execute.
                if line[0] == '@':
                    try:
                        os.system(line[1:])
                    except KeyboardInterrupt:
                        print('You interupted the prgoram!')
                    continue
                #Find Page commands and execute.
                if line[0] == '<':
                    try:
                        #Get cmd, args for the Page command.
                        cmd, args = line[1:].split('/')
                    #Catch if no args specified, or in the incorrect format.
                    except Exception:
                        sys.stderr.write('Page: ERROR: No args specified.')
                    #Create a simple bar divider
                    if cmd == 'bar':
                        try:
                            args = int(args)
                        except ValueError:
                            sys.stderr.write("Page: ERROR: ArgsERROR, Args type specified incorrectly for this command")

                        barstr = ''
                        for i in range(args):
                            barstr = barstr + '_'
                        print(barstr)
                    #Used for text transitions.
                    if cmd == 'inp':
                        input()

                    #Creates a new page within the file.
                    if cmd == 'npg':
                        import os
                        import platform
                        #Set up new page within OS.
                        if platform.system() == "Linux" or "Darwin":

                            os.system('clear')
                            os.system('setterm -term linux -back default -fore default -clear')
                        if platform.system() == "Windows":
                            os.system('clear')
                            os.system('color')

                    continue



            print(line)

        if platform.system() == "Windows":

            os.system('color')
        if platform.system() == "Linux":
            os.system("setterm -term linux -default black -fore default -clear")
