# Custom imports
from src.streamapps.multipage import MultiPage
from src.streamapps.stream_basicapp import showdataframe,pandasprofile, basic_info



# import your pages here

# Create an instance of the app
def app():
    local = MultiPage()

    local.add_page("ShowDAtaFrame", showdataframe.app)
    local.add_page("PandasProfiling Report", pandasprofile.app)
    local.add_page("Test Report", basic_info.app)




    # The main app
    local.run()