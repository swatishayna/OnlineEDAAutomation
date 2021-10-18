# We can delete delete this
# do not work in this because omkar said we dont need multipageapp for upload_data.... check app.py and stream_uploadapp










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