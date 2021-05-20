#!/usr/bin/env python
# coding: utf-8

# # Disclaimer about my data

# - NORTH KOREA and SOUTH KOREA have yet to be untangled, which is why their counts are artificially low
# - "catkey" column is our local record number
# - country codes and regions come from this dataset : https://www.kaggle.com/petersorensen360/iso3166countrieswithregionalcodes
# 

# # Import Packages I need

# In[108]:


import numpy as np
import pandas as pd
import matplotlib as plt


# # Set up the Data

# In[39]:


# create a dataframe from my csv 
# define datatype = string for all columns (won't need to do any math with the numbers)
df_final = pd.read_csv('NASIG_final.csv', dtype='str', header=0)


# In[40]:


# check column names for df_final dataframe
for col in df_final.columns:
    print(col)


# In[77]:


# look at the first 20 rows of the dataframe
# confirm that the NULL values came over as null (they did)
df_final.head(20)


# In[ ]:





# # START ANSWERING QUESTIONS!

# ## Which countries occur most / least frequently?

# In[42]:


# count the total number of times each country occurs
# use 'df_final['country'].value_counts()[:50]' if you want to see only the top 50 , etc.
df_final['country'].value_counts()


# ## Which countries are best / worst represented when measuring by titles?

# In[86]:


# create a new dataframe with the count of unique catkeys for each country 
# (in other words, how many bibs total contain a subject from each country)
df_uni_countries = df_final.groupby('country')['catkey'].nunique()
print(df_uni_countries)


# In[96]:


# order by catkey column (which should actually be called "count_unique_catkey")
df_uni_countries = df_final.groupby('country')['catkey'].nunique().reset_index().sort_values("catkey", ascending=False)
print(df_uni_countries)


# In[85]:


# create my final dataframe which has the count in order and the column name changed to "count_unique_catkey"
df_uni_countries = df_final.groupby('country')['catkey'].nunique().reset_index().sort_values("catkey", ascending=False)
df_unicon_final = df_uni_countries.rename(columns={"country": "country", "catkey": "count_unique_catkey"})
print(df_unicon_final)


# ## Which regions occur most / least frequently?

# In[88]:


# count the total number of times each region occurs
# reminder - column names are "region" , "sub-region" , "intermediate-region"
df_final['region'].value_counts()


# In[89]:


df_final['sub-region'].value_counts()


# In[90]:


df_final['intermediate-region'].value_counts()


# ## Which regions are best / worst represented when measuring by titles? 

# In[95]:


# create a new dataframe with the count of unique catkeys for each region 
# (in other words, how many bibs total contain a subject from each region)
# order by catkey column (which should actually be called "count_unique_catkey")
df_uni_regions = df_final.groupby('region')['catkey'].nunique().reset_index().sort_values("catkey", ascending=False)
print(df_uni_regions)


# In[98]:


# create my final dataframe which has the count in order and the column name changed to "count_unique_catkey"
df_uni_regions = df_final.groupby('region')['catkey'].nunique().reset_index().sort_values("catkey", ascending=False)
df_unireg_final = df_uni_regions.rename(columns={"region": "region", "catkey": "count_unique_catkey"})
print(df_unireg_final)


# In[102]:


# create a new dataframe with the count of unique catkeys for each sub-region 
# (in other words, how many bibs total contain a subject from each sub-region )
# order by catkey column (which should actually be called "count_unique_catkey")
df_uni_subregions = df_final.groupby('sub-region')['catkey'].nunique().reset_index().sort_values("catkey", ascending=False)
print(df_uni_subregions)


# In[104]:


# create my final dataframe which has the count in order and the column name changed to "count_unique_catkey"
df_uni_subregions = df_final.groupby('sub-region')['catkey'].nunique().reset_index().sort_values("catkey", ascending=False)
df_unisubreg_final = df_uni_subregions.rename(columns={"sub-region": "sub-region", "catkey": "count_unique_catkey"})
print(df_unisubreg_final)


# In[105]:


# create a new dataframe with the count of unique catkeys for each sub-region 
# (in other words, how many bibs total contain a subject from each sub-region )
# order by catkey column (which should actually be called "count_unique_catkey")
df_uni_intregions = df_final.groupby('intermediate-region')['catkey'].nunique().reset_index().sort_values("catkey", ascending=False)
print(df_uni_intregions)


# In[106]:


# create my final dataframe which has the count in order and the column name changed to "count_unique_catkey"
df_uni_intregions = df_final.groupby('intermediate-region')['catkey'].nunique().reset_index().sort_values("catkey", ascending=False)
df_uniintreg_final = df_uni_intregions.rename(columns={"intermediate-region": "intermediate-region", "catkey": "count_unique_catkey"})
print(df_uniintreg_final)


# ## Which countries had the most / least distinct 650$a 's?

# In[172]:


# create a new dataframe that contains the count of the unique subject heading for each country

grouped_651_df = df_final.groupby("country")
grouped_651_df_agg = grouped_651_df.agg({"geoname": "nunique"}).sort_values("geoname", ascending=False)
grouped_651_df_reorder = grouped_651_df_agg.reset_index().rename(columns={"country": "country", "geoname": "count_unique_651"})
print(grouped_651_df_reorder)


# In[175]:


print(grouped_651_df_reorder.to_string())


# # Visually communicate findings 

# ### Reminder of the df names:
# df_final - entire dataset
# df_unicon_final - count of unique catkeys for each country 
# df_unireg_final - count of unique catkeys for each region  
# df_unisubreg_final - count of unique catkeys for each sub-region  
# df_uniintreg_final - count of unique catkeys for each intermediate-region  
# 
# ### Didn't declare a df yet, but could
# df_final['country'].value_counts() - count the total number of times each country occurs
# df_final['region'].value_counts() - count the total number of times each region occurs
# df_final['sub-region'].value_counts() - count the total number of times each sub-region occurs
# df_final['intermediate-region'].value_counts() - count the total number of times each intermediate-region occurs

# In[131]:


ax = df_unicon_final.head(10).plot.bar(x='country')
ax.set_xlabel("country")
ax.set_ylabel('count')
ax.set_title('Count of unique catkeys for top 10 countries')


# In[132]:


ax = df_unicon_final.tail(10).plot.bar(x='country')
ax.set_xlabel("country")
ax.set_ylabel('count')
ax.set_title('Count of unique catkeys for lowest 10 countries')


# In[116]:


ax = df_unireg_final.plot.bar(x='region')
ax.set_xlabel("region")
ax.set_ylabel('count')
ax.set_title('Count of unique catkeys for each region')


# In[117]:


ax = df_unisubreg_final.plot.bar(x='sub-region')
ax.set_xlabel("sub-region")
ax.set_ylabel('count')
ax.set_title('Count of unique catkeys for each sub-region')


# In[118]:


ax = df_uniintreg_final.plot.bar(x='intermediate-region')
ax.set_xlabel("intermediate-region")
ax.set_ylabel('count')
ax.set_title('Count of unique catkeys for each intermediate-region')


# In[129]:


df_totalcountries = df_final['country'].value_counts().head(15)
ax = df_totalcountries.plot.bar(x='country')
ax.set_xlabel("country")
ax.set_ylabel('count')
ax.set_title('Count of total occurences for each country')


# In[130]:


df_totalcountries = df_final['country'].value_counts().tail(15)
ax = df_totalcountries.plot.bar(x='country')
ax.set_xlabel("country")
ax.set_ylabel('count')
ax.set_title('Count of total catkeys for each country')


# In[133]:


df_totalregion = df_final['region'].value_counts()
ax = df_totalregion.plot.bar(x='region')
ax.set_xlabel("region")
ax.set_ylabel('count')
ax.set_title('Count of total catkeys for each region')


# In[139]:


df_final['country'].value_counts()[:50].plot(kind='barh', figsize = (10,10))

