# Racial and Ethnic Minorities Disproportionately Exposed to Extreme Daily Temperature Variation in the United States

[Shengjie Liu](https://skrisliu.com), [Emily Smith-Greenaway](http://emilysmithgreenaway.org/)

Code and Data: [https://github.com/skrisliu/dtvus](https://github.com/skrisliu/dtvus)

### Figure 1: World Maps of Daily Temperature Variation and Population Density

#### Population Density

The world’s annual mean daily temperature variation data in Fig. 1 is from the WorldClim v2 dataset 1970-2000, publicly available on [their website](https://www.worldclim.com/version2). 

#### Daily Temperature Variations

The population density data is from the NASA Center for International Earth Science Information Network at Columbia University. We use the gridded population of the world v4 in 2000-2020 ([https://sedac.ciesin.columbia.edu/data/collection/gpw-v4](https://sedac.ciesin.columbia.edu/data/collection/gpw-v4)).


### Figure 2: Distribution of the exposure to daily temperature variation (DTV) of White and non-White populations

### run the following scripts in order

#### 1. Generate population-weighted exposure data of each state by race and ethnicity, save the data in folder
  -- t20240224a_analysis_race.py

#### 2. Load the population-weighted exposure data, merged to White and non-White, then kernel density estimation
  -- t20240224b_plot_race.py

#### 3. Calculate K-S statistics
  -- t20240224c_kstest_all_Wasserstein.py

#### 4. Load the kernel density estimation of White and non-White populations from (2), load the statistics from (3), make Figure 2
  -- t20240224d_bigFigure_race.py
