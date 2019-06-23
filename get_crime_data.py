import pandas as pd
import numpy as np
import datetime
from sodapy import Socrata

def get_crime_data(city = 'SFO',
                   start_time = datetime.date.today() - datetime.timedelta(days = 7),
                   end_time = datetime.date.today()):
    
    if city == 'SFO':
        client_name = 'data.sfgov.org'
        api_endpoint = 'wg3w-h783'
        relevant_cols = 'analysis_neighborhood,incident_category,incident_code,incident_description,latitude,longitude,point,police_district,incident_datetime,report_datetime,report_type_code,report_type_description,resolution,supervisor_district'
        date_col = 'report_datetime'
    else:
        client_name = 'data.cityofchicago.org'
        api_endpoint = 'ijzp-q8t2'
        relevant_cols = 'arrest, beat, block,case_number,date,description,district,domestic,fbi_code,location_description,primary_type,ward'
        date_col = 'date'

    client = Socrata(client_name, None)
    
    where_query = date_col + ' between ' + "'"+str(start_time) + 'T00:00:00'+"'"+ ' and ' + "'"+str(end_time) + 'T00:00:00'+"'"
    
    results = client.get(dataset_identifier = api_endpoint, 
                     content_type = 'json',
                     where = where_query,
                     select = relevant_cols)
    # Convert to pandas DataFrame
    results_df = pd.DataFrame.from_records(results)

    return(results_df)