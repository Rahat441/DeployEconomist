import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import seaborn as sns
import datetime
import panel as pn

pn.extension('plotly')



from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.ensemble import RandomForestRegressor

from sklearn.model_selection import train_test_split

from sklearn import metrics

#abbrevation
def us_state_to_abbrev(string):
    us_state_to_abbrev = {
        "Alabama": "AL",
        "Alaska": "AK",
        "Arizona": "AZ",
        "Arkansas": "AR",
        "California": "CA",
        "Colorado": "CO",
        "Connecticut": "CT",
        "Delaware": "DE",
        "Florida": "FL",
        "Georgia": "GA",
        "Hawaii": "HI",
        "Idaho": "ID",
        "Illinois": "IL",
        "Indiana": "IN",
        "Iowa": "IA",
        "Kansas": "KS",
        "Kentucky": "KY",
        "Louisiana": "LA",
        "Maine": "ME",
        "Maryland": "MD",
        "Massachusetts": "MA",
        "Michigan": "MI",
        "Minnesota": "MN",
        "Mississippi": "MS",
        "Missouri": "MO",
        "Montana": "MT",
        "Nebraska": "NE",
        "Nevada": "NV",
        "New Hampshire": "NH",
        "New Jersey": "NJ",
        "New Mexico": "NM",
        "New York": "NY",
        "North Carolina": "NC",
        "North Dakota": "ND",
        "Ohio": "OH",
        "Oklahoma": "OK",
        "Oregon": "OR",
        "Pennsylvania": "PA",
        "Rhode Island": "RI",
        "South Carolina": "SC",
        "South Dakota": "SD",
        "Tennessee": "TN",
        "Texas": "TX",
        "Utah": "UT",
        "Vermont": "VT",
        "Virginia": "VA",
        "Washington": "WA",
        "West Virginia": "WV",
        "Wisconsin": "WI",
        "Wyoming": "WY",
        "District of Columbia": "DC",
        "American Samoa": "AS",
        "Guam": "GU",
        "Northern Mariana Islands": "MP",
        "Puerto Rico": "PR",
        "United States Minor Outlying Islands": "UM",
        "U.S. Virgin Islands": "VI",
        }
    return us_state_to_abbrev[string]

df1 = pd.read_csv("Master_DF.csv")


df1_nat = df1[df1['GeoName'] == 'United States']
df1_nat["Abrev"] = "US"

df1_states = df1[df1['GeoName'].isin(['Alabama', 'Alaska', 'Arizona', 'Arkansas',
       'California', 'Colorado', 'Connecticut', 'Delaware',
       'District of Columbia', 'Florida', 'Georgia', 'Hawaii', 'Idaho',
       'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana',
       'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota',
       'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada',
       'New Hampshire', 'New Jersey', 'New Mexico', 'New York',
       'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon',
       'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota',
       'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington',
       'West Virginia', 'Wisconsin', 'Wyoming'])]

df1_states["Abbrev"] = df1_states['GeoName'].apply(us_state_to_abbrev)

df1_regions = df1[df1['GeoName'].isin(['Wyoming', 'New England', 'Mideast',
       'Great Lakes', 'Plains', 'Southeast', 'Southwest',
       'Rocky Mountain', 'Far West'])]

     #
  


#site config
st.set_page_config(
    page_title="State Economic Comp",
    page_icon="",
    layout = "wide"
)



col0 = st.columns([1])[0]

# -- Create three columns of equal size
col1, col2, col3 = st.columns(3)

# column 0 header
with col0:
    st.header('State Economic Comps')
# column 1 pick a state for regression plot and real gdp data
with col1:
    st.write('Choose states to view.')
    
    #create a sorted list for user to choose from
    # state_list = sorted(df1_states['Abbrev'].unique())
    
    # #selection tool
    # selected_states = st.multiselect(
    #     "Select which states to compare.",
    #     state_list,
    #     )
        
    # #create dataframe of the seleted states
    # state_df = df1_states[df1_states['Abbrev'].isin(selected_states)].copy()
    
    # #create scatter plot for selected states
    # fig = px.scatter(
    #     state_df, x= "Real GDP", y= "Personal Income", opacity=0.65,
    #     trendline='ols', trendline_color_override='darkblue'
    # )
    
    # #change the background color of plot
    # fig.update_layout({
    #     'plot_bgcolor': 'rgba(0, 0, 0, 0)',
    #     'paper_bgcolor': 'rgba(0, 0, 0, 0)',
    #     })

    # # adds grid axes for better vizualization
    # fig.update_xaxes(showgrid=False, gridwidth=1, gridcolor='Gray')
    # fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='Gray')
    
    # # create stats from user selected states dataframe
    # # we can probably have the user pick what stats they want to see
    # summary_stats = state_df.groupby('Abbrev')['Real GDP'].agg(['mean', 'median', 'min', 'max', 'std'])
    
    # #print out the stats in index
    # summary_stats.index = summary_stats.index.rename('Real GDP Info')
    # st.write('Real GDP Info', summary_stats)
    
    # #fixes plot sizing
    # st.plotly_chart(fig, use_container_width=True)



map_type = st.multiselect(
        "Select the type of specialization required.",
        ['Real GDP', 'Real GDP per Capita', 'Population', 'Personal Income', 'Personal Income per Capita'])

map_var = ''.join(map_type) 



#start_time = st.select_slider('Years',  datetime.date(2011,1,1),datetime.date(2021,1,1))
start_time = st.select_slider("Date", options = np.unique(df1_nat["Date"]))
st.write(start_time)
df1_states_recent = df1_states[df1_states["Date"] == start_time]
if(map_var != "" ):
  fig = px.choropleth(df1_states_recent,
          locations="Abbrev",
          color= map_var,
          locationmode="USA-states",
          #range_color=(0,df1_states_recent[map_var].max()),
          range_color = (0, df1_states[map_var].max()),
          scope="usa")
  fig.update_geos(fitbounds="locations", visible=True)
  fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
  st.plotly_chart(fig, use_container_width=True)



# import streamlit as st
# import pandas as pd
# import numpy as np
# import plotly.express as px
# import seaborn as sns
# import datetime



# from sklearn.linear_model import LinearRegression, LogisticRegression
# from sklearn.ensemble import RandomForestRegressor

# from sklearn.model_selection import train_test_split

# from sklearn import metrics

# #abbrevation
# def us_state_to_abbrev(string):
#     us_state_to_abbrev = {
#         "Alabama": "AL",
#         "Alaska": "AK",
#         "Arizona": "AZ",
#         "Arkansas": "AR",
#         "California": "CA",
#         "Colorado": "CO",
#         "Connecticut": "CT",
#         "Delaware": "DE",
#         "Florida": "FL",
#         "Georgia": "GA",
#         "Hawaii": "HI",
#         "Idaho": "ID",
#         "Illinois": "IL",
#         "Indiana": "IN",
#         "Iowa": "IA",
#         "Kansas": "KS",
#         "Kentucky": "KY",
#         "Louisiana": "LA",
#         "Maine": "ME",
#         "Maryland": "MD",
#         "Massachusetts": "MA",
#         "Michigan": "MI",
#         "Minnesota": "MN",
#         "Mississippi": "MS",
#         "Missouri": "MO",
#         "Montana": "MT",
#         "Nebraska": "NE",
#         "Nevada": "NV",
#         "New Hampshire": "NH",
#         "New Jersey": "NJ",
#         "New Mexico": "NM",
#         "New York": "NY",
#         "North Carolina": "NC",
#         "North Dakota": "ND",
#         "Ohio": "OH",
#         "Oklahoma": "OK",
#         "Oregon": "OR",
#         "Pennsylvania": "PA",
#         "Rhode Island": "RI",
#         "South Carolina": "SC",
#         "South Dakota": "SD",
#         "Tennessee": "TN",
#         "Texas": "TX",
#         "Utah": "UT",
#         "Vermont": "VT",
#         "Virginia": "VA",
#         "Washington": "WA",
#         "West Virginia": "WV",
#         "Wisconsin": "WI",
#         "Wyoming": "WY",
#         "District of Columbia": "DC",
#         "American Samoa": "AS",
#         "Guam": "GU",
#         "Northern Mariana Islands": "MP",
#         "Puerto Rico": "PR",
#         "United States Minor Outlying Islands": "UM",
#         "U.S. Virgin Islands": "VI",
#         }
#     return us_state_to_abbrev[string]

# df1 = pd.read_csv("Master_DF.csv")


# df1_nat = df1[df1['GeoName'] == 'United States']
# df1_nat["Abrev"] = "US"

# df1_states = df1[df1['GeoName'].isin(['Alabama', 'Alaska', 'Arizona', 'Arkansas',
#        'California', 'Colorado', 'Connecticut', 'Delaware',
#        'District of Columbia', 'Florida', 'Georgia', 'Hawaii', 'Idaho',
#        'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana',
#        'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota',
#        'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada',
#        'New Hampshire', 'New Jersey', 'New Mexico', 'New York',
#        'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon',
#        'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota',
#        'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington',
#        'West Virginia', 'Wisconsin', 'Wyoming'])]

# df1_states["Abbrev"] = df1_states['GeoName'].apply(us_state_to_abbrev)

# df1_regions = df1[df1['GeoName'].isin(['Wyoming', 'New England', 'Mideast',
#        'Great Lakes', 'Plains', 'Southeast', 'Southwest',
#        'Rocky Mountain', 'Far West'])]
       
# #site config
# st.set_page_config(
#     page_title="State Economic Comp",
#     page_icon="📈",
#     layout = "wide"
# )

# #header column
# col0 = st.columns([1])[0]

# # column 0 header
# with col0:
#     st.header('Welcome to my economic dashboard!')


# # CHoro pleth map alternatint with input date 
# user_input = st.text_input( "Input text")
# st.write(user_input)
# start_time = st.slider('Years', 2010, 2021, 2010)
# df1_states_recent = df1_states[df1_states["Year"] == start_time]
# if(user_input != "" ):
#     fig = px.choropleth(df1_states_recent,
#                     locations="Abbrev",
#                     color= "Personal Income",
#                     locationmode="USA-states",
#                     range_color=(0,df1_states_recent["Personal Income"].max()),
#                     scope="usa")
#     fig.update_geos(fitbounds="locations", visible=False)
#     fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
#     st.plotly_chart(fig)

# st.dataframe(df1)

# # column 1 pick a state for regression plot and real gdp data
# st.write('Choose state to view.')
    
# #create a sorted list for user to choose from
# state_list = sorted(df1_states['Abbrev'].unique())
    
# #selection tool
# selected_states = st.multiselect(
#     "Select the state you want to see.",
#     state_list,
#     max_selections = 1
#     )

# df1_states['Date'] = pd.to_datetime(df1_states['Date'], format='%Y-%m-%d').dt.date
# #create dataframe of the seleted states
# state_df = df1_states[df1_states['Abbrev'].isin(selected_states)].copy()
# selected_cat = []
# #create a list of ecnomonic data to see
# cat_list = ['Real GDP', 'Personal Income', 'Population', 'Real GDP per Capita', 'Personal Income per Capita', 'Date']
# if(len(selected_states) == 1):
#     selected_cat = st.multiselect(
#         "Select what data you want to see.",
#         cat_list,
#         max_selections = 2,
#         )
# chart = ""
# if(len(selected_cat) == 2):
#     cat_1 = selected_cat[1]
#     cat_2 = selected_cat[0]
#     if(selected_cat.count('Date')):
#         chart = st.selectbox(
#             "Which plot do you want to see?",
#             ('None', 'Line'),
#         )
#     else:
#         chart = st.selectbox(
#             "Which plot do you want to see?",
#             ('None', 'Regression', 'Line'),
#         )
#     complete = True
# else:
#     complete = False

# created = False
# col1, col2 = st.columns(2)
# #create scatter plot for selected states
# if(complete):
#     with col1:
#         if (chart == 'Regression'):
#             fig = px.scatter(
#                 state_df, x= cat_1, y= cat_2, opacity=0.65,
#                 trendline='ols', trendline_color_override='darkblue'
#             )
#             col1.plotly_chart(fig)
#             created = True
#         elif (chart == 'Line'):
#             n_state_df = state_df.sort_values(by=cat_1)
#             fig = px.line(
#                 n_state_df, x= cat_1, y= cat_2,
#             )
#             col1.plotly_chart(fig)
#             created = True
#         else:
#             created = False
#     with col2:
#         # create stats from user selected states dataframe
#         summary_stats = state_df
#         st.write('Selected States Info')
#         st.dataframe(summary_stats)

# if(created):
#     # change the background color of plot
#     fig.update_layout({
#         'plot_bgcolor': 'rgba(0, 0, 0, 0)',
#         'paper_bgcolor': 'rgba(0, 0, 0, 0)',
#     })

#     # adds grid axes for better vizualization
#     fig.update_xaxes(showgrid=False, gridwidth=1, gridcolor='Gray')
#     fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='Gray')
#     #fixes plot sizing
#     #st.plotly_chart(fig, use_container_width=T
