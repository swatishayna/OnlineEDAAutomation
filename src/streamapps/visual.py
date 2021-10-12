# Custom imports
from src.streamapps.multipage import MultiPage
from src.streamapps.stream_visualapps import Correlation_Graph,CorrelationHeatmap,Distribution_Graph



# import your pages here

# Create an instance of the app
def app():
    local = MultiPage()

    local.add_page("Correlation_Graph", Correlation_Graph.app)
    local.add_page("CorrelationHeatmap", CorrelationHeatmap.app)
    local.add_page("Distribution Report", Distribution_Graph.app)



    # The main app
    local.run()