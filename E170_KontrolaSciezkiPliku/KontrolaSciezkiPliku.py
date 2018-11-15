import os
import datetime

data_input_catalog = r'c:\temp\data_input'

data_output_catalog = r'c:\temp\data_output'

today = datetime.date.today()

today_output_catalog = os.path.join(data_output_catalog, today.strftime('%Y-%m-%d'))

is_input_catalog_ok = os.path.isdir(data_input_catalog)
is_output_catalog_ok = os.path.isdir(data_output_catalog)
is_today_output_catalog_ok = not os.path.isdir(today_output_catalog)\
                             and not os.path.isfile(today_output_catalog)

if (is_input_catalog_ok and is_output_catalog_ok and is_today_output_catalog_ok):

    print('Conditions met! We can continue!')

else:

    print('The following errors appeared:')

    if not is_input_catalog_ok:
        
        print('Input catalog does not exists!')      

    if not is_output_catalog_ok:

        print('Output catalog does not exists!')

    if not is_today_output_catalog_ok:

        print('Today catalog/file exists!')



