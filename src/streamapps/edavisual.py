# Custom imports
from src.streamapps.multipage import MultiPage
from src.streamapps.stream_visualapps import Distribution_Graph,boxplot, linechart, piechart,barplot, Meshplot,scatterchart,surfaceplot,scatterplot
from src.streamapps.stream_advancedapp import CorrelationMatrix


# import your pages here

# Create an instance of the app
def app():
    local = MultiPage()

    local.add_page("2D - Correlation Report", CorrelationMatrix.app)
    local.add_page("2D - Distribution Report", Distribution_Graph.app)
    local.add_page("2D - Boxplot Report", boxplot.app)
    local.add_page("2D - LineChart Report", linechart.app)
    local.add_page("2D - PieChart Report", piechart.app)
    local.add_page("2D - ScatterPlot Report", scatterplot.app)
    local.add_page("2D - BarPlot Report", barplot.app)
    #######################################################
    local.add_page("3D - ScatterChart Report", scatterchart.app)
    local.add_page("3D - MeshPlot Report", Meshplot.app)
    local.add_page("3D - SurfacePlot Report", surfaceplot.app)



    # The main app
    local.run()