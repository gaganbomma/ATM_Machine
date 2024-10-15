from ATMExcept import depositerror, insufffunderror,withdrawerror

bal=500.00

def deposit():
    damt=float(input("enter ur deposit amount:"))
    if(damt<=0):
        raise depositerror
    else:
        global bal
        bal=bal+damt
        print("ur account xxxxxx123 credited with AUD:{}".format(damt))
        print("now ur account xxxxxx123 AUD:{}".format(bal))



def withdraw():
    global bal
    wamt = float(input("enter ur withdraw amount:"))
    if(wamt<=0):
        raise withdrawerror
    if((wamt+500)>bal):
        raise insufffunderror
    else:
        bal=bal-wamt
        print("ur account xxxxxx123 debited with AUD:{}".format(wamt))
        print("now ur account xxxxxx123 AUD:{}".format(bal))


def balenq():
    print("ur current account balance is AUD:{}".format(bal))