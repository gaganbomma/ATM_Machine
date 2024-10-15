from ATMMenu import menu

import sys

from ATMExcept import depositerror, withdrawerror, insufffunderror
from ATMOperations import deposit, withdraw,balenq

while(True):
    try:
        menu()
        ch=int(input("Enter ur choice:"))
        match(ch):
         case 1:
             try:
                 deposit()
             except depositerror:
                 print("Don't Deposit -VE and Zero Amount in the accounts-try again ")
             except ValueError:
                 print("Don't try to enter alnums,strs and symbols for Depositing Amount ")


         case 2:
             try:
               withdraw()
             except withdrawerror:
                 print("Don't Withdraw -VE and Zero Amount in the accounts-try again ")
             except ValueError:
                 print("Don't try to enter alnums,strs and symbols for withdrawing Amount ")
             except insufffunderror:
                 print("Ur Account does not have suff funds-So I should crack the interview")
         case 3:
             balenq()

         case 4:
             print("Thx for using pgm")
             sys.exit()

         case _:
            print("Ur selection of operation is wrong-try again")

    except ValueError:
        print("Don't enter alnums,strs and special symbols for Choice--try again")
