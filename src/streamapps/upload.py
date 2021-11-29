# Custom imports
from src.streamapps.multipage import MultiPage
from src.streamapps.stream_projapp import upload_data, viewproject



# import your pages here

# Create an instance of the app
def app():
    local = MultiPage()

    local.add_page("Add Project",  upload_data.app)
    local.add_page("View Project", viewproject.app)






    # The main app
    local.run()