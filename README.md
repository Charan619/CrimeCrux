# CrimeCrux

- Kirushikesh DB, Charan KR, Jeyakumaran

## Problem Statement 2: Crime Analysis & Safety recommendation

### Features

- Visual Heat-map dashboard for each category of crime

- Crime index per population for each State

- Advisory to users travelling to high crime locations

- Crime forecast for current year

### Visual Heat-map dashboard for each category of crime

Understanding large amount of data across many years and states is almost imposible with just lines and numbers. To make things simpler for the user we implemented a country-wide heat map for each given year and crime category.

### Crime index per population for each State

India is a very large country with varying population densities for each district. This introduces an implicit bias for states with high population and showcases them in a bad light. To solve this we showed the data normalized for population to understand which states have high crime per capita

### Advisory to users travelling to high crime locations

Given a starting and ending location for travel we inform the user with insights about differences in crime activity for each major category and also give them apropriate tips to ensure safety of the user.

### Crime forecast for current year

The dataset available tracks crime only from 2001-2014. This proposes a problem where the crime data might not be accurate in the current scenario. To solve this we forecasted the data using ARIMA.

### Improvements/Ideas

Giving travel advisory to user for each district between start and end location as well ( by calculating path )





