#------------------------------------------#
# Title: CDInventory.py
# Desc: Working with classes and functions.
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, Created File
# AMalavia, 2022-Mar-06, Assignment06_Starter.py to include IO Functions, and Processing Functions.
#------------------------------------------#

# -- DATA -- #
strChoice = '' # User input
lstTbl = []  # list of lists to hold data
dicRow = {}  # list of data row
strFileName = 'CDInventory.txt'  # data storage file
objFile = None  # file object

# -- PROCESSING -- #
class DataProcessor:
    """Processing the data to and from the runtime memory"""
    
    @staticmethod

    def cd_add(strID, strTitle, strArtist):
        
        """Adding items to our 2D table each time the user wants to add data.
        
        
        Args:
            strID (string): ID for the CD that is to be stored into memory. Converted to string from an int.
            strTitle (string): The title of the CD stored into memory
            strArtist (string): The artist name for the CD stored into memory
            lstTbl (list of lists): 2D data structure that holds the data

        Returns:
            lstTbl: List of lists where it's a 2d data structure with 2 dicRows
        """
        # Add item to the table with the append function
        intID = int(strID)
        dicRow = {'ID': intID, 'Title': strTitle, 'Artist': strArtist}
        lstTbl.append(dicRow)
        return strID, strTitle, strArtist

    @staticmethod
    def cd_delete(lstTbl):
        
        """Function to delete a CD from our CD Collection


        Args:
            lstTbl: 2D data structure (list of dicts) that holds the data during runtime

        Returns:
            lstTbl.
        """
        # Diplays the  CDInventory to the user
        # Gets the User Input for which CD to Delete
        IO.show_inventory(lstTbl)
        intIDDel = int(input('Which ID would you like to delete? ').strip())
        # Search thru table and delete the CD
        intRowNr = -1
        blnCDRemoved = False
        for row in lstTbl:
            intRowNr += 1
            if row['ID'] == intIDDel:
                del lstTbl[intRowNr]
                blnCDRemoved = True
                break
        if blnCDRemoved:
            print('The CD was removed')
        else:
            print('Could not find this CD!')         
        IO.show_inventory(lstTbl)
        return lstTbl
    
class FileProcessor:
    """Processing the data to and from text file"""

    @staticmethod
    def read_file(file_name, table):
        """Function to manage data ingestion from file to a list of dictionaries

        Reads the data from file identified by file_name into a 2D table
        (list of dicts) table one line in the file represents one dictionary row in table.


        Args:
            file_name (string): name of file used to read the data from
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime

        Returns:
            None.
        """
        table.clear()  # this clears existing data and allows to load data from file
        objFile = open(file_name, 'r')
        for line in objFile:
            data = line.strip().split(',')
            dicRow = {'ID': int(data[0]), 'Title': data[1], 'Artist': data[2]}
            table.append(dicRow)
        objFile.close()

    @staticmethod
    def write_file(file_name, table):
        """Function to write data to a file 


        Args:
            file_name (string): name of file used to write data into
            table (list of dict): 2D data structure and contains the list of CDs for writing to file

        Returns:
            None.
        """
    
        objFile = open(file_name, 'w')
        for row in lstTbl:
            lstValues = list(row.values())
            lstValues[0] = str(lstValues[0])
            objFile.write(','.join(lstValues) + '\n')
        objFile.close()
        return 

# -- PRESENTATION (Input/Output) -- #

class IO:
    """Handling Input / Output"""

    @staticmethod
    def print_menu():
        """Displays a menu of choices to the user

        Args:
            None.

        Returns:
            None.
        """

        print('Menu\n\n[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
        print('[d] delete CD from Inventory\n[s] Save Inventory to file\n[x] exit\n')
        return 
    @staticmethod
    def menu_choice():
        """Gets user input for menu selection

        Args:
            None.

        Returns:
            choice (string): a lower case sting of the users input out of the choices l, a, i, d, s or x

        """
        choice = ' '
        while choice not in ['l', 'a', 'i', 'd', 's', 'x']:
            choice = input('Which operation would you like to perform? [l, a, i, d, s or x]: ').lower().strip()
        print()  # Add extra space for layout
        return choice

    @staticmethod
    def show_inventory(table):
        """Displays current inventory table

        Args:
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime.

        Returns:
            None.

        """
        print('======= The Current Inventory: =======')
        print('ID\tCD Title (by: Artist)\n')
        for row in table:
            print('{}\t{} (by:{})'.format(*row.values()))
        print('======================================')

    @staticmethod
    def input_data():
        """Request user input for ID, Title and Artist for the CD

        Args:
            None.

        Returns:
            strID = ID of the CD, int converted to string, input by the user
            strTitle = TTitle of the CD, which is a string, input by the user
            strArtist = Artist for the CD, which is a string, inputy by the user
            
        """
        strID = input('Enter ID: ').strip()
        strTitle = input('What is the CD\'s title? ').strip()
        strArtist = input('What is the Artist\'s name? ').strip()
        return strID, strTitle, strArtist

# When program starts, read in the currently saved Inventory
FileProcessor.read_file(strFileName, lstTbl)

# Start main loop
while True:
    # Display Menu to user and get choice
    IO.print_menu()
    strChoice = IO.menu_choice()
    # Process menu selection

    # Process exiting the while loop first
    if strChoice == 'x':
        break

    # Loading the CDInventory
    if strChoice == 'l':
        print('WARNING: If you continue, all unsaved data will be lost and the Inventory re-loaded from file.')
        strYesNo = input('type \'yes\' to continue and reload from file. otherwise reload will be canceled: ')
        if strYesNo.lower() == 'yes':
            print('reloading...')
            FileProcessor.read_file(strFileName, lstTbl)
            IO.show_inventory(lstTbl)
        else:
            input('canceling... Inventory data NOT reloaded. Press [ENTER] to continue to the menu.')
            IO.show_inventory(lstTbl)
        continue  # start loop back at top.

    # Add a CD
    elif strChoice == 'a':
        # Ask user for new ID, CD Title and Artist
        strID, strTitle, strArtist = IO.input_data()
        DataProcessor.cd_add(strID, strTitle, strArtist)
        # Add item to the table
        IO.show_inventory(lstTbl)
        continue  # start loop back at top.

    # Display current inventory
    elif strChoice == 'i':
        IO.show_inventory(lstTbl)
        continue  # start loop back at top.

    # Delete a CD
    elif strChoice == 'd':
        DataProcessor.cd_delete(lstTbl)
        continue  # start loop back at top.

    # Save inventory to file
    elif strChoice == 's':
        # Display current inventory and ask user for confirmation to save
        IO.show_inventory(lstTbl)
        strYesNo = input('Save this inventory to file? [y/n] ').strip().lower()
        # Process the choice made
        if strYesNo == 'y':
        # Save the data
            FileProcessor().write_file(strFileName, lstTbl)
        else:
            input('The inventory was NOT saved to file. Press [ENTER] to return to the menu.')
        continue  # start loop back at top.
    
    # Catch-all should not be possible, as user choice gets vetted in IO, but to be safe:
    else:
        print('General Error')

