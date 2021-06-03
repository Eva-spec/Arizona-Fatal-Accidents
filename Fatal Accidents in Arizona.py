#!/usr/bin/env python
# coding: utf-8

# # Arizona Fatal Accidents from 2012-2016
# 
# ### BRIEF
# * This is a basic version of the two main tables in the Fatality Accident Reporting System as published on NHTSA's.
# ### SOURCE:
# <b> This data contains two datasets one is about accidents that is accident.tsv and another is about vehicles that is vehicle.tsv.</b>
# https://data.world/cronkite-data/azfars
# * Analytic manual and detailed record layouts and instructions: https://crashstats.nhtsa.dot.gov/Api/Public/ViewPublication/812447
# 
# * Auxiliary file layouts:
# https://crashstats.nhtsa.dot.gov/Api/Public/ViewPublication/AUXF_A
# 
# ### DATA SELECTION AND OBJECTIVE:
# <b> I have taken this data in consideration due to following reasons:</b>
# * Firstly open source data ,so one can download without any restrictions.
# * It fulfills the requirements of this project
# * It is an interesting data as I have two datasets which i am going to merge for further detailed EDA
# * I will find out famous city for accident 
# * contribution of weather and speed in accident will be analysed in this.
# * Hypothesis testing to prove aur finding.
# 
# 
# 
# 
# ### DATA PROPERTIES:
# ### Accident Data
# * Number of columns:79
# * Number of Rows:3904
# #### Columns detail:
# 
# * accident_id - id related to the accident
# * st_case - Consecutive Number
# * ve_total - Number of Vehicle Forms Submitted
# * ve_forms - Number of Vehicle Forms Submitted for MV In Transport
# * peds - Number of Forms Submitted for Persons Not in Motor Vehicles
# * persons - Number of MV Occupant
# * county - county name
# * country - country name
# * city - city
# * city_name - city name
# * day - Crash Date (Day)
# * month - Crash Date (Month)
# * year - Crash Date (Year)
# * hour - Crash Time (Hour)
# * minute - Crash Time (Minute)
# * nhs - National Highway System
# * func_sys_lit - Functional System
# * road_fnc_lit - Roadway Function Class
# * rd_owner_lit - Ownership
# * tway_id - Trafficway Identifier (1)
# * tway_id2 - Trafficway Identifier (2)
# * latitude - Global Position (Latitude)
# * longiture - Global Position (Longitude)
# * sp_jur_lit - Special Jurisdiction
# * harm_ev_lit - First Harmful Event
# * man_col_lit - Manner of Collision
# * reljct1 - Relation to Junction Within Interchange Area
# * reljct2 - Relation to Junction - Specific Location
# * typ_int - Type of Intersection
# * wrk_zone - Work Zone
# * rel_road - Relation To Trafficway
# * lgt_cond_lit - Light Condition
# * weather_lit - Atmospheric Conditions
# * sch_bus - School Bus Related
# * cf1_lit - Related Factors (1)
# * cf2_lit - Related Factors (2)
# * cf3_lit - Related Factors (3)
# * fatals - Fatalities
# * a_inter_lit - interstate
# * a_road_fc_lit - roadway function class
# * a_tod_lit - Time of Day
# * a_dow_lit - day of week
# * a_lt_lit - involving a large truck
# * a_spcra_lit - Involving Speeding
# * a_ped_lit - Involving a Pedestrian
# * a_ped_f_lit - Involving a Pedestrian Fatality
# * a_pedal_lit - Involving a Pedalcyclist
# * a_pedal_f - Involving a Pedalcyclist Fatality
# * a_polpur_lit - Involving a Police Pursuit
# * a_posbac - Involving a Driver With Positive BAC
# * a_dist_lit - Involving a Distracted Driver
# * a_drowsy_lit - Involving a Drowsy Driver
# * indian_res - Indian Reservation based on special jurisdiction and geographic location data
# 
# 
# ### Vehicle data
# 
# * Number of rows:5889
# * Number of columns:131
# 
# ### Columns detail:
# 
# * state - State Number
# * st_case - Consecutive Number
# * veh_no - Vehicle Number
# * ve_forms - Number of Vehicle Forms Submitted for MV In Transport
# * numoccs - Number of Occupants
# * day - Crash Date (Day)
# * month	- Crash Date (Month)
# * hour - Crash Time (Hour)
# * minute - Crash Time (Minute)
# * harm_ev - First Harmful Event
# * man_coll - Manner of Collision
# * unittype - Unit Type	
# * hit_run - Hit and Run
# * reg_stat - Vehicle Registration State
# * owner - Registered Vehicle Owner
# * make - Vehicle Make
# * model - Vehicle Model
# * mak_mod - Make Model Combined
# * body_type - Body Type	
# * mode_year - Vehicle Model Year
# * vin_vechile - Identification Number
# * vin_1 - VIN Character(1)
# * vin_2 - VIN Character(2)
# * vin_3 - VIN Character(3)
# * vin_4 - VIN Character(4)
# * vin_5 - VIN Character(5)
# * vin_6 - VIN Character(6)
# * vin_7 - VIN Character(7)
# * vin_8 - VIN Character(8)
# * vin_9 - VIN Character(9)
# * vin_10 - VIN Character(10)
# * vin_11 - VIN Character(11)
# * vin_12 - VIN Character(12)
# * tow_veh - Vehicle Trailing
# * j_knife - Jackknife	
# * mcarr_i1 - MCID Issuing Authority
# * mcarr_i2 - MCID Identification Number
# * mcarr_id - Motor Carrier Identification Number
# * gvwr - Gross Vehicle Weight Rating
# * v_config - Vehicle Configuration
# * cargo_bt - Cargo Body Type
# * haz_inv - Hazardous Materials Involvement/Placard-HM1 -Involvement
# * haz_plac - Hazardous Materials Involvement/Placard-HM2 Placard
# * haz_id - Hazardous Materials Involvement/Placard- HM3 Identification Number
# * haz_cno - Hazardous Materials Involvement/Placard-HM4 Class Number
# * haz_rel - Hazardous Materials Involvement/Placard-HM5 Released
# * bus_use - Bus Use	
# * spec_use - Special Use
# * emer_use - Emergency Use
# * trav_sp - Travel Speed
# * underride - Underride/Override
# * rollover - Rollover Type
# * rolinloc - Location of Rollover
# * impact1 - Areas of Impact - Initial Contact Point
# * deformed - Extent of Damage
# * towed - Vehicle Removal
# * m_harm - Most Harmful Event
# * veh_sc1 - Vehicle Related Factors (1)
# * veh_sc2 - Vehicle Related Factors (2)
# * fire_exp - Fire Occurrence
# * dr_pres - Driver Presence
# * l_state - Driver License State
# * dr_zip - Driver ZIP Code
# * l_status - Non-CDL License Status
# * l_type - Non-CDL License Type
# * cdl_stat - Commercial MV License Status
# * l_endors - Compliance with CDL Endorsements
# * l_cmpl - License Compliance with Class of Vehicle
# * l_restri - Compliance with License Restrictions
# * dr_hgt - Driver Height
# * dr_wgt - Driver Weight
# * prev_acc - Previous Recorded Crashes
# * prev_sus - Previous Recorded Suspensions and Revocations
# * prev_dwi - Previous DWI Convictions
# * prev_spd - Previous Speeding Convictions
# * prev_oth - Previous Other Moving Violation Convictions
# * first_mo - Date of First Crash, Suspension or Conviction (Month)
# * first_yr - Date of First Crash, Suspension or Conviction (Year)
# * last_mo - Date of Last Crash, Suspension or Conviction (Month)
# * last_yr - Date of Last Crash, Suspension or Conviction (Year)
# * speedrel - Speeding Related
# * dr_sf1 - Driver Related Factors (4 choices)
# * dr_sf2 - Driver Related Factors (4 choices)
# * dr_sf3 - Driver Related Factors (4 choices)
# * dr_sf4 - Driver Related Factors (4 choices)
# * vtrafway - Trafficway Description

# ## 1. Import Libraries

# In[3]:


import os
import re
from datetime import datetime as dt
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")
## getting path
path = os.getcwd()


# ## 2. Import Data

# ### 2.1 Accident data
# 
# Below are the accident data for each accident happened from 2012 through 2016.
# * For many fields, the original code and the translation of that code as provided by NHTSA are shown next to each other, with the original field name followed by that field name with the suffix “lit”, for “literal”.Example, if the original record layout contains a field called WEATHER, this file will include WEATHER as a numeric, coded field, and WEATHER_LIT as its translation.

# In[2]:


acci_df=pd.read_csv(r"accident.tsv",sep='\t')  ## importing accident.tsv data
print("Shape of the accident data is {}.".format(acci_df.shape))  ## getting shape
acci_df = acci_df.rename(columns=str.lower) ## converting all columns into lowercase data
acci_df.head(2)


# In[8]:


# Dataset information
#acc_df.info()
#acc_df.a_drowsy_lit


# ### 2.2 vehicle data
# 
# The data represents the vehicle involves in the accident.

# In[9]:


vech_df=pd.read_csv(r"vehicle.tsv", sep='\t') ## importing vehicle.tsv data
print("Shape of the vehicle data is {}.".format(vech_df.shape))  ## getting shape
vech_df = vech_df.rename(columns=str.lower) ## converting all columns into lowercase data
vech_df.head(5)  ## getting head


# In[10]:


vech_df.info()


# ### 2.3 Merging the dataset

# In[11]:


## merging accident and vehicle data on accident id
finalised_df = pd.merge(acci_df, vech_df, on=["accident_id", "st_case", "ve_forms", 'harm_ev', 'man_coll'])
### getting final shape and head
print("Shape of the data after merging all columns are {}.".format(finalised_df.shape))
### getting head
finalised_df.head(2)


# ## 3. Data Cleaning

# ### 3.1 Duplicate Column Analysis

# #### 3.1.1 removing all columns with encoded values and have _lit as other columns

# In[12]:


## as we can read above all columns with "lit" is the lireral meaning of the corresponding columns
col_remove = [i.replace("_lit", "") for i in list(finalised_df.columns) if "_lit" in i]
col_remove.remove('a_road_fc'); col_remove.remove('a_polour')  ## remove 
col_remove.append("a_roadfc"); col_remove.append("a_polpur")   ## appending same columns with different name

finalised_df_m1 = finalised_df.drop(columns = col_rem)   ## drop columns
## sanity check
print("Shape after dropping the encoded columns is {}.".format(finalised_df_m1.shape))


# #### 3.1.2 removal of redundent columns present in both accident and vehicle file

# In[13]:


## we saw there were many columns with duplicate information in all three columns now it has come as _x, _y
## we need to check and remove the redundent one
dup_column = sorted([i for i in list(finalised_df_m1.columns) if (i[-2:] in "_x") or (i[-2:] in "_y")])
## checking values
finalised_df_m1[dup_col].head()


# In[14]:


## removing all redundent columns
dup_col_remove = sorted([i for i in list(finalised_df_m1.columns) if (i[-2:] in "_y")])
finalised_df_m2 = finalised_df_m1.drop(columns = dup_col_remove)
## sanity check
print("Shape after removing redundent columns are {}.".format(final_df_m2.shape))


# ### 3.2 Null Values Analysis
# 
# * The dataset contains null values in the form of None,NONE LISTED,UNKNOWN and "." inside the columns. Before proceeding into analysis, we must replace these values as well.

# In[15]:


## there are some columns with null values as none and "."
for col in finalised_df_m2.columns:
    finalised_df_m2[col] = finalised_df_m2[col].replace("None", np.nan)
    finalised_df_m2[col] = finalised_df_m2[col].replace(".", np.nan)
    finalised_df_m2[col] = finalised_df_m2[col].replace("NONE LISTED", np.nan)   ## city name
    finalised_df_m2[col] = finalised_df_m2[col].replace("UNKNOWN", np.nan)   ## city name


# In[16]:


#getting missing value counts
count = finalised_df_m2.isnull().sum()

#getting missing value percentage
percent = 100 * ((finalised_df_m2.isnull().sum()) / (final_df_m2.shape[0]))

#creating dataframe and renaming column
table = pd.concat([count, percentage], axis=1).rename(columns = {0:"missing_count", 1:"missing_percentage"})


# In[17]:


## show table with only missing percentage more than 40%
table[table['missing_percentage'] > 40].round(2).transpose()


# ### Observation
# * To keep all the values with more than 40% null values is not logical. So removing all columns at once.

# In[18]:


to_drop = list(table[table['missing_percentage'] > 40].transpose().columns)  ## getting column names to drop
finalised_df_m3 = finalised_df_m2.drop(columns = to_drop)  ### dropping all selected columns
## sanity check
print("Shape after dropping the null columns is {}.".format(finalised_df_m3.shape))


# ### 3.3 Duplicate rows analysis

# In[19]:


## checking for duplicate rows
finalised_df_m3[finalised_df_m3.duplicated()]


# ### Result:
# * no duplicate data is present.

# ### 3.4 Redundent Feature Removal

# In[20]:


## as we have date column we can map it into one
finalised_df_m3["date_time"] = finalised_df_m3["day_x"].apply(str) + "-" + finalised_df_m3["month_x"].apply(str) + "-"+ finalised_df_m3["year_x"].apply(str)

## dropping day, month, year, minutes columns
## also city and county are redundent with city name and county name
finalised_df_m4 = finalised_df_m3.drop(columns = ["day_x", "month_x", "year_x", "minute_x", "county", "city"])


# In[21]:


### vin_vechile - Identification Number
### the number is present indivilually as we can see
finalised_df_m5 = finalised_df_m4.drop(columns = list(final_df_m4.iloc[:,53:65].columns))
## showing output
finalised_df_m4.iloc[:,52:65].head(1)


# In[22]:


## sanity check
print("Shape after dropping the unnecessary columns are {}.".format(finalised_df_m5.shape))


# In[23]:


### copy the final dataframe into another one
df = finalised_df_m5.copy(deep = True)


# ### Result:
# * Redundancy is removed.
# * two columns has made compact such rather than using 12 different columns for vehicle identification ,we can use one compact identification number vin only.

# ## Analysis with Visualization for easy understanding.

# ## 4. Exploratory Data Analysis

# ### 4.1 details about accident 

# * The total number of accident details present in the dataset is 3904, where as the dataset contains accident id multiple times as there are multiple vehicle involved in the accident. 
# * Let's analyse that.

# In[24]:


### bar plot function
def bar_plot(data, xlabel_, ylabel_, title_, num, size, color):
    """
    This function produces bar plot using pandas plot attribute
    """
    plot = data.value_counts()[0:num].plot(kind="bar", figsize=size, color=color)
    plt.xlabel(xlabel_, fontsize=15)
    plt.ylabel(ylabel_, fontsize=15)
    plt.title(title_, fontsize=15)
    plt.show()


# In[25]:


print("There are {} accident id present in the dataset.".format(len(df["accident_id"].unique())))


# In[26]:


bar_plot(df["accident_id"], "accident id", "count", "Total number of vehicle involved in each accident", 30, (10,5), color="blue")


# ### Observation:
# * Although its weird to see that more than 16 vehicles are associated with one accident id,but sometimes due sudden breaking multiple cars bumps into each other.

# In[27]:


df[df["accident_id"] == 2013040743]


# ### Observation:
# * As we can see above 2013040743 accident id present 17 times in the dataset.
# .

# ### 4.2 Accident in a particular day
# 
# * To check the number accidents happened on the particular dates we must take unique data to analyse it.

# #### Creation of a temporary dataframe to get the unique accident id only

# In[28]:


## dropping all redundent columns with accident_id and keeping the first row
temporary_df = df.drop_duplicates(subset = ["accident_id"], keep="first")


# In[29]:


bar_plot(temporary_df["date_time"], "day_month_year", "count", "Accident happened on dates", 50, (15,3), color = "green")


# ### observation:
# * The maximum accident happend on a single date is 8. There are 5 accident id present with 8 accidents in a single day only.
# * In 2014 maximum accident happend on one day is 7 .

# ### 4.3 Here's the yearwise count of accidents?
# 

# In[30]:


## getting years from date time column to check how many accidents happening year wise
temporary_df["year"] = temporary_df["date_time"].apply(lambda x : x[-4:])
## getting dictionary of thr year and number of accidients
getting_dict = temporary_df["year"].value_counts().sort_index().to_dict()
print(getting_dict)


# In[31]:


## getting key and values from the dictionaries
labels = getting_dict.keys(); values = getting_dict.values()
plt.figure(figsize=(6,6))
plt.pie(values, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
plt.title("Number of accidents per year", fontsize=15)
plt.show()


# ### Observation:
# * As we see the last 5 years of trend, we can say that accident rate has increased from 2014 to 2016 constantly.
# * In 2016 the most number of accidents recorded.

# ### 4.4 During which month-year the accident rate is high?

# In[47]:


### bar plot function unsorted
def bar_plot_unsorted(data, xlabel_, ylabel_, title_, num, size, color):
    """
    This function produces bar plot using pandas plot attribute
    """
    plot = data.value_counts().sort_index()[0:num].plot(kind="bar", figsize=size, color=color)
    plt.xlabel(xlabel_, fontsize=15)
    plt.ylabel(ylabel_, fontsize=15)
    plt.title(title_, fontsize=15)
    plt.show()


# In[56]:


temporary_df["my"] = temporary_df["date_time"].apply(lambda x : x.split("-")[2] + "-" + x.split("-")[1])
temporary_df["my"] = temporary_df["my"].apply((lambda x : dt.strptime(x, '%Y-%m')))
temporary_df["my"] = temporary_df["my"].dt.strftime('%Y-%m')


# In[57]:


bar_plot_unsorted(temporary_df["my"], "month&year combination", "count", "Accident rate", 48, (15,3), color = "magenta")


# ### Observation:
# * The most of the accidents recored during the month of march 2015.
# * I didn't find any particular pattern here of the accidents. But the volume of accidents during the month of march is very high yearly.

# ### 4.5 During which hour accident rates are high?
# 

# In[35]:


bar_plot_unsorted(temporary_df["hour_x"], "hours", "count", "accident count per hours", 24, (15,4), "black")


# ### Observation
# * As we can see the accident mostly happened during evening to night time, from 5PM to 10PM.
# * This may happen due to the rush in the roads during the night time.

# ### 4.6 Travel speed of vehicle
# 
# * The data is given with a travel speed of the vehicle column as well. We must analyse it.

# In[36]:


## distribution plot
plot = sns.distplot(df["trav_sp"], color="red", kde=True)
plt.title("Distribution plot of travel speed of the vehicle", fontsize=20)
plt.show()

## bot plot
plot = plt.boxplot(df["trav_sp"].values)
plt.ylabel("range", fontsize=15)
plt.title("Travel Speed Analysis", fontsize=20)
plt.show()


# ### Observation
# * As we can see above the travel speed starts from "0" unit but it had values more than 900 as well. 
# * Though the unit is not present I am generalizing it with km/hr.
# * It seems weird, as boxplot shows there is no outlier. We must do percentile analysis here.

# In[58]:


### percetile analysis
###sanity check

ls1 = [(val, np.percentile(df["trav_sp"].values, val)) for val in range(0,91,10)]
ls2 = [(val, np.percentile(df["trav_sp"].values, val)) for val in range(91,100)]
ls3 = [(val, np.percentile(df["trav_sp"].values, val)) for val in [99.1,99.2,99.3, 99.4, 99.5, 99.6, 99.7, 99.8, 99.9, 100]]
## extending class
ls1.extend(ls2); ls1.extend(ls3)
## getting x and y
percent = [val[0] for val in ls1]
print(percent)
values = [val[1] for val in ls1]
print(values)
fig, ax = plt.subplots(ncols=3, figsize=(15,3))
## getting for 0-90
ax[0].plot(percent[0:10], values[0:10], 'r-o')
ax[0].set_xticks(percent[0:10])
ax[0].set_title("Percentile Analysis for 0 to 90")
## getting for 90-99
ax[1].plot(percent[10:19], values[10:19], 'g-o')
ax[1].set_xticks(percent[10:19])
ax[1].set_title("Percentile Analysis for 91 to 99")
## getting for 99.1 to 99.9
ax[2].plot(percent[19:], values[19:], 'b-o')
ax[2].set_xticks(percent[19:])
ax[2].set_title("Percentile Analysis for 99.1 to 99.9")
plt.show()


# In[38]:


print("The 63rd percentile of the travel speed is {:.2f} units.".format(np.percentile(df["trav_sp"].values, 63)))
print("The 64rd percentile of the travel speed is {:.2f} units.".format(np.percentile(df["trav_sp"].values, 64)))


# ### Observation:
# * From above analysis we conclude that 34 percentile of the values present in the travel speed section is junk and full of outliers which 998. This anomaly coz a vehicle can't go more than 1000km/hr which is impossible.

# In[39]:


x = df[df["trav_sp"] < 120]["trav_sp"]

### after removal of outliers
plot = plt.boxplot(x)
plt.ylabel("range", fontsize=15)
plt.title("Travel Speed Analysis", fontsize=20)
plt.show()


# In[63]:


plot = sns.distplot(x, color="red", kde=True)
plt.title("Distribution plot of travel speed of the vehicle, after removing outliers", fontsize=15)
plt.show()


# * The average vehicle speed was betwen 30 to 60 units when accident happened.

# ### Q1 what is the probability of death and chances of to be alive according to the speed of vehicle?

# * using temp_df to analyse speed with death rate

# In[40]:


## creating dataframe for speed below 120 which is acceptable
speedo_df = df[df["trav_sp"] < 120]
## creating bins using panndas cut
speedo_df["bins_of_speed"] = pd.cut(x, bins=[0, 30, 60, 90, 120], include_lowest=True)
speedo_df


# In[41]:


### creating a new column of death or no death as yes or no
speedo_df["is_dead?"] = ["No" if i < 1 else "Yes" for i in speed_df["deaths"].values]
speedo_df["is_dead?"]


# In[42]:


fig = plt.figure(figsize=(15,5))
plot = sns.countplot(x="bins_of_speed", hue="is_dead?", data=speed_df)
plt.title("mortality rate with the speed of vehicle analysis", fontsize=20)
plt.show()


# ### Observation:
# * As we can see above vehicle in speed 0 to 60, the probability of death is less.
# * But if the speed is more than 60 it is severe and death rate is high.
# * Comparatively chances of to be alive are more when speed is less.

# ### 4.7 Fatality

# In[43]:


getting_dict = temp_df["fatals"].value_counts().sort_index().to_dict()
print(getting_dict)

## getting key and values from the dictionaries
labels = getting_dict.keys(); values = getting_dict.values()
plt.figure(figsize=(8,8))
plt.pie(values, autopct='%1.1f%%', shadow=True, startangle=90)
plt.title("Fatality range", fontsize=15)
plt.legend(labels, loc='upper center', bbox_to_anchor=(1.45, 0.8))
plt.show()


# ### Conclusion:
# 
# * As we can see that 92.3% accidents were not severe,means fatality  is only 1
# * In one accident it is 7 which shows that only one  accident was quite severe.

# ### what was the weather condition during accidents?

# In[44]:


### getting plot for weather list
plot = df["weather_lit"].value_counts().plot(kind="bar", xlabel ="weather condition", ylabel="total count", figsize=(15,5), color="skyblue")
plt.title("What was the weather condition during accidents?", fontsize=15,)
plt.show()


# ### Observation:
# 
# * Most of the accidents happend when weather was clear.
# * It is observed that worse weather conditions did not contribute in accidents.

# ### In which city and corresponding country has the higher accident rate?

# In[45]:


df[["city_name", "county_name"]].value_counts()[0:20].plot(kind="bar", xlabel = "City with corressponding county", figsize=(15,5))
plt.ylabel("count")
plt.title("Number of accident happen in perticular county", fontsize=20)
plt.show()


# ### Observation:
# * Above analysis conclude that the most of the accidents happend in PHOENIX city's MARICOPA county,which were around 1400.

# ### How drinking and driving are related to death rate?
# 

# In[77]:


df["is_dead?"] = ["No" if i < 1 else "Yes" for i in df["deaths"].values]
fig = plt.figure(figsize=(10,5))
plot = sns.countplot(x="dr_drink", hue="is_dead?", data=df, palette="BuGn")
plt.title("mortality rate with the condition of drinking and driving", fontsize=20)
plt.show()


# ## 5. Correlation

# In[69]:


## selecting some particlular columns for correaltion which makes sense
column_list = ["accident_id", "nhs", "hour_x", "wrk_zone", "fatals", "deaths", "mak_mod", "mod_year", "trav_sp", "underide", "dr_drink"]
fig = plt.figure(figsize=(15,10))
sns.heatmap(df[column_list].corr(), annot=True, cmap="ocean",  fmt='.2f')
plt.show()


# ### Observation:
# * There is some relation between fatal accidents and deaths,so if accident is fatal then deaths would be high(38% chances).
# * From selected columns we plotted the correaltion and we didn't find any strong correaltion with any thing.
# * There is some correlation between make_mod(which is model of the vehicle) and mod_year(vechicle build on which year), but not enough to form a strong relationship.

# ## NULL HYPOTHESIS
# ## 6. Hypothesis Testing

# ### Assumption: There is no significant difference between deaths and people escaped in an accident  with respect to speed. It means severity of accident independent of speed.

# * the alpha = 0.05

# In[42]:


from scipy.stats import ttest_ind, norm

## to avoid the outliers issue in speed we are taking the speed_df as created above.
death_yes = speedo_df[speedo_df['is_dead?'] == "Yes"]
death_no = speedo_df[speedo_df['is_dead?'] == "No"]

yes_speed = death_yes["trav_sp"].values
no_speed = death_no["trav_sp"].values

ttest_ind(yes_speed, no_speed, equal_var=False)


# * As p-value is very very less than alpha, that means we reject the null hypothesis using t-test.
# * That mean there is a significant difference between death and alive rate according to the speed.
# * This means death rate or severity of accident depends upon speed of the vehicle .

# In[ ]:





# In[87]:


from scipy.stats import ttest_ind, norm

## to avoid the outliers issue in speed we are taking the speed_df as created above.
drink_n_drive_yes = speedo_df[speedo_df['dr_drink'] == 1]
drink_n_drive_no = speedo_df[speedo_df['dr_drink'] == 0]

yes_speed = drink_n_drive_yes["trav_sp"].values
no_speed = drink_n_drive_no["trav_sp"].values

ttest_ind(yes_speed, no_speed, equal_var=False)


# In[88]:


fig = plt.figure(figsize=(10,5))
plot = sns.countplot(x="bins_of_speed", hue="dr_drink", data=speedo_df, palette="prism")
plt.title("mortality rate with the speed of vehicle analysis", fontsize=20)
plt.show()


# In[90]:


speedo_df["dr_drink"].value_counts()


# In[91]:


3111/600


# In[94]:


drink_n_drive_yes["bins_of_speed"].value_counts()


# In[95]:


drink_n_drive_no["bins_of_speed"].value_counts()


# In[100]:


1015/87, 1471/306, 601/182,  24/25


# ## Summary:
# <b> After doing extensive analysis I came down to following conclusion</b>:
# 
# * we consider some factors such as weather,speed to check their impact on mortality and frequency of accidents and analysis concluded that most of accidents happened in clear weather ,but speead has a significant effect on mortality of accident .It means death rate is increases with surge in speed and more severe is accident.
# 
# * T-test done for hypothesis testing also rejects the null hypothesis as p value considerably less than alpha value and reveals that fatality depends upon speed.
# 
# * data was very vast as encoded information was present ,so i smplify the data by keeping relevent information which provided me substanial visualisation and made a compact dataset.
# * outliers are detected and removed to clean the data. main outlier was about speed ,which was showing car speed around 1000 which is impossible.
# * It is concluded that accidents are increasing incessantly.
# * Around 93% accidents are not much harsh.mortality is negligble .

# ## what I learned so far?
# * I performed statistical analysis and used advance visualisation with Seaborn and Matplotlib, which are crucial skills for a an aspiring Data scientist .
# * I learned about timeseries analysis and got idea about Extensive EDA and made some interesting insights.
# * Got to know,how important is data visualisation for a buisness. 
# * how to deal with  complex pattern and find out meaningful insight from them.

# ### Objective:
# * This analysis can be useful in reducing the number of accidents. As we all know, the majority of accidents occur between the hours of 5 and 10 p.m., which means more traffic on the roads. As a result, the NHS can take steps to regulate traffic to avoid accidents.
# * Since speed is directly linked to the seriousness of an accident, the NHS could create a new speed limit regulation.
