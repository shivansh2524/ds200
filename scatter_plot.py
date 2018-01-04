import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv('MOP_ATC_losses.csv')
df2a=df[['State','Input Energy (MU)']]
siz=df2a.shape[0]
for i in range(0,siz):
    temp=df2a.get_value(i,'Input Energy (MU)')
    temp2=[x for x in temp if x!=',']
    df2a.set_value(i,'Input Energy (MU)',int(''.join(temp2)))

df2a[['Input Energy (MU)']]=df2a[['Input Energy (MU)']].apply(pd.to_numeric)
df4=df2a.groupby(['State'],as_index=False)['State','Input Energy (MU)'].mean()  

df2=df[['State','AT&C Losses (%)']]
df3=df2.groupby(['State'],as_index=False)['State','AT&C Losses (%)'].mean()

inputener=df4['Input Energy (MU)'].tolist()
losses=df3['AT&C Losses (%)'].tolist()

plt.scatter(inputener,losses)
plt.title('Effect of Statewise Input Energy Amount on Losses')
plt.xlabel('Input Energy (MU)')
plt.ylabel('Average AT&C Losses')
plt.show()