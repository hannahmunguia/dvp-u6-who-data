
# coding: utf-8

# # Introduction
# 
# For this project, you will act as a data researcher for the World Health Organization. You will investigate if there is a strong correlation between the economic output of a country and the life expectancy of its citizens.  
# 
# During this project, you will analyze, prepare, and plot data, and seek to answer questions in a meaningful way.
# 
# After you perform analysis, you'll be creating an article with your visualizations to be featured in the fictional "Time Magazine".
# 
# **Focusing Questions**: 
# + Has life expectancy increased over time in the six nations?
# + Has GDP increased over time in the six nations?
# + Is there a correlation between GDP and life expectancy of a country?
# + What is the average life expactancy in these nations?
# + What is the distribution of that life expectancy?
# 
# GDP Source:[World Bank](https://data.worldbank.org/indicator/NY.GDP.MKTP.CD)national accounts data, and OECD National Accounts data files.
# 
# Life expectancy Data Source: [World Health Organization](http://apps.who.int/gho/data/node.main.688)
# 

# ## Step 1. Import Python Modules

# Import the modules that you'll be using in this project:
# - `from matplotlib import pyplot as plt`
# - `import pandas as pd`
# - `import seaborn as sns`

# In[91]:


from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns


# To look for connections between GDP and life expectancy you will need to load the datasets into DataFrames so that they can be visualized.
# 
# Load **all_data.csv** into a DataFrame called `df`. Then, quickly inspect the DataFrame using `.head()`.
# 
# Hint: Use `pd.read_csv()`
# 

# In[92]:


df = pd.read_csv('all_data.csv')
print(df.head())


# ## Step 2 Prep The Data

# The datasets are large and it may be easier to view the entire dataset locally on your computer. You can open the CSV files directly from the folder you downloaded for this project.
# 
# Let's learn more about our data:
# - GDP stands for **G**ross **D**omestic **P**roduct. GDP is a monetary measure of the market value of all final goods and services produced in a time period. 
# - The GDP values are in current US dollars.

# ## Step 3 Examine The Data

# What six countries are represented in the data?

# In[93]:


#Chile, China, Germany, Mexico, United States of America, Zimbabwe


# What years are represented in the data?

# In[94]:


#2000 to 2015


# ## Step 4 Tweak The DataFrame
# 
# Look at the column names of the DataFrame `df` using `.head()`. 

# In[95]:


df.head()


# What do you notice? The first two column names are one word each, and the third is five words long! `Life expectancy at birth (years)` is descriptive, which will be good for labeling the axis, but a little difficult to wrangle for coding the plot itself. 
# 
# **Revise The DataFrame Part A:** 
# 
# Use Pandas to change the name of the last column to `LEABY`.
# 
# Hint: Use `.rename()`. [You can read the documentation here.](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.rename.html)). </font>

# In[135]:


df.rename(columns = {'Life expectancy at birth (years)':'LEABY'}, inplace = True)


# Run `df.head()` again to check your new column name worked.

# In[97]:


df.head()


# ---

# To take a first high level look at both datasets, create a bar chart for each DataFrame:
# 
# A) Create a bar chart from the data in `df` using `Country` on the x-axis and `GDP` on the y-axis. 
# Remember to `plt.show()` your chart!

# In[137]:


x = df.Country
y = df.GDP

plt.figure(figsize = (24,24))
sns.set_palette("Set1")
plt.bar(x,y)
plt.title('How Does GDP Differ Per Country?')
plt.xlabel('Countries')
plt.ylabel('GDP')
sns.set_style('darkgrid')
sns.set_context('talk')
plt.xticks(rotation = 90)
sns.set_palette("Set1")
plt.savefig('How_Does_GDP_Differ_Per_Country_bar.png')
plt.show()


# B) Create a bar chart using the data in `df` with `Country` on the x-axis and `LEABY` on the y-axis.
# Remember to `plt.show()` your chart!

# ## Step 5 Bar Charts To Compare Average

# In[138]:


x = df.Country
y = df.LEABY
plt.figure(figsize = (24,24))
sns.set_style('darkgrid')
ax = plt.subplot()
sns.set_context('talk')
plt.xticks(rotation = 90)
plt.bar(x,y)
plt.title('How Does Life Expectancy At Birth (Years) Differ Per Country?')
plt.xlabel('Countries')
plt.ylabel('Life Expectancy')
sns.set_palette("Set1")
plt.savefig('How_Does_LEABY_Differ_Per_Country_bar.png')
plt.show()


# What do you notice about the two bar charts? Do they look similar?

# In[123]:


# there is no correlation between GDP and Life Expentancy


# ## Step 6. Violin Plots To Compare Life Expectancy Distributions 

# Another way to compare two datasets is to visualize the distributions of each and to look for patterns in the shapes.
# 
# We have added the code to instantiate a figure with the correct dimmensions to observe detail. 
# 1. Create an `sns.violinplot()` for the dataframe `df` and map `Country` and `LEABY` as its respective `x` and `y` axes. 
# 2. Be sure to show your plot

# In[139]:


plt.figure(figsize = (24,24))
sns.set_style('darkgrid')
sns.set_context('talk')
plt.xticks(rotation = 90)
plt.title('Violin Plots')
sns.violinplot(data = df, x = 'Country', y = 'LEABY')
sns.set_palette("Set1")
plt.savefig('Violin.png')
plt.show()
# This graphs shows that there is a longer rangeb between the confidence interval for China
# while that confidence interval range is smaller for the US and Mexico
# Mozambiques life expectancy changed the most


# What do you notice about this distribution? Which country's life expactancy has changed the most?

#  

# ## Step 7. Bar Plots Of GDP and Life Expectancy over time
# 
# We want to compare the GDPs of the countries over time, in order to get a sense of the relationship between GDP and life expectancy. 
# 
# First, can plot the progession of GDP's over the years by country in a barplot using Seaborn.
# We have set up a figure with the correct dimensions for your plot. Under that declaration:
# 1. Save `sns.barplot()` to a variable named `ax`
# 2. Chart `Country` on the x axis, and `GDP` on the `Y` axis on the barplot. Hint: `ax = sns.barplot(x="Country", y="GDP")`
# 3. Use the `Year` as a `hue` to differentiate the 15 years in our data. Hint: `ax = sns.barplot(x="Country", y="GDP", hue="Year", data=df)`
# 4. Since the names of the countries are long, let's rotate their label by 90 degrees so that they are legible. Use `plt.xticks("rotation=90")`
# 5. Since our GDP is in trillions of US dollars, make sure your Y label reflects that by changing it to `"GDP in Trillions of U.S. Dollars"`. Hint: `plt.ylabel("GDP in Trillions of U.S. Dollars")`
# 6. Be sure to show your plot.
# 

# In[125]:


plt.figure(figsize = (24,24))
ax = sns.barplot(x="Country", y="GDP", hue="Year", data=df)
sns.set_style('darkgrid')
sns.set_context('talk')
plt.xticks(rotation = 90)
plt.ylabel("GDP in Trillions of U.S. Dollars")
plt.title('How does the GDP Change Over the Years?')
sns.set_palette("Set1")
plt.savefig('GDP_Over_Years.png')
plt.show()


# Now that we have plotted a barplot that clusters GDP over time by Country, let's do the same for Life Expectancy.
# 
# The code will essentially be the same as above! The beauty of Seaborn relies in its flexibility and extensibility. Paste the code from above in the cell bellow, and: 
# 1. Change your `y` value to `LEABY` in order to plot life expectancy instead of GDP. Hint: `ax = sns.barplot(x="Country", y="LEABY", hue="Year", data=df)`
# 2. Tweak the name of your `ylabel` to reflect this change, by making the label `"Life expectancy at birth in years"` Hint: `ax.set(ylabel="Life expectancy at birth in years")`
# 

# In[126]:


plt.figure(figsize = (24,24))
ax = sns.barplot(x="Country", y="LEABY", hue="Year", data=df)
plt.xticks(rotation = 90)
ax.set(ylabel="Life expectancy at birth in years")
plt.title('How does The Life Expectancy at Birth Change Over the Years?')
sns.set_palette("Set1")
plt.savefig('LEABY_over_years.png')
plt.show()


# What are your first impressions looking at the visualized data?
# 
# - Which countries' bars changes the most?
# - What years are there the biggest changes in the data?
# - Which country has had the least change in GDP over time? 
# - How do countries compare to one another?
# - Now that you can see the both bar charts, what do you think about the relationship between GDP and life expectancy?
# - Can you think of any reasons that the data looks like this for particular countries?

# In[127]:


# GDP was steadily increasing for every country and so was the life expectancy (except for Zimbabwe where there was a slight decrease)

# Which countries' bars changes the most?
# From 2000 to 2015, China's CDP changed the most
# From 2000 to 2015, Zimbabwe's Life Expectancy At Birth Year changed the most

# What years are there the biggest changes in the data?
# 2004-2008

# Which country has had the least change in GDP over time?
# Zimbabwe

# How do countries compare to one another?
# The Life Expectancy At Birth Year was very similar for both Chile and Germany

# Now that you can see the both bar charts, what do you think about the relationship between GDP and life expectancy?
# There might be a slight possible correlation between the two but that might be a stretch


# Note: You've mapped two bar plots showcasing a variable over time by country, however, bar charts are not traditionally used for this purpose. In fact, a great way to visualize a variable over time is by using a line plot. While the bar charts tell us some information, the data would be better illustrated on a line plot.  We will complete this in steps 9 and 10, for now let's switch gears and create another type of chart.

# ## Step 8. Scatter Plots of GDP and Life Expectancy Data

# To create a visualization that will make it easier to see the possible correlation between GDP and life expectancy, you can plot each set of data on its own subplot, on a shared figure.
# 
# To create multiple plots for comparison, Seaborn has a special (function)[https://seaborn.pydata.org/generated/seaborn.FacetGrid.html] called `FacetGrid`. A FacetGrid takes in a function and creates an individual graph for which you specify the arguments!
#     
# Since this may be the first time you've learned about FacetGrid, we have prepped a fill in the blank code snippet below. 
# Here are the instructors to fill in the blanks from the commented word bank:
# 
# 1. In this graph, we want GDP on the X axis and Life Expectancy on the Y axis.
# 2. We want the columns to be split up for every Year in the data
# 3. We want the data points to be differentiated (hue) by Country.
# 4. We want to use a Matplotlib scatter plot to visualize the different graphs
# 
# 
# Be sure to show your plot!
# 

# In[128]:


# WORDBANK:
# "Year"
# "Country" 
# "GDP" 
# "LEABY" 
# plt.scatter


# Uncomment the code below and fill in the blanks
plt.figure(figsize = (10,15))
sns.set_style('darkgrid')
sns.set_context('talk',font_scale = 0.65)
g = sns.FacetGrid(data = df, col= 'Year', hue='Country', col_wrap=4, height=2)
g = (g.map(plt.scatter, "GDP", "LEABY", edgecolor="w").add_legend())
sns.set_palette("Dark2")
plt.savefig('FacetGrid_LEABY.png')
plt.show()


# + Which country moves the most along the X axis over the years?
# + Which country moves the most along the Y axis over the years?
# + Is this surprising?
# + Do you think these scatter plots are easy to read? Maybe there's a way to plot that! 

# In[129]:


# Which country moves the most along the X axis over the years?
# China

# Which country moves the most along the Y axis over the years?
# Zimbabwe

# Is this surprising?
# No! This data was derived from the old plots 

# Do you think these scatter plots are easy to read? Maybe there's a way to plot that!
# Add axis?


# ## Step 9. Line Plots for Life Expectancy

# In the scatter plot grid above, it was hard to isolate the change for GDP and Life expectancy over time. 
# It would be better illustrated with a line graph for each GDP and Life Expectancy by country. 
# 
# FacetGrid also allows you to do that! Instead of passing in `plt.scatter` as your Matplotlib function, you would have to pass in `plt.plot` to see a line graph. A few other things have to change as well. So we have created a different codesnippets with fill in the blanks.  that makes use of a line chart, and we will make two seperate FacetGrids for both GDP and Life Expectancy separately.
# 
# Here are the instructors to fill in the blanks from the commented word bank:
# 
# 1. In this graph, we want Years on the X axis and Life Expectancy on the Y axis.
# 2. We want the columns to be split up by Country
# 3. We want to use a Matplotlib line plot to visualize the different graphs
# 
# 
# Be sure to show your plot!
# 
# 

# In[130]:


plt.figure(figsize = (10,15))
sns.set_style('darkgrid')
sns.set_context('talk',font_scale = 0.65)
sns.set_palette("Set1")
g3 = sns.FacetGrid(df, col="Country", col_wrap=3, height=4)
g3 = (g3.map(plt.plot, "Year", "LEABY").add_legend())
plt.savefig('FacetGrid_Line_LEABY.png')
plt.show()


# Which countries' line changes the most?
# Zimbabwe had the largest slope

# What years are there the biggest changes in the data?
# Zimbabwe

# Which country has had the least change in life expectancy over time?
# USA (maybe Chile)

# Can you think of any reasons that the data looks like this for particular countries?
# Zimbabwe probably grew a lot because its life expectancy was really low and it would take basic 
# medical procedures to increase its life expectancy. 
# The USA probably stayed the same because it hasnt really had a unviersal health care system
# The countries that had little change were probably because it had basic technologies that were needed 
# to save lives of many children but still couldnt provide for everyone with more complicated cases 


# What are your first impressions looking at the visualized data?
# 
# - Which countries' line changes the most?
# - What years are there the biggest changes in the data?
# - Which country has had the least change in life expectancy over time? 
# - Can you think of any reasons that the data looks like this for particular countries?

#  

# ## Step 10. Line Plots for GDP

# Let's recreate the same FacetGrid for GDP now. Instead of Life Expectancy on the Y axis, we now we want GDP.
# 
# Once you complete and successfully run the code above, copy and paste it into the cell below. Change the variable for the X axis. Change the color on your own! Be sure to show your plot.
# 

# In[131]:


plt.figure(figsize = (10,15))
sns.set_style('darkgrid')
sns.set_context('talk',font_scale = 0.65)
sns.set_palette("Set2")
g3 = sns.FacetGrid(df, col="Country", col_wrap=3, height=4)
g3 = (g3.map(plt.plot, "Year", "GDP").add_legend())
plt.savefig('FacetGrid_Line_GDP.png')
plt.show()


# Which countries have the highest and lowest GDP?

# In[132]:


# The US has the highest GDP and Zimbabwe has the lowest


# Which countries have the highest and lowest life expectancy?

# In[133]:


# The Germany has the highest GDP and Zimbabwe has the lowest


# ## Step 11 Researching Data Context 

# Based on the visualization, choose one part the data to research a little further so you can add some real world context to the visualization. You can choose anything you like, or use the example question below.
# 
# What happened in China between in the past 10 years that increased the GDP so drastically?

# In[134]:


# Chinas education has been increasing and it is known that a more educated society 
# which could increase the jobs with a higher income

# It is also noted that china is still considered a "developing country" and so its 
# Carbon dioxide emissions have not been capped (like the US) particularly in coal burning. 
# Because of this, there are less egulation on the amount of environmental polution that 
# companies there are accountable for. This could increase the amount of production, thereby 
# increasing its GDP drastically over the last decade or so. 

# Sources
# https://www.weforum.org/agenda/2016/06/how-has-china-s-economy-changed-in-the-last-10-years/

. 


# ## Step 12 Create Blog Post

# Use the content you have created in this Jupyter notebook to create a blog post reflecting on this data.
# Include the following visuals in your blogpost:
# 
# 1. The violin plot of the life expectancy distribution by country
# 2. The facet grid of scatter graphs mapping GDP as a function Life Expectancy by country
# 3. The facet grid of line graphs mapping GDP by country
# 4. The facet grid of line graphs mapping Life Expectancy by country
# 
# 
# We encourage you to spend some time customizing the color and style of your plots! Remember to use `plt.savefig("filename.png")` to save your figures as a `.png` file.
# 
# When authoring your blog post, here are a few guiding questions to guide your research and writing:
# + How do you think the histories and the cultural values of each country relate to its GDP and life expectancy?
# + What would have helped make the project data more reliable? What were the limitations of the dataset?
# + Which graphs better illustrate different relationships??

# In[ ]:


# How do you think the histories and the cultural values of each country relate to its GDP and life expectancy?

# What would have helped make the project data more reliable? What were the limitations of the dataset?

# Which graphs better illustrate different relationships??


