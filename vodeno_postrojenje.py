import numpy 
from scipy.integrate import odeint
import matplotlib.pyplot as plt 
from colorama import Fore 
from colorama import Style
pi=3.14159



print('')
print('')
print('')
print('')


radijus=float(input('   RADIJUS BAZENA r= '))
print('r=',radijus)
dubina=float(input(     'DUBINA BAZENA h= '))
površina_bazena=radijus**2*pi 
voluemen_bazena=površina_bazena*dubina



print(' POVRŠINA BAZENA IZNOSI    ',Style.BRIGHT,round(površina_bazena,2),Style.RESET_ALL,' m2')
print(Style.RESET_ALL+'')
print(' VOLUMEN BAZENA IZNOSI     ',Style.BRIGHT,round(voluemen_bazena,2),Style.RESET_ALL,' m3')
print('')
print('')
print('')


#   BILANCA PROTOKA BENZENA

# P= VOLUMNI PROTOK [=] m3/h 
# C= KONCENTRACIJA BENZENA g/m3
# BZ1= MASA BENZENA KOJA ULAZI U 1. BAZEN 
p=100
t0=0

t_min=numpy.linspace(0,60,10000)
bz=numpy.piecewise(t_min,[ t_min<=30.0000,t_min>30.0000],[5.0,0.0])
plt.plot(t_min,bz*100)
plt.title('MASENI PROTOK BENZENA U 1. BAZEN KROZ VRIJEME')
plt.xlabel(' VRIJEME t/min ')
plt.ylabel(' BENZEN PROTOK g/h ')
plt.show()

#c0=numpy.piecewise(t,[t<=30.00,t>30.00],[5.00,0.00])


t=numpy.linspace(0.000,1.000,10000)            # VREMENSKI RASPON I TOČKE

def dc(c,t):                                    # RJEŠAVANJE DVIJE DIFERENCIJALNE JEDNADŽBE PARALELNO, KAŽE: IZRAČUNAJ VRIJEDNOSTI [c] ZA VREMENA [t]
    ca=c[0]                                     # KAŽE: ca SE RAČUNA PRVO 
    cb=c[1]                                     # KAŽE: cb SE RAČUNA DRUGI
    diff_1=((100*numpy.piecewise(t,[t<=0.50000,t>0.50000],[5.0000,0.0000]))-(394.450*ca))/9.8200        # 1. DIFERENCIJALNA JEDNADŽBA
    diff_2=(100*ca-394.45*cb)/9.82                                                                      # 2. DIFERENCIJALNA JEDNADŽBA
    return(diff_1,diff_2)                       # KAŽE: PROVEDI POSTUPAK ZA DIFF_1 I DIFF_2


c=odeint(dc,[0,0],t)                           # RIJEŠI FUNKCIJU dc S POČETNIM UVJETIMA [0,0] I ZA VREMENA t

print('numerička rješenja funkcije BAZEN A: ',c[:,0])
print('numerička rješenja funkcije za definirane unose vremena- BAZEN B: ',c[:,1])

plt.plot(t,c[:,:])
plt.title('KONCENTRACIJE BENZENA U BAZENU [A-PLAVO] I [B-CRVENO] ZA VRIJEME')
plt.xlabel(' VRIJEME U SATIMA ')
plt.ylabel(' KONCENTRACIJA BENZENA U BAZENU ')
plt.legend(['PLAVO- BAZEN A','NARANČASTO- BAZEN B'])
plt.show()


print('::::::::::::::::::::::::::::::::::')
print('::::::::::::::::::::::::::::::::::')
print('')
print('')
print('')
print('')
print('  MAKSIMALNI UDIO BENZENA U BAZENU A = ',round(numpy.max(c[:,0]),3),'g/m3')
print('  MAKSIMALNI UDIO BENZENA U BAZENU B = ',round(numpy.max(c[:,1]),3),'g/m3')

if round(numpy.max(c[:,1]))<1.00:
    print('')
    print('')
    print('')
    print(Fore.RED,Style.BRIGHT+'  BENZEN:          OK      ',Fore.RESET,Style.RESET_ALL)
    print('')
    print('')
    print('')
else:
    print('')
    print('')
    print('')
    print(Fore.RED,Style.BRIGHT+'  BENZEN:       TOO HIGH   ',Fore.RESET,Style.RESET_ALL)
    print('')
    print('')
    print('')




# PITANJE C
# TRANSFER FUNCTIONS

g1=(c[:,0])/bz

plt.plot(t,g1)
plt.xlabel('t')
plt.ylabel('g(t)')
plt.title('OMJER KONCENTRACIJE BENZENA U SPREMNIKU {A} I ULAZNE KONCENTRACIJE KROZ VRIJEME')
plt.legend(['g(t)'])
plt.show()


g2=(c[:,1])/(c[:,0])

plt.plot(t,g2)
plt.xlabel('t')
plt.ylabel('g2(t)')
plt.title('OMJER KONCENTRACIJE BENZENA U SPREMNIKU {B} I ULAZNE KONCENTRACIJE KROZ VRIJEME')
plt.legend(['g2(t)'])
plt.show()






