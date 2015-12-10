""""
************************************************************
*** Earthquake stat in Myanmar that affect Thailand 2004-2014. ****
***                 Create Graph by module "plotly"                ****
************************************************************
"""
import plotly.plotly as py
from plotly.graph_objs import *

#Login Plotly by using account username and api_key of plotly for open graph on browser.
py.sign_in('bbellkungdesu', 'b3ngpu9r4g')

#Pull data from Database for bring create graph.
data = Data([
    Scatter(
        x=['2004-12-26', '2004-12-30', '2005-09-18', '2006-01-24', '2006-09-27', '2006-09-28', '2006-09-28', '2006-10-08', '2007-05-15', '2007-05-16', '2007-06-23', '2007-11-02', '2008-08-21', '2008-09-22', '2010-03-20', '2010-07-06', '2011-02-04', '2011-03-24', '2011-05-10', '2012-11-11', '2012-11-11', '2012-12-20', '2013-02-07', '2013-04-11', '2013-05-07', '2015-05-24'],
        y=[6.4, 5.5, 6, 5.7, 4.8, 4.8, 5, 5.6, 5.1, 6.1, 5.35, 5.7, 5.7, 5.2, 5, 4.5, 6.8, 6.7, 4, 6.6, 5.8, 4.6, 4.3, 5.1, 5.4, 5.1],
        mode='lines+markers',
        name='M/I',
        text=['Myanmar ', 'Myanmar ', 'Myanmar-India Border', 'Chan, Myanmar ', 'Myanmar ', 'Myanmar ', 'Myanmar ', 'Myanmar ', 'Laos - Myanmar Border', 'Laos - Myanmar Border ', 'Myanmar ', 'Myanmar - Laos - China Border', 'Myanmar - China Border', 'Myanmar', 'Myanmar', 'Myanmar ', 'Myanmar-India Border ', 'Myanmar ', 'Myanmar ', 'Myanmar', 'Myanmar', 'Myanmar', 'Myanmar', 'Myanmar', 'Myanmar', 'Myanmar'],
        uid='7de5d6'
    )
])

#define layout and scope of graph.
layout = Layout(
    annotations=Annotations([
        Annotation(
            x=1419614831752.236,
            y=6.762837056737828,
            font=Font(
                size=18
            ),
            showarrow=False,
            text='Average : 5.42'
        ),
        Annotation(
            x=1294813761674.7356,
            y=6.848228510491848,
            ax=-46,
            ay=-28,
            font=Font(
                size=14
            ),
            text='Maximum : 6.8'
        ),
        Annotation(
            x=1306500818404.4011,
            y=3.9876148097322,
            ax=35,
            ay=30,
            font=Font(
                size=14
            ),
            text='Minimum : 4'
        )
    ]),
    autosize=True,
    height=536,
    hovermode='x',
    title='Earthquake stat in Myanmar that affect Thailand 2004-2014',
    width=1121,
    xaxis=XAxis(
        autorange=False,
        range=[1079229304500.7252, 1480345787258.177],
        title='DATE',
        type='date'
    ),
    yaxis=YAxis(
        autorange=False,
        range=[3.4005485651733167, 7.200468257227177],
        title='M/I',
        type='linear'
    )
)

#Plot graph.
fig = Figure(data=data, layout=layout)
#Open graph on any browser.
plot_url = py.plot(fig)
