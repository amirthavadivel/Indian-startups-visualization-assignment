#!/usr/bin/env python
# coding: utf-8

# In[31]:


#importing library
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px


# In[7]:


#importing dataset
companies=pd.read_csv('C:/Users/amirt/OneDrive/Documents/OneDrive/Documents/2021_registered_companies.csv')


# In[32]:


#visualizing registered companies
ax=plt.figure(figsize=(10,8)).add_axes([0,0,1,1])
sns.set_style('white')
sns.countplot(x='month_name',data=companies)

for rect in ax.patches:
    ax.text (rect.get_x() + rect.get_width() / 2,rect.get_height(),"%i"% rect.get_height()
             ,fontsize=14 )

plt.title('Registered Companies',fontsize=14, weight='bold')
plt.xlabel('Month',fontsize=14)
plt.ylabel('Number of Companies Registered',fontsize=14)
plt.show()


# In[10]:


#date of registration
companies_date=pd.DataFrame(companies['date_of_registration'].groupby
                              (companies['date_of_registration'].iloc[:]).count())
companies_date.rename(columns={"date_of_registration":"count"},inplace=True)
companies_date.sort_values('date_of_registration')
companies_date.reset_index(inplace=True)


# In[12]:


#month date
month_date=pd.DataFrame(companies['date_of_registration'].value_counts())
month_date.reset_index(inplace=True)
month_date['month']='month'
month_date.sort_values('index',inplace=True)

def assign_month(df):
    for i in range(0,len(df.index)):
        if '/01' in df.loc[i,'index']:
            df.loc[i,'month']='Jan-21'
        elif '/02' in df.loc[i,'index']:
            df.loc[i,'month']='Feb-21'
        elif '/03' in df.loc[i,'index']:
            df.loc[i,'month']='Mar-21'
        elif '/04' in df.loc[i,'index']:
            df.loc[i,'month']='Apr-21'
            
assign_month(month_date)


# In[33]:


#Registered companies in a day
ax=plt.figure(figsize=(10,8)).add_axes([0,0,1,1])
sns.set_style('white')
sns.boxplot(x='month',y='date_of_registration',data=month_date)
plt.title('Registered Companies in a day',fontsize=14, weight='bold')
plt.xlabel('Month',fontsize=14)
plt.ylabel('Number of Companies Registered in a day',fontsize=14)
plt.show()


# In[34]:


#company sectors
ax=plt.figure(figsize=(11,8)).add_axes([0,0,1,1])
sns.set_style('white')
sns.countplot(y='activity_description',data=companies)
for rect in ax.patches:
    ax.text (rect.get_width(), rect.get_y() + rect.get_height() / 2,
             "%i"% rect.get_width(),fontsize=13 )

plt.title('Sectors of Companies',fontsize=14, weight='bold')
plt.xlabel('Number of Companies Registered',fontsize=14)
plt.ylabel('Sectors',fontsize=14)
plt.show()


# In[15]:


#sectors %
companies_sector=pd.DataFrame(companies['activity_description'].groupby
                              (companies['activity_description'].iloc[:]).count())
companies_sector.rename(columns={"activity_description":"count"},inplace=True)
companies_sector.sort_values('count',ascending=False,inplace=True)
companies_sector.loc['Others'] = [ companies_sector.iloc[5:,0].sum()] 
companies_sector.sort_values('count',ascending=False,inplace=True)
companies_sector=companies_sector.iloc[:6,0]


# In[16]:


plt.figure(dpi=1000)

pie, ax = plt.subplots(figsize=[10,7])
labels = companies_sector.keys()
plt.pie(x=companies_sector, autopct="%.1f%%",labels=labels, pctdistance=0.5)
plt.title("Registered Companies by Sector", weight='bold',fontsize=14);
plt.show()


# In[18]:


#sectors table
companies_activity=companies.pivot_table(index='activity_description',values=['paidup_capital','authorized_capital'])
companies_activity.reset_index(inplace=True)


# In[35]:


#comparision between sectors
plt.figure(figsize=(17,8))
df = companies_activity.melt('activity_description', var_name='capital',  value_name='vals')
sns.pointplot(x="activity_description", y="vals", hue='capital', data=df)
plt.xticks(rotation = 90)
plt.title('Comparision between sectors',fontsize=14, weight='bold')
plt.xlabel('Sectors',fontsize=14)
plt.ylabel('Capital',fontsize=14)
plt.show()


# In[21]:


#states
companies_state=pd.DataFrame(companies['state'].groupby
                              (companies['state'].iloc[:]).count())
companies_state.rename(columns={"state":"count"},inplace=True)
companies_state.sort_values('count',ascending=False,inplace=True)
companies_state.reset_index(inplace=True)


# In[37]:


#Registered compaines in state
plt.figure(figsize=(17,7))
sns.set_style('whitegrid')
sns.barplot(x='state',y='count',data=companies_state[21:])

plt.xticks(rotation = 90)
plt.title('Registered Companies in States',fontsize=10, weight='bold')
plt.xlabel('States',fontsize=14)
plt.ylabel('Number of Companies Registered',fontsize=14)
plt.show()


# In[38]:


#top 5 states
companies5=companies[(companies['state'] == 'Maharashtra') |
                     (companies['state'] == 'Uttar Pradesh') |
                     (companies['state'] == 'Delhi') |
                     (companies['state'] == 'Karnataka') |
                     (companies['state'] == 'Telangana')
                    ]


# In[39]:


companies5_sector=pd.DataFrame(companies5['activity_description'].groupby
                              (companies5['activity_description'].iloc[:]).count())
companies5_sector.rename(columns={"activity_description":"count"},inplace=True)
companies5_sector.sort_values('count',ascending=False,inplace=True)
companies5_sector.loc['Others'] = [ companies5_sector.iloc[5:,0].sum()] 
companies5_sector.sort_values('count',ascending=False,inplace=True)
companies5_sector=companies5_sector.iloc[:6,0]


# In[40]:


plt.figure(dpi=1000)

pie, ax = plt.subplots(figsize=[10,7])
labels = companies5_sector.keys()
plt.pie(x=companies5_sector, autopct="%.1f%%",labels=labels, pctdistance=0.5)
plt.title("Registered Companies by Sector in top 5 states", weight='bold',fontsize=14);
plt.show()


# In[28]:


ax=plt.figure(figsize=(10,8)).add_axes([0,0,1,1])
sns.set_style('white')
sns.countplot(x='category',data=companies)

for rect in ax.patches:
    ax.text (rect.get_x() + rect.get_width() / 2,rect.get_height(),"%i"% rect.get_height()
             ,fontsize=14 )

plt.title('Category of Registered Companies',fontsize=14, weight='bold')
plt.xlabel('Categories',fontsize=14)
plt.ylabel('Number of Companies Registered',fontsize=14)
plt.show()


# In[29]:


plt.figure(figsize = (5,5))
sns.scatterplot(x='company_type',y='category',data=companies)
plt.xticks(rotation = 90)
plt.show()


# In[ ]:




