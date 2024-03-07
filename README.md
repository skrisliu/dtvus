# Racial and Ethnic Minorities Disproportionately Exposed to Extreme Daily Temperature Variation in the United States

[Shengjie Liu](https://skrisliu.com), [Emily Smith-Greenaway](http://emilysmithgreenaway.org/)

Data and code are released here: [https://github.com/skrisliu/dtvus](https://github.com/skrisliu/dtvus)


## Figure 1

### Population Density

The world’s annual mean daily temperature variation data in Fig. 1 is from the WorldClim v2 dataset 1970-2000, publicly available on [their website](https://www.worldclim.com/version2). 

### Daily Temperature Variations

The population density data is from the NASA Center for International Earth Science Information Network at Columbia University. We use the gridded population of the world v4 in 2000-2020 ([https://sedac.ciesin.columbia.edu/data/collection/gpw-v4](https://sedac.ciesin.columbia.edu/data/collection/gpw-v4)).


## Figure 2

### Run the following scripts in order

#### 1. Generate population-weighted exposure data of each state by race and ethnicity, save the data in folder
    python makefig2_1.py

#### 2. Load the population-weighted exposure data, merge as White and non-White, then run kernel density estimation, save KDE in folder
    python makefig2_2.py

#### 3. Calculate K-S statistics
    python makefig2_3.py

#### 4. Load the kernel density estimation of White and non-White populations from (2), load the statistics from (3), make Figure 2
    python makefig2_4.py


## Figure 3

### Monthly DTV difference of 51 states, by race and ethnicity, income, and age
    python HeatMap.py
