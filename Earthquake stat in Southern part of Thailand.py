import plotly.plotly as py
from plotly.graph_objs import *
py.sign_in('bbeammor', 'wtjo8fd6hu')
data = Data([
    Scatter(
        x=['2004-09-17', '2004-12-27', '2008-12-23', '2011-04-30', '2011-06-24', '2012-02-20', '2012-04-16', '2012-06-04', '2015-02-20', '2015-03-25', '2015-05-06', '2015-05-07'],
        y=[5.8, 6.6, 4.1, 4.4, 3.5, 2.7, 4.3, 4, 4, 3.8, 4.6, 4.5],
        name='M/I',
        text=['Andaman Sea ', 'Andaman Sea ', 'Phrasaeng, Surat Thani ', 'Andaman Sea ', 'Hat Samran, Trang', 'Takua Pa, Phangnga', 'Thalang, Phuket', 'Mueang Ranong, Ranong', 'Ko Yao, Phangnga', 'Phuket', 'Ko Yao, Phangnga', 'Ko Yao, Phangnga'],
        uid='178361'
    )
])
layout = Layout(
    annotations=Annotations([
        Annotation(
            x=1413045086913.9258,
            y=6.307718120805369,
            font=Font(
                size=18
            ),
            showarrow=False,
            text='Average : 4.34'
        ),
        Annotation(
            x=1103847158292.5122,
            y=6.656711409395973,
            ax=49,
            ay=-30,
            font=Font(
                size=14
            ),
            text='Maximum : 6.6'
        ),
        Annotation(
            x=1334375740517.8447,
            y=2.679065018997905,
            ax=75,
            ay=-30,
            font=Font(
                size=14
            ),
            text='Minimum : 2.7'
        )
    ]),
    autosize=True,
    height=536,
    title='Earthquake stat in Southern part of Thailand',
    width=1121,
    xaxis=XAxis(
        autorange=True,
        range=[1075080009237.2289, 1451205590762.7712],
        title='DATE',
        type='date'
    ),
    yaxis=YAxis(
        autorange=True,
        range=[2.4089362318740974, 7.217228642677874],
        title='M/I',
        type='linear'
    )
)
fig = Figure(data=data, layout=layout)
plot_url = py.plot(fig)