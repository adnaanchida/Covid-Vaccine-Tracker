Python 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#######################################################
# Name:   Adnaan Chida
# Latest Update: October 9
#######################################################


print('\n**  Adnaan Chida  **\n') # Display author's name

... # selecting menu for first screen
... def menu1():
...     print('\nCovid Vaccine Tracker', '\n1 - Enter records', '\n2 - Update records', '\n3 - Run reports')
...     print('Please select an option (press Enter to exit)')
... 
... 
... # selecting menu for Run reports screen
... def menu2():
...     print('\n1 - Display test results by Zip code', '\n2 - Display total results')
...     print('Please select an option (press Enter to exit)')
... 
... 
... # main function
... def main():
...     # theNames = []
...     # theZips = []
...     # theResults = []
...     theNames = ['Aname', 'Cname', 'Hname', 'Bname', 'Gname', 'Fname', 'Dname', 'Ename', 'Iname']
...     theZips = ['60137', '60138', '60555', '60138', '60137', '60555', '60555', '60138', '60137']
...     # A-C positive, D-F negative, G-I no result
...     theResults = ['P', 'P', 'P', 'P', 'M', 'M', 'J', '', '', 'P']
... 
...     # taking boolean value for first screen
...     condition4 = True
...     while condition4:
...         # showing menu after every operation
...         menu1()
...         choice1 = input()
... 
...         # after choosing one first screen
...         if choice1 == '1':
... 
...             # Taking two boolean values one is asking again and again zip-code
...             # and other is for asking result
... 
...             condition2 = True
            condition3 = True
            print('\nEnter a name (press Enter to exit): ', end='')
            name = input().strip()
            if name == '':
                # exist out when user enter without adding anything
                condition2 = False
                condition3 = False
            else:
                theNames.append(name)
            while condition2:
                print('Enter a zip code: ', end='')
                zip_code = input().strip()
                if len(zip_code) == 5:
                    condition2 = False
                    theZips.append(zip_code)
                else:
                    print('Invalid zip code, try again.')
            while condition3:
                print('Enter a vaccine (P for Pfiser, M for Moderna, J for Johnson & Johnson or leave empty):')
                result = input().strip()
                if result == '' or result == 'P' or result == 'M' or result == 'J':
                    theResults.append(result)
                    condition3 = False
                else:
                    print('invalid key, try again.')
        elif choice1 == '2':

                # Taking two boolean values one is asking again and again if name is not found in above list
                # and other is for asking result

            condition1 = True
            condition2 = False
            while condition1:
                print('\nEnter a name to search (press Enter to exit): ', end='')
                name = input().strip()
                if name == '':
                    condition1 = False
                elif name in theNames:
                    condition2 = True
                    print(name, '\nZip code:', theZips[theNames.index(name)], '\nCurrent vaccine:',
                          str(None) if theResults[theNames.index(name)] == '' else theResults[
                              theNames.index(name)], sep='')
                else:
                    print('Name not found.')
                while condition2:
                    print('\nEnter a new vaccine (P for Pfiser, M for Moderna, J for Johnson & Johnson or leave empty): ',
                          end='')
                    result = input()
                    if result == '' or result == 'P' or result == 'M' or result == 'J':
                        theResults[theNames.index(name)] = result
                        condition2 = False
                    else:
                        print('invalid key, try again.')

        elif choice1 == '3':
            # opening second selecting screen for run reports
            menu2()
            choice = input()
            if choice == '1':
                '''
                Using dictionary making all values in the format of
                {
                    'zip-code' : [the values of result for particular zip-code],
                    'zip-code' : [the values of result for particular zip-code],
                     ------ so on..
                }
                '''
                uniqueZips = dict()
                for i in range(len(theZips)):
                    if theZips[i] in uniqueZips.keys():
                        uniqueZips[theZips[i]] += [theResults[i]]
                    else:
                        uniqueZips[theZips[i]] = list(theResults[i])
                # printing them in order
                print('Test results by zip code.')
                print('%-10s' % 'zip_code', '%-10s' % 'Pfiser', '%-10s' % 'Moderna', '%-10s' % 'Johnson & Johnson', '%-50s' % '\tNone' )
                for i in uniqueZips.keys():
                    print('%-10s' % i, '%-10s' % uniqueZips[i].count('P'), '%-10s' % uniqueZips[i].count('M'), '%-10s' % uniqueZips[i].count('J'), '\t\t' '%-50s' % uniqueZips[i].count(''))
            elif choice == '2':
                # printing all values counts in order
                print('Total results by order.')
                print('%-10s' % 'Pfiser', '%-10s' % 'Moderna', '%-10s' % 'Johnson & Johnson', '%-10s' % '\tNone')
                print('%-10s' % theResults.count('P'), '%-10s' % theResults.count('M'), '%-10s' % theResults.count('J'), '\t\t'  '%-10s' % theResults.count(''))

            else:
                print('Invalid option.')
        elif choice1 == '':
            condition4 = False
        else:
            print('Invalid option, please try again.')


# def bubbleSort3(names, zips, results):
#     for i in range(0, len(zips) - 1):
#         for j in range(0, len(zips) - 1 - i):
#             if zips[j] > zips[j + 1]:
#                 zips[j], zips[j + 1] = zips[j + 1], zips[j]
#                 names[j], names[j + 1] = names[j + 1], names[j]
#                 results[j], results[j + 1] = results[j + 1], results[j]



main()


'''
OUTPUT:
**  Adnaan Chida  **
Covid Vaccine Tracker
1 - Enter records
2 - Update records
3 - Run reports
Please select an option (press Enter to exit)
1
Enter a name (press Enter to exit): Adnaan C.
Enter a zip code: 60108
Enter a vaccine (P for Pfiser, M for Moderna, J for Johnson & Johnson or leave empty):
M
Covid Vaccine Tracker
1 - Enter records
2 - Update records
3 - Run reports
Please select an option (press Enter to exit)
2

Enter a name to search (press Enter to exit): Adnaan C.
Adnaan C.
Zip code:60108
Current vaccine:P

Enter a new vaccine (P for Pfiser, M for Moderna, J for Johnson & Johnson or leave empty): 3
invalid key, try again.

Enter a new vaccine (P for Pfiser, M for Moderna, J for Johnson & Johnson or leave empty): P

Enter a name to search (press Enter to exit): Adnaan C.
Adnaan C.
Zip code:60108
Current vaccine:P

Enter a new vaccine (P for Pfiser, M for Moderna, J for Johnson & Johnson or leave empty):

Enter a name to search (press Enter to exit):

Covid Vaccine Tracker
1 - Enter records
2 - Update records
3 - Run reports
Please select an option (press Enter to exit)
3

1 - Display test results by Zip code
2 - Display total results
Please select an option (press Enter to exit)
1
Test results by zip code.
zip_code   Pfiser     Moderna    Johnson & Johnson      None
60137      1          1          0                      1
60138      2          0          0                      1
60555      1          1          1                      0
60108      0          0          0                      0

Covid Vaccine Tracker
1 - Enter records
2 - Update records
3 - Run reports
Please select an option (press Enter to exit)
3 - Run reports
Invalid option, please try again.

Covid Vaccine Tracker
1 - Enter records
2 - Update records
3 - Run reports
Please select an option (press Enter to exit)
Please select an option (press Enter to exit)

'''




