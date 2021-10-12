# Custom imports
from src.streamapps.multipage import MultiPage
from src.streamapps.stream_advancedapp import columwisereport,CorrelationMAtrix



# import your pages here

# Create an instance of the app
def app():
    local = MultiPage()

    local.add_page("Show Column Report", columwisereport.app)
    local.add_page("PandasProfiling Report", CorrelationMAtrix.app)
    local.run()