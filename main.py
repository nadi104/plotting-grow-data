import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


# print(df)
def filterdata(olddf):
    # The following use to filter the dataframe
    # https://www.listendata.com/2019/07/how-to-filter-pandas-dataframe.html
    """Filter sensor dataset and get Longitude and Latitude details"""
    dflat = olddf[(olddf.Longitude >= 50.681) & (olddf.Longitude <= 57.985)]
    dflon = dflat[(dflat.Latitude >= -10.592) & (dflat.Latitude <= 1.6848)]
    dfAllsensor = dflon[["Latitude", "Longitude", "Type"]]

    # Each location has six sensors. For remove the location duplication use one type of sensor data
    # Remove the duplicate location
    dfAir = dfAllsensor[dfAllsensor.Type == "Thingful.Connectors.GROWSensors.AirTemperature"]
    dfAirFinal = dfAir[["Latitude", "Longitude"]]
    return dfAirFinal

def loadmap(newdf):
    # Following link code at the stackoverflow is used to draw the map and the plot
    # https://stackoverflow.com/questions/61942985/animate-a-plot-over-an-image-in-python
    """Load the UK map and load data on it"""
    BBox = ((newdf.Latitude.min() - 2, newdf.Latitude.max(),
             newdf.Longitude.min(), newdf.Longitude.max() + 1))
    # read the image in, plot points over image
    plotmap = "map7.png"
    truthplot = plt.imread(plotmap)
    fig, ax = plt.subplots(figsize=(8, 8), linewidth=0.1)
    plottitle = "Plotting Grow Data"
    ax.set_title(plottitle)
    ax.set_xlabel("Latitude")
    ax.set_ylabel("Longitude")
    ax.set_xlim(BBox[0], BBox[1])
    ax.set_ylim(BBox[2], BBox[3])

    scat = ax.scatter(newdf.Latitude, newdf.Longitude, zorder=1, c="b", alpha=0.5, s=50)

    ax.imshow(truthplot, zorder=0, extent=BBox, aspect='equal')
    plt.show()


df = pd.read_csv('GrowLocations.csv')
newdf = filterdata(df)
print(newdf)
loadmap(newdf)
