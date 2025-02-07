#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Challenge-1" data-toc-modified-id="Challenge-1-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Challenge 1</a></span><ul class="toc-item"><li><ul class="toc-item"><li><ul class="toc-item"><li><span><a href="#Import-all-required-libraries." data-toc-modified-id="Import-all-required-libraries.-1.0.0.1"><span class="toc-item-num">1.0.0.1&nbsp;&nbsp;</span>Import all required libraries.</a></span></li><li><span><a href="#Import-data-set." data-toc-modified-id="Import-data-set.-1.0.0.2"><span class="toc-item-num">1.0.0.2&nbsp;&nbsp;</span>Import data set.</a></span></li><li><span><a href="#Print-first-10-rows-of-pokemon." data-toc-modified-id="Print-first-10-rows-of-pokemon.-1.0.0.3"><span class="toc-item-num">1.0.0.3&nbsp;&nbsp;</span>Print first 10 rows of <code>pokemon</code>.</a></span></li><li><span><a href="#Obtain-the-distinct-values-across-Type-1-and-Type-2." data-toc-modified-id="Obtain-the-distinct-values-across-Type-1-and-Type-2.-1.0.0.4"><span class="toc-item-num">1.0.0.4&nbsp;&nbsp;</span>Obtain the distinct values across <code>Type 1</code> and <code>Type 2</code>.</a></span></li><li><span><a href="#Cleanup-Name-that-contain-&quot;Mega&quot;." data-toc-modified-id="Cleanup-Name-that-contain-&quot;Mega&quot;.-1.0.0.5"><span class="toc-item-num">1.0.0.5&nbsp;&nbsp;</span>Cleanup <code>Name</code> that contain "Mega".</a></span></li><li><span><a href="#Create-a-new-column-called-A/D-Ratio-whose-value-equals-to-Attack-devided-by-Defense." data-toc-modified-id="Create-a-new-column-called-A/D-Ratio-whose-value-equals-to-Attack-devided-by-Defense.-1.0.0.6"><span class="toc-item-num">1.0.0.6&nbsp;&nbsp;</span>Create a new column called <code>A/D Ratio</code> whose value equals to <code>Attack</code> devided by <code>Defense</code>.</a></span></li><li><span><a href="#Identify-the-pokemon-with-the-highest-A/D-Ratio." data-toc-modified-id="Identify-the-pokemon-with-the-highest-A/D-Ratio.-1.0.0.7"><span class="toc-item-num">1.0.0.7&nbsp;&nbsp;</span>Identify the pokemon with the highest <code>A/D Ratio</code>.</a></span></li><li><span><a href="#Identify-the-pokemon-with-the-lowest-A/D-Ratio." data-toc-modified-id="Identify-the-pokemon-with-the-lowest-A/D-Ratio.-1.0.0.8"><span class="toc-item-num">1.0.0.8&nbsp;&nbsp;</span>Identify the pokemon with the lowest A/D Ratio.</a></span></li><li><span><a href="#Create-a-new-column-called-Combo-Type-whose-value-combines-Type-1-and-Type-2." data-toc-modified-id="Create-a-new-column-called-Combo-Type-whose-value-combines-Type-1-and-Type-2.-1.0.0.9"><span class="toc-item-num">1.0.0.9&nbsp;&nbsp;</span>Create a new column called <code>Combo Type</code> whose value combines <code>Type 1</code> and <code>Type 2</code>.</a></span></li><li><span><a href="#Identify-the-pokemon-whose-A/D-Ratio-are-among-the-top-5." data-toc-modified-id="Identify-the-pokemon-whose-A/D-Ratio-are-among-the-top-5.-1.0.0.10"><span class="toc-item-num">1.0.0.10&nbsp;&nbsp;</span>Identify the pokemon whose <code>A/D Ratio</code> are among the top 5.</a></span></li><li><span><a href="#For-the-5-pokemon-printed-above,-aggregate-Combo-Type-and-use-a-list-to-store-the-unique-values." data-toc-modified-id="For-the-5-pokemon-printed-above,-aggregate-Combo-Type-and-use-a-list-to-store-the-unique-values.-1.0.0.11"><span class="toc-item-num">1.0.0.11&nbsp;&nbsp;</span>For the 5 pokemon printed above, aggregate <code>Combo Type</code> and use a list to store the unique values.</a></span></li><li><span><a href="#For-each-of-the-Combo-Type-values-obtained-from-the-previous-question,-calculate-the-mean-scores-of-all-numeric-fields-across-all-pokemon." data-toc-modified-id="For-each-of-the-Combo-Type-values-obtained-from-the-previous-question,-calculate-the-mean-scores-of-all-numeric-fields-across-all-pokemon.-1.0.0.12"><span class="toc-item-num">1.0.0.12&nbsp;&nbsp;</span>For each of the <code>Combo Type</code> values obtained from the previous question, calculate the mean scores of all numeric fields across all pokemon.</a></span></li></ul></li></ul></li></ul></li></ul></div>

# # Challenge 1
# 
# In this challenge you will be working on **Pokemon**. You will answer a series of questions in order to practice dataframe calculation, aggregation, and transformation.
# 
# ![Pokemon](../images/pokemon.jpg)
# 
# Follow the instructions below and enter your code.
# 
# #### Import all required libraries.

# In[1]:


# import libraries
import pandas as pd


# #### Import data set.
# 
# The dataset is here: https://drive.google.com/file/d/1Q3biC9Efii2eRhHcT81XsqSUqKBtK3Zc/view?usp=sharing . Read the data into a dataframe called `pokemon`.
# 
# *Data set attributed to [Alberto Barradas](https://www.kaggle.com/abcsds/pokemon/)*

# In[2]:


# import data set from Ironhack's database


#df=pd.read_csv('Pokemon.csv')
df = pd.read_csv('Pokemon.csv')
df


# #### Print first 10 rows of `pokemon`.

# In[3]:


print(df.head(10))


# When you look at a data set, you often wonder what each column means. Some open-source data sets provide descriptions of the data set. In many cases, data descriptions are extremely useful for data analysts to perform work efficiently and successfully.
# 
# For the `Pokemon.csv` data set, fortunately, the owner provided descriptions which you can see [here](https://www.kaggle.com/abcsds/pokemon/home). For your convenience, we are including the descriptions below. Read the descriptions and understand what each column means. This knowledge is helpful in your work with the data.
# 
# | Column | Description |
# | --- | --- |
# | # | ID for each pokemon |
# | Name | Name of each pokemon |
# | Type 1 | Each pokemon has a type, this determines weakness/resistance to attacks |
# | Type 2 | Some pokemon are dual type and have 2 |
# | Total | A general guide to how strong a pokemon is |
# | HP | Hit points, or health, defines how much damage a pokemon can withstand before fainting |
# | Attack | The base modifier for normal attacks (eg. Scratch, Punch) |
# | Defense | The base damage resistance against normal attacks |
# | SP Atk | Special attack, the base modifier for special attacks (e.g. fire blast, bubble beam) |
# | SP Def | The base damage resistance against special attacks |
# | Speed | Determines which pokemon attacks first each round |
# | Generation | Number of generation |
# | Legendary | True if Legendary Pokemon False if not |

# #### Obtain the distinct values across `Type 1` and `Type 2`.
# 
# Exctract all the values in `Type 1` and `Type 2`. Then create an array containing the distinct values across both fields.

# In[4]:


import numpy as np


# In[5]:


# Extract all unique values from 'Type 1' and 'Type 2' columns
T1_values = df['Type 1'].unique()
T2_values = df['Type 2'].unique()


# In[6]:


# Combine the two arrays and get distinct values
distinct_types = np.concatenate((T1_values, T2_values))

print(distinct_types)


# #### Cleanup `Name` that contain "Mega".
# 
# If you have checked out the pokemon names carefully enough, you should have found there are junk texts in the pokemon names which contain "Mega". We want to clean up the pokemon names. For instance, "VenusaurMega Venusaur" should be "Mega Venusaur", and "CharizardMega Charizard X" should be "Mega Charizard X".

# In[7]:


df['Name'].replace(to_replace=[r'\w+M'], value=['M'], regex=True, inplace=True)
df


# #### Create a new column called `A/D Ratio` whose value equals to `Attack` devided by `Defense`.
# 
# For instance, if a pokemon has the Attack score 49 and Defense score 49, the corresponding `A/D Ratio` is 49/49=1.

# In[8]:


df['A/D Ratio'] = df['Attack'] / df['Defense']

print(df)# your code here


# #### Identify the pokemon with the highest `A/D Ratio`.

# In[16]:


max_ratio = df['A/D Ratio'].max()
print("Highest A/D Ratio", max_ratio)


# your code here


# #### Identify the pokemon with the lowest A/D Ratio.

# In[18]:


min_ratio = df['A/D Ratio'].min()
print("Lowest A/D Ratio", min_ratio)# your code here


# #### Create a new column called `Combo Type` whose value combines `Type 1` and `Type 2`.
# 
# Rules:
# 
# * If both `Type 1` and `Type 2` have valid values, the `Combo Type` value should contain both values in the form of `<Type 1> <Type 2>`. For example, if `Type 1` value is `Grass` and `Type 2` value is `Poison`, `Combo Type` will be `Grass-Poison`.
# 
# * If `Type 1` has valid value but `Type 2` is not, `Combo Type` will be the same as `Type 1`. For example, if `Type 1` is `Fire` whereas `Type 2` is `NaN`, `Combo Type` will be `Fire`.

# In[19]:


df.fillna('', inplace=True)

# combine Type 1 and Type 2 columns using string concatenation and store in a new column
df['Combo Type'] = df['Type 1'] + '-' + df['Type 2']
print(df)


# #### Identify the pokemon whose `A/D Ratio` are among the top 5.

# In[21]:


top_5 = df.head(5)

# display the top 5 Pokémon
print(top_5['Name'])


# #### For the 5 pokemon printed above, aggregate `Combo Type` and use a list to store the unique values.
# 
# Your end product is a list containing the distinct `Combo Type` values of the 5 pokemon with the highest `A/D Ratio`.

# In[22]:


top_5 = df.head(5)

# aggregate the Combo Type column and store unique values in a list
combo_types = list(top_5['Combo Type'].unique())

# display the unique combo types for the top 5 Pokémon
print('Unique combo types:', combo_types)


# #### For each of the `Combo Type` values obtained from the previous question, calculate the mean scores of all numeric fields across all pokemon.
# 
# Your output should look like below:
# 
# ![Aggregate](../images/aggregated-mean.png)

# In[25]:


for combo_type in combo_types:
    # filter the DataFrame to include only rows with the current Combo Type
    filtered_df = df[df['Combo Type'] == combo_type]
    
    # calculate the mean scores of all numeric fields
    means = filtered_df.mean(numeric_only=True)
    # your code here

