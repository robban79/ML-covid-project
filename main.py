#!/usr/bin/env python3
"""
Project description:
The novel corona-virus COVID-19 has left its mark individuals, families and society as a whole. Your task in this project is a quite open ended one: analyze and visualize the years 2019, 2020 and 2021 in the context of how people perceived the more severe global pandemic of our times. Here are a number of datasets you can use:

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

import pandas as pa

"""
http://www.statistikdatabasen.scb.se/
Population in sweden 
"""
population_swe = {'2015': 9851017, '2016': 9995153, '2017': 10120242,
                  '2018': 10230185, '2019': 10327589, '2020': 10379295,
                  '2021': None}


def main():
    # ----------------Deaths in sweden --------------------
    headers = ['Date', '2015', '2016', '2017', '2018', '2019', '2020', '2021']
    d_type = {'Date': str, '2015': str, '2016': str, '2017': str, '2018': str,
              '2019': str, '2020': str, '2021': str}
    df = pa.read_excel('CovidDeathsSweden.xlsx', sheet_name='Tabell 1',
                       skiprows=7, header=None, names=headers, dtype=d_type,
                       usecols=range(len(headers))
                       )
    print(df.head(10))


if __name__ == "__main__":
    main()
