# Crime-Data-Analysis

------------------------------------------------------------------------------
# **MAIN DATASET: NYPD COMPLAINTS (Historic)**
------------------------------------------------------------------------------

Team : ACHIEVERS (TEAM - 7)

1. Pruthviraj R Patil
2. Swathi Jain
3. Nithya Satish

------------------------------------------------------------------------------
# **PART - 1 : Working on main dataset**
------------------------------------------------------------------------------

## a. To get the required columns, use this module: 

1.   get_area_of_interest(df_spark, interested_columns)


## b. Data Preprocessing


###    a. Scaled peprocessing pipeline: Pass your data through these functions (if using other datasets and if your columns fall in those categories)

1.   valid_date_check(date)
2.   valid_time_check(time)
3.   reverse_geo_code_boros(df_spark, Latitude, Longitude, Boro, lat_index, long_index)
4.   refine_age_group_race(df_spark, victim_age_group=None, suspect_age_group=None, suspect_race=None, victim_race=None)
5.   refine_sex_gender_impute(df_spark, suspect_age=None, suspect_gender=None, victim_age=None, victim_gender=None)
6.   refine_precinct_jur(df_spark, precinct=None, Jur_code=None)

###.   b. Preprocessing modules curated in this notebook which are not associated with scaled preprocessing: 

1. level_of_offense_check()
2. KY_CD_Check()
3. hpsa_check()
4. prem_check()
5. pd_cd_check()

## c. Data Visualization

To bring out insights after data profiling

## d. Save the cleaned data

# ** ARCHITECTURE - FLOWCHART**


<img src="https://raw.githubusercontent.com/Aahbree/Crime-Data-Analysis/main/Screen%20Shot%202021-12-12%20at%209.01.42%20PM.png" width="800" height="800">


------------------------------------------------------------------------------
# **PART - 2: Working on other datasets**
------------------------------------------------------------------------------

## Instructions for running notebooks with different datasets:

I. Import dataset. (Links are given below)


1. NYPD vehicle collision data
https://data.cityofnewyork.us/Public-Safety/Motor-Vehicle-Collisions-Crashes/h9gi-nx95 
 
2. NYPD Attests Data
https://data.cityofnewyork.us/Public-Safety/NYPD-Arrests-Data-Historic-/8h9b-rp9u 
 
3. NYPD Shooting Incident Data
https://data.cityofnewyork.us/Public-Safety/NYPD-Shooting-Incident-Data-Historic-/833y-fsy8 
 
4. NYPD Criminal Court Summons Data
https://data.cityofnewyork.us/Public-Safety/NYPD-Criminal-Court-Summons-Historic-/sv2w-rv3k 
 
5. NYPD Summons Historic Data
https://data.cityofnewyork.us/Public-Safety/NYPD-B-Summons-Historic-/bme5-7ty4 
 
6. NYPD Service Calls Data
https://data.cityofnewyork.us/Public-Safety/NYPD-Calls-for-Service-Historic-/d6zx-ckhd 
 
7. NYPD Incident Data
https://data.cityofnewyork.us/Public-Safety/NYPD-Use-of-Force-Incidents/f4tj-796d 
 
8. Incidents Responded Data
https://data.cityofnewyork.us/Public-Safety/Incidents-Responded-to-by-Fire-Companies/tm6d-hbzd 

9. Emergency Response Incidents
https://data.cityofnewyork.us/Public-Safety/Emergency-Response-Incidents/pasr-j7fb

10. Rodent Inspection Data
https://data.cityofnewyork.us/Health/Rodent-Inspection/p937-wjvj

II. Select the columns of interest from the datasets.

III. Use the modules to preprocess the dataset as required

IV. Save the datasets to CSV files
