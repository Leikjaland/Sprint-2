# Útgáfa 1.0

import sys
import time
import select
#from herbergi_2 import skolastofa

# Hlutir sem þarf að satna í skólasofu og útiveru
#bok = {}
#blom = {}


class leikjaland(object):

    #def __init__(self,bok,blom):
    #    self.bok=bok
    #    self.blom=blom


# Hér ver verið að taka á móti leikmanni og spyrja um kyn.
    print('Velkomin\\nn í leikjaland')
    kyn = input('Veldu kyn, strakur eða stelpa: ')
    print('Þú ert ' + kyn  )

# Hér byrjar herbergi_1
    def Herbergi_1(self):
        #print('test1')
        while (1):
            try:
                fot= input('Viltu fara í skólann eða út að leika, velja\\skrifa skolafot eða utifot: ')
                fot=fot
                break
# Þarf að skoða betur!
            except:
                print ('Þú hefur ekki valið föt')


# leikmaður fer í skolastofuna
        if fot == 'skolafot':
            print('Þú ert komin\\nn í skólann')
            #skolastofa()
            # forritið sem verður fyrir skólastofu herbergið


# Leikmaður fer í útiveru
        elif fot == 'utifot':
            print('Þú ert komin\\nn út')
        # utivera(blom)
        # forritið sem verður fyrir utiveru herbergið

# ef ekki ekki er valið skólaföt eða útiföt
        else:
            print ('Þú hefur ekki valið föt')
            self.Herbergi_1()

# Fallið leyfir leikmanni að koma til baka og skipta um föt til að fara í hitt herbergið
    def skipta_um_fot(self):
        if fot == 'skolafot':
            print('Þú ert að fara í útiföt')
            # utivera()

        elif fot == 'utifot':
            print('Þú ert að fara í skólaföt')
            # skolastofa()



def  main():
    leikur=leikjaland()
    leikur.Herbergi_1()



if __name__  == '__main__':
    main()
