# Custom imports
from src.streamapps.multipage import MultiPage
from src.streamapps.stream_advancedapp import CorrelationMatrix, columwisereport,get_count_value,get_quantile_stats,get_missing_value,get_crosstab,get_groups

# import your pages here

# Create an instance of the app
def app():
    local = MultiPage()

    # local.add_page("ShowAdvancedInfo", advanced_info.app)
    local.add_page("Missing value", get_missing_value.app)
    local.add_page("Quantile statistics", get_quantile_stats.app)
    local.add_page("Count value", get_count_value.app)
    local.add_page("Crosstab", get_crosstab.app)
    local.add_page("Groups", get_groups.app)
    local.add_page("Show Column Report", columwisereport.app)
    local.add_page("Correlation", CorrelationMatrix.app)
    local.run()