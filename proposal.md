# Proposal
### Aishwarya SHarma, Ling Xiang Zou, Sean Casey, Tingwen Hua

---

## Motivation and Purpose

Our role: Data scientist consultancy firm

Target audience: Natural Resources Canada renewable energy planning committee

The growth and development of renewable energy sources as replacements for fossil
fuels is an important aspect of combatting climate change. In order to develop
Canada's national strategy for renewable energy production in Canada, it is
important to understand the current situation and the history of existing wind
power production in Canada. To accomplish this, we propose building a data
visualization app that allows members of Natural Resources Canada planning 
committees to visually explore a dataset detailing existing windpower capacity 
in Canada. Our dashboard will show the different variables that contribute to
the overall existing windpower capacity within Canada, and allow the user to 
filter on different variables to explore different aspects of the data.   

---

## Description of the data

We will be visualizing a dataset of approximately 6,500 existing wind power 
turbines in Canada. Each turbine entry has 13 different numerical and categorical 
variables that describe the location within Canada (province/territory, latitude, 
longitude), the project to which the turbine belongs (project name, total project 
capacity, number within project), and the turbine itself (turbine id, rated 
capacity, rotor diameter, hub height, manufacturer, model, and commissioning 
year). Using this data, we will be able to calculate new aggregated variables 
such as total power capacity per province, and yearly total cumulative turbine 
count. 

---

## Research questions and usage scenario

Francois is a bureaucrat in Canada's Department of Natural Resources, who sits 
on a planning committee that is drafting policy regarding the direction of 
future developments of wind power projects within Canada. As part of his 
research, he wants to explore a dataset in order to find patterns in how wind 
power generation in Canada has changed over time, and how the different 
provinces and territories of Canada differ from each other in respect to wind 
power capacity. When Francois first visits our windpower visualization 
dashboard, he will see an overview of the available data on a national level,
including change in wind power generation capacity over time, and the locations
of existing wind power projects within Canada. He can filter the data by 
province to see which provinces have the most or the least wind power capacity,
for example. He can also filter the data by turbine capacity ranges to see where
the turbines with the largest power generation capacities are located within
the country. Francois may notice that certain provinces have much greater wind
power capacity than others, or that the largest turbines tend to be clustered in
specific areas of the country. He might hypothesize that these clustered pockets
of wind power development in the country could be correlated with areas of 
increased population density that have a greater energy demand, or geographic 
regions which have a typically windy climate that is suitable for wind power 
generation. Francois may decide that he needs to conduct a follow-up 
investigation that includes examination of demographic and climate information 
that is not included in the current data set. 