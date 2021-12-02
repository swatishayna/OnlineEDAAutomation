                                                                                EDAAutomation
                                              ========================================================================================

                                                                            Automated EDA Project


Link to the deployed app: https://flasklogineda.herokuapp.com/
Application video Demo: https://youtu.be/Cnqi35boTe8
LinkedIn Post : https://www.linkedin.com/in/swati-968834130/recent-activity/


 
The initial and the most crucial part of any model building is making the data set ready for next step.   Howsoever it consumes 70-80% of the time which can be reduced. An initial knowledge of the data is very much required to go for advanced data mining. This work discusses the implementation of unmanned basic exploration of the data in order to reduce the time of the scientist so they can work on other important part of the work. And this work also explains the behind implementation of data mining and can be very much useful for new data analytics.

The solution proposed here is an Automated EDA which can be implemented to perform above mentioned use cases. Initially the Automated EDA will take the dataset from the client , will process the dataset into Dataframe and on this processed DataFrame further operations will be performed. The choice of operations are fairly dependent on the user and the copy of the performed operations will be made available to the client on the provided email.
To create an automated exploration of data at the initial stage will make following processes faster:
To reduce coding so the exploration of the data can be made possible for management
To reduce time involved in basic exploration of data set and data mining
To demonstrate the working of exploring data to the data science enthusiast
To make the code readily available to the data scientists

This project can perform basic to advanced to visual analysis on the data set without writing any code.

Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io


--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
