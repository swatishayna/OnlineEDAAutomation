# Custom imports
from src.streamapps.multipage import MultiPage
from src.streamapps.stream_uploadapp import upload_data



# import your pages here

# Create an instance of the app
def app():
    local = MultiPage()

    local.add_page("UploadData", upload_data.app)





    # The main app
    local.run()