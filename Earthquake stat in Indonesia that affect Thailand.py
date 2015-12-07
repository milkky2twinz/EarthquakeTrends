import plotly.plotly as py
from plotly.graph_objs import *
py.sign_in('milkky2twinz', 'jl493198bg')
data = Data([
    Scatter(
        x=['2004-12-26', '2005-02-09', '2005-03-28', '2005-04-10', '2005-05-14', '2005-05-19', '2005-05-22', '2005-07-05', '2005-09-07', '2005-10-11', '2005-11-19', '2006-12-01', '2007-04-27', '2007-09-12', '2007-09-13', '2007-12-28', '2008-02-20', '2009-09-30', '2010-04-07', '2010-05-09', '2011-09-06', '2012-03-05', '2012-04-11', '2012-06-23', '2013-07-02'],
        y=[8, 5.8, 8.5, 6.7, 6.5, 6.8, 6.1, 6.8, 5, 6.2, 6.1, 6.5, 6.1, 8.4, 7.1, 5.7, 7.5, 7.9, 7.6, 7.3, 6.7, 5.2, 8.6, 6.3, 6],
        mode='lines+markers',
        name='M/I',
        text=['Sumatra, Indonesia ', 'Sumatra, Indonesia ', 'Sumatra, Indonesia ', 'Sumatra, Indonesia', 'Sumatra, Indonesia ', 'Sumatra, Indonesia ', 'Sumatra, Indonesia ', 'Sumatra, Indonesia ', 'Sumatra, Indonesia ', 'Sumatra, Indonesia ', 'Sumatra, Indonesia ', 'Sumatra, Indonesia ', 'Sumatra, Indonesia', 'Sumatra, Indonesia', 'Sumatra, Indonesia', 'Sumatra, Indonesia', 'Sumatra, Indonesia ', 'Sumatra, Indonesia', 'Sumatra, Indonesia ', 'Sumatra, Indonesia', 'Sumatra, Indonesia ', 'Sumatra, Indonesia ', 'Sumatra, Indonesia', 'Sumatra, Indonesia', 'Sumatra, Indonesia'],
        uid='5e37c4'
    )
])
layout = Layout(
    annotations=Annotations([
        Annotation(
            x=1363703592722.1833,
            y=8.3071907957814,
            arrowsize=0.29999999999999993,
            font=Font(
                size=18
            ),
            showarrow=False,
            text='Average : 6.78'
        ),
        Annotation(
            x=1330483830650.8047,
            y=8.537296260786194,
            ax=-56,
            ay=24,
            font=Font(
                size=14
            ),
            showarrow=True,
            text='Maximum : 8.6'
        ),
        Annotation(
            x=1128658106368.0896,
            y=5.016682646212847,
            ax=56,
            ay=-42,
            font=Font(
                size=14
            ),
            showarrow=True,
            text='Minimum :5'
        )
    ]),
    autosize=True,
    height=536,
    title='Earthquake stat in Indonesia that affect Thailand 2004-2014',
    width=1121,
    xaxis=XAxis(
        autorange=False,
        range=[1088606673594.9557, 1389778290110.0007],
        title='DATE',
        type='date'
    ),
    yaxis=YAxis(
        autorange=False,
        range=[4.752061361457336, 8.847938638542663],
        title='M/I',
        type='linear'
    )
)
fig = Figure(data=data, layout=layout)
plot_url = py.plot(fig)
