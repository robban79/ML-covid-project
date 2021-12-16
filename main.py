#!/usr/bin/env python3
"""
Project description:
The novel corona-virus COVID-19 has left its mark individuals, families and society as a whole.
Your task in this project is a quite open ended one: analyze and visualize the years 2019, 2020 and 2021 in the context of how people perceived the more severe global pandemic of our times.
Here are a number of datasets you can use:

EU media releases (in Swedish) (downloaded from consilium.europa.eu),
Twitter comments (downloaded from kaggle.com),
Country vaccinations (downloaded from kaggle.com),
Reddit comments about vaccinations (downloaded from kaggle.com),
Covid-19 deaths in Sweden (downloaded from scb.se),
Deaths/infections/recovery data from countries all over the world (downloaded from kaggle.com),
Excerpt of Trump tweets talking about themes surrounding COVID-19 (downloaded from thetrumparchive.com)
Disclaimer: Some of the data sources contain texts and impressions from social media. The data is uncurated and may contain inappropriate comments. Viewer discression is adviced.

You can choose what you want to investigate and connect the different datasets to tell a story! Some pointers to get you started:

1)
You may want to make a timeline of the pandemic in the EU, combining the death/infections data with press releases and selected impressions from people on reddit and twitter!

The data is unfortunately not complete so you may want to focus on parts of the timeline or incorporate more data into your visualization as time progresses!

You may want to visualize in a chart the progression of death/infection rates and insert news headlines at particular times.

You may also want to see how the number of post/tweets changes over time mentioning COVID-19. Donald Trumps tweets may also be included.

There are many more ways of combining the data for interesting analysis, be creative! Have Fun!

For reporting, use this jupyter notebook to make illustrations and analyze the data and submit it on the hub. Create all the cells you need.
"""
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

"""
Population in sweden
from http: // www.statistikdatabasen.scb.se /
"""
# Population in sweden
population_swe = {'2015': 9851017, '2016': 9995153, '2017': 10120242,
                  '2018': 10230185, '2019': 10327589, '2020': 10379295,
                  '2021': 0}


def fill_population_swe():
    """
    fill missing data in swe population from scb by fitting curve to int.
    Assuming curve population growth to be linear
    """
    def line_func(x, a, b):
        return a * x + b

    popt, _ = curve_fit(line_func, range(0, 6), list(population_swe.values())[:6])
    population_swe['2021'] = int(popt[0] * 6 + popt[1])

    print(f'Population swe:\n {population_swe}')


def mortality_swe_2015_2021():
    """
    Compare mortality in swe over time compared with population.
    """
    def death_per_population(row_data):
        return row_data.tot_dead / population_swe[row_data.year] * 100

    def population(row_data):
        return population_swe[row_data.year] / 1000

    # Read the file
    headers = ['Date', '2015', '2016', '2017', '2018', '2019', '2020', '2021']
    d_type = {'Date': str, '2015': int, '2016': int, '2017': int, '2018': int,
              '2019': int, '2020': int, '2021': int}

    df_raw = pd.read_excel('CovidDeathsSweden.xlsx', sheet_name='Tabell 1',
                           skiprows=7, header=None, names=headers,
                           dtype=d_type,
                           usecols=range(len(headers)))

    # Fill in missing data in 2021 with average from January. Perhaps to small
    # of a dataset, but it will do for this experiment
    df_raw.loc[30:, ['2021']] = pd.NA
    avr_2021 = int(df_raw.loc[:, ['2020']].mean())
    df_raw = df_raw.fillna(avr_2021)
    # Create mortality df
    mortality_swe = df_raw.drop(columns=['Date']).sum(
        axis=0).to_frame().reset_index()

    mortality_swe.columns = ['year', 'tot_dead']
    mortality_swe['percent'] = mortality_swe.apply(death_per_population,
                                                   axis=1)
    mortality_swe['population'] = mortality_swe.apply(population, axis=1)

    print(f'Mortality data swe:\n {mortality_swe}')

    fig, ax1 = plt.subplots(figsize=(12, 6))
    plt.title("SWE: Total dead and population in [k]")
    plt.ylim(85000, 115000)
    sns.barplot(x='year', y='tot_dead', data=mortality_swe, ax=ax1)
    ax2 = ax1.twinx()
    sns.lineplot(data=mortality_swe['population'], marker='o', sort=False,
                 ax=ax2)
    plt.show()

    fig, ax1 = plt.subplots(figsize=(12, 6))
    plt.title("SWE: Total dead and percentage of population")
    plt.ylim(85000, 115000)
    sns.barplot(x='year', y='tot_dead', data=mortality_swe, ax=ax1)
    ax2 = ax1.twinx()
    sns.lineplot(data=mortality_swe['percent'], sort=False, markers=True,
                 dashes=False,
                 ax=ax2)
    plt.show()

def mortality_swe_2015_2021_per_week():
    """
    Compare mortality in swe over time compared with population.
    """
    # Read the file
    headers = ['Week', '2015', '2016', '2017', '2018', '2019', '2020', '2021']
    d_type = {'Week': str, '2015': float, '2016': float, '2017': float, '2018': float,
              '2019': float, '2020': float, '2021': float}

    df_raw = pd.read_excel('CovidDeathsSweden.xlsx', sheet_name='Tabell 5',
                           skiprows=11, header=None, names=headers,
                           dtype=d_type,
                           usecols=range(len(headers)))
    df_raw.loc[4:, ['2021']] = pd.NA
    df_raw.plot.line()
    plt.show()

def media_sv():
    # Headline, body, date


if __name__ == "__main__":
    #fill_population_swe()
    mortality_swe_2015_2021()
    mortality_swe_2015_2021_per_week()




