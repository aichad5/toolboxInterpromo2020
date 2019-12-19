import datetime


# Transform a date to standard format
def format_date(date):
    # Transform a string date into a standard format by trying each
    # date format. If you want to add a format, add a try/except in the
    # last except
    # date : str : the date to transform
    # return : m : timedata : format is YYYY-MM-DD HH:MM:SS
    date_str = date
    #
    date_str = date_str.replace("st","").replace("th","")\
        .replace("nd","").replace("rd","").replace(" Augu "," Aug ")
    m = None
    try:
        m = datetime.datetime.strptime(date_str, "%d %B %Y")
    except ValueError:
        try:
            m = datetime.datetime.strptime(date_str, "%d %b %Y")
        except ValueError:
            try:
                m = datetime.datetime.strptime(date_str, "%Y/%m/%d")
            except ValueError:
                try:
                    m = datetime.datetime\
                        .strptime(date_str,"%d/%m/%Y %H:%M:%S")
                except ValueError:
                    try:
                        m = datetime.datetime\
                            .strptime(date_str, "%Y-%m-%d %H:%M:%S")
                    except ValueError:
                        try :
                            m = datetime.datetime.strptime(date_str,
                                                       "%d %m %Y")
                        except ValueError:
                            # HERE ADD A FORMAT TO CHECK
                            print("Format not recognised. \nConsider "
                                  "adding a date format "
                                  "in the function \"format_date\".")

    return m
