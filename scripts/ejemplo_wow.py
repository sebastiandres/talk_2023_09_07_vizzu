def make_chart(width=800, height=600):
    import pandas as pd
    from ipyvizzu import Chart, Data, Config, Style, DisplayTarget
    
    df = pd.read_csv(
        "https://ipyvizzu.vizzuhq.com/0.16/showcases/musicformats/musicformats.csv",
        dtype={"Year": str},
    )
    data = Data()
    data.add_df(df)
    
    config = {
        "channels": {
            "y": {
                "set": ["Format"],
            },
            "x": {"set": ["Revenue [m$]"]},
            "label": {"set": ["Revenue [m$]"]},
            "color": {"set": ["Format"]},
        },
        "sort": "byValue",
    }
     
    style = Style(
        {
            "plot": {
                "paddingLeft": 100,
                "paddingTop": 25,
                "yAxis": {
                    "color": "#ffffff00",
                    "label": {"paddingRight": 10},
                },
                "xAxis": {
                    "title": {"color": "#ffffff00"},
                    "label": {
                        "color": "#ffffff00",
                        "numberFormat": "grouped",
                    },
                },
                "marker": {
                    "colorPalette": "#b74c20FF #c47f58FF #1c9761FF"
                    + " #ea4549FF #875792FF #3562b6FF"
                    + " #ee7c34FF #efae3aFF"
                },
            },
            "title": {
                "fontSize": 20,
            }
        }
    )
     
    chart = Chart(width=width, height=height, display=DisplayTarget.MANUAL)
    #chart = Chart(display=DisplayTarget.MANUAL)
     
    chart.animate(data, style)
     
    for year in range(1973, 2021):
        config["title"] = f"Ingresos anuales de la industria musical en EEU según formato - {year}"
        chart.animate(
            Data.filter(f"parseInt(record.Year) == {year}"),
            Config(config),
            duration=0.2,
            x={"easing": "linear", "delay": 0},
            y={"delay": 0},
            show={"delay": 0},
            hide={"delay": 0},
            title={"duration": 0, "delay": 0},
        )
     
    chart.animate(
        Config(
            {
                "channels": {
                    "x": {"attach": ["Year"]},
                    "label": {"set": None},
                }
            }
        ),
        duration=0.3,
    )
     
    chart.animate(
        Data.filter("record.Year == '2020' || record.Year == '1972'"),
        Config({"title": "Veamos el total de los últimos 47 años"}),
        duration=2,
    )
     
    chart.animate(Config({"sort": "none"}), delay=0, duration=2)
     
    for year in reversed(range(1973, 2020)):
        chart.animate(
            Data.filter(
                f"parseInt(record.Year) >= {year} || record.Year == '1972'"
            ),
            Config({"split": True}),
            Style({"plot.xAxis.interlacing.color": "#ffffff"}),
            duration=0.005,
        )
     
    chart.animate(
        Data.filter("record.Year != '1972'"),
        Config({"split": False}),
        duration=1.5,
    )
     
    chart.animate(
        Config({"channels": {"x": {"detach": ["Year"]}}}), duration=0
    )
     
    chart.animate(
        Config({"channels": {"label": {"set": ["Revenue [m$]"]}}}),
        duration=0.1,
    )
     
    chart.animate(
        Config(
            {
                "channels": {
                    "x": {"attach": ["Year"]},
                    "label": {"detach": ["Revenue [m$]"]},
                }
            }
        ),
        duration=1,
    )
     
    chart.animate(
        Config(
            {
                "channels": {
                    "x": {"set": ["Year"]},
                    "y": {
                        "set": ["Revenue [m$]", "Format"],
                        "range": {"min": None, "max": None},
                    },
                    "color": {"set": ["Format"]},
                },
                "title": "Ingresos industria musical en EEU según formato 1973 - 2020",
                "split": True,
            }
        ),
        Style(
            {
                "plot": {
                    "paddingLeft": 7.5,
                    "paddingTop": 25,
                    "xAxis": {
                        "label": {
                            "fontSize": 9,
                            "angle": 2.0,
                            "color": "#8e8e8e",
                        }
                    },
                    "yAxis": {
                        "interlacing": {"color": "#ffffff00"},
                        "title": {"color": "#ffffff00"},
                        "label": {"color": "#ffffff00"},
                    },
                }
            }
        ),
        duration=2,
    )
     
    chart.animate(Config({"geometry": "area"}), duration=1)
     
    chart.animate(
        Config(
            {
                "channels": {
                    "x": {"set": ["Year"]},
                    "y": {"range": {"max": "110%"}},
                },
                #"align": "center",
                "split": False,
            }
        ),
        Style({"plot.marker.borderWidth": 1}),
        duration=1,
    )
    return chart