import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stt
def fetch(Symbol:str,Market:str='USD'):
    # Cryptocurrency API address
    URL_API='https://www.alphavantage.co/query?function=DIGITAL_CURRENCY_DAILY&symbol={}&market={}&apikey=https://www.alphavantage.co/query?function=DIGITAL_CURRENCY_DAILY&symbol=ETH&market=USD&apikey=KY1LVVD6LP4NY26K&datatype=csv&datatype=csv'.format(Symbol,Market)
    Columns=['timestamp','open (USD)','high (USD)','low (USD)','close (USD)','volume']
    DF=pd.read_csv(URL_API,sep=',',usecols=Columns,header=0)
    #Reversing history
    C=(DF['close (USD)'].to_numpy())[::-1].copy()

    #Graphical chart
    # plt.subplot(1,2,1)
    # plt.plot(C,label='ETH Closes (Last 1000 Day)')
    # plt.xlabel('Time (Day)')
    # plt.ylabel('Price ($)')
    # plt.legend()
    # #Logarithmic graph along the Y axis
    # plt.subplot(1,2,2)
    # plt.semilogy(C,label='ETH Closes (Last 1000 Day)')
    # plt.xlabel('Time (Day)')
    # plt.ylabel('Price ($)')
    # plt.legend()
    # plt.show()

    #Taking logarithms
    L=np.log(C)
    return C, L
C_eth,L_eth=fetch('ETH')
C_btc,L_btc=fetch('BTC')
#Chart for both
# plt.subplot(1,2,1)
# plt.plot(L_eth,label='ETH closes')
# plt.xlabel('Time (Day)')
# plt.ylabel('Price ($)')
# plt.legend()

# plt.subplot(1,2,2)
# plt.plot(L_btc,label='BTC closes')
# plt.xlabel('Time (Day)')
# plt.ylabel('Price ($)')
# plt.legend()
# plt.show()

#scatter ploat
# plt.scatter(C_btc,C_eth,s=4)
# plt.xlabel('BTC Price')
# plt.ylabel('ETH Price')
# plt.legend()

#Computing
Cs=np.polyfit(L_btc,L_eth,1)
P=np.poly1d(Cs)
#[ 1.00000000e+00 -1.16506362e-16]
Relation='log(ETH)= {}*log(BTC) + {}'.format(str(round(Cs[0],2)),str(round(Cs[1],2)))
#logarithms
plt.scatter(L_btc,L_eth,s=4)
plt.plot([6,9],[P(6),P(9)],label='Linear Regression',linewidth=1.3,c='k')
plt.title(Relation)
plt.xlabel('log(BTC Price)')
plt.ylabel('log(ETH Price)')
plt.legend()
plt.show()

#Calculate the correlation value with Pearson
PCC,_=stt.pearsonr(L_btc,L_eth)
#PCC = 1.0
#PCC -1 <= PCC <= +1