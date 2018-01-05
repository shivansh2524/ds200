# ds200
## This repository contains the tasks performed as a part of module 4 of DS200 course.

### Dataset
The Dataset used for this analysis is [Aggregate Technical & Commercial (AT&C) Losses in power sector](https://data.gov.in/catalog/aggregate-technical-commercial-atc-losses-power-sector)

The dataset contains following fields:
```
Index(['Start Month _ Year', 'End Month _ Year', 'State', 'DISCOM',
       'Input Energy (MU)', 'Billed Energy (MU)', 'Billed Amount (Rs crore)',
       'Collected Amount (Rs crore)', 'AT&C Losses (%)'],
      dtype='object')
```

A Snapshot of dataset is shown below:
```
 Start Month _ Year End Month _ Year      State  DISCOM Input Energy (MU)  \
0         April 2014       March 2015      Bihar  NBPDCL            5,849    
1         April 2014       March 2015      Bihar  SBPDCL           10,148    
2         April 2014       March 2015  Jharkhand   JBVNL           11,105    
3         April 2014       March 2015     Odisha    CESU            8,297    
4         April 2014       March 2015     Odisha   NESCO            5,046    

  Billed Energy (MU) Billed Amount (Rs crore) Collected Amount (Rs crore)  \
0             3,823                    1,621                       1,444    
1             5,574                    2,648                       2,638    
2             7,646                    3,042                       2,341    
3             5,494                    2,801                       2,662    
4             3,456                    1,853                       1,668    

   AT&C Losses (%)  
0            41.76  
1            45.28  
2            47.01  
3            37.08  
4            38.36  
```

### Motivation for the analysis of dataset 
The losses that occur in power sector during the dustribution of electrical power are prevalent and are a major cause of total commercial losses to power distribution corporations. The electrical distribution network achieving efficiencies more than 90% nowadays\[[1](https://blog.schneider-electric.com/energy-management-energy-efficiency/2013/03/25/how-big-are-power-line-losses/)]. **The major cause of these accentuated losses is unbilled energy, and analysis of these losses indirectly gives an idea about power theft in a given distribution network.**

### Analysis and Code
The analysis tries to extract the following insights from the given dataset.
  1. How AT&C losses are distributed among individual states?
  2. The distribution of AT&C losses and analysis of median and IQR along with outliers.
  3. Is there any association between the amount of input energy supplied and losses occured in each state?
  
#### 1. How AT&C losses are distributed among individual states?

A bar plot containing states and Average AT&C losses(Averaged over different DISCOMs of the same state).

![Screenshot](https://github.com/shivansh2524/ds200/blob/master/bar_plot_img.png)

**Insights**: Highest losses occur in Nagaland. States having extremme value of losses are Arunachal Pradesh and Nagaland. Not much varaiability is observed among other states.


The python code for generating above plot:
```python
import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv('MOP_ATC_losses.csv')
df2=df[['State','AT&C Losses (%)']]
df3=df2.groupby(['State'],as_index=False)['State','AT&C Losses (%)'].mean()
states=df3['State'].tolist()
losses=df3['AT&C Losses (%)'].tolist()
plt.bar(list(range(len(states))),losses,width=0.8)
plt.xticks(list(range(len(states))),states,rotation='vertical')
plt.title('Average AT&C losses v/s States')
plt.xlabel('States')
plt.ylabel('Average AT&C Losses')
plt.show()
```

#### 2. The distribution of AT&C losses and analysis of median and IQR along with outliers.

A box plot showing the distribution of Average AT&C losses(Averaged over different DISCOMs of the same state).

**Insights**: The Distributed is a little skewed on the higher side which indicates that majority of states have losses higher than median.
Also, the moderately larger IQR (or size) of box plot indicates spreaded out distribution. 

![Screenshot](https://github.com/shivansh2524/ds200/blob/master/box_plot_img.png)

The python code for generating above plot:
```python
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
```
#### 3. Is there any association between the amount of input energy supplied and losses occured in each state?

A scatter plot showing association between Input Energy(MU) and Average AT&C losses(Averaged over different DISCOMs of the same state).

**Insights**: A dense collection of points near origin suggest that small Input energy leads to lower average percentage losses.
![Screenshot](https://github.com/shivansh2524/ds200/blob/master/scatter_plot_img.png)

The python code for generating above plot:
```python
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
```

### References
\[1] https://blog.schneider-electric.com/energy-management-energy-efficiency/2013/03/25/how-big-are-power-line-losses/
