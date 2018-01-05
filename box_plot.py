import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv('MOP_ATC_losses.csv')
df2=df[['State','AT&C Losses (%)']]
df3=df2.groupby(['State'],as_index=False)['State','AT&C Losses (%)'].mean()
states=df3['State'].tolist()
losses=df3['AT&C Losses (%)'].tolist()
plt.boxplot(losses)
plt.title('Average AT&C Losses')
plt.show()
