import pandas as pd
import numpy as np

def blight_model():
    
    # Your code here
    
    return # Your answer here

df_train = pd.read_csv('train.csv', encoding = "ISO-8859-1")
df_test = pd.read_csv('test.csv', encoding = "ISO-8859-1")

df_train.columns

list_to_remove = ['balance_due',
 'collection_status',
 'compliance_detail',
 'payment_amount',
 'payment_date',
 'payment_status']

list_to_remove_all = ['violator_name', 'zip_code', 'country', 'city',
                      'inspector_name', 'violation_street_number', 'violation_street_name',
                      'violation_zip_code', 'violation_description',
                      'mailing_address_str_number', 'mailing_address_str_name',
                      'non_us_str_code',
                      'ticket_issued_date', 'hearing_date']


df_train.drop(list_to_remove, axis=1, inplace=True)
df_train.drop(list_to_remove_all, axis=1, inplace=True)
df_test.drop(list_to_remove_all, axis=1, inplace=True)

df_train.drop('grafitti_status', axis=1, inplace=True)
df_test.drop('grafitti_status', axis=1, inplace=True)

df_latlons = pd.read_csv('latlons.csv')

df_address =  pd.read_csv('addresses.csv')

df_id_latlons = df_address.set_index('address').join(df_latlons.set_index('address'))

df_train = df_train.set_index('ticket_id').join(df_id_latlons.set_index('ticket_id'))
df_test = df_test.set_index('ticket_id').join(df_id_latlons.set_index('ticket_id'))

vio_code_freq10 = df_train.violation_code.value_counts().index[0:10]

df_train['violation_code_freq10'] = [list(vio_code_freq10).index(c) if c in vio_code_freq10 else -1 for c in df_train.violation_code ]

# drop violation code

df_train.drop('violation_code', axis=1, inplace=True)

df_test['violation_code_freq10'] = [list(vio_code_freq10).index(c) if c in vio_code_freq10 else -1 for c in df_test.violation_code ]
df_test.drop('violation_code', axis=1, inplace=True)

#df_train.grafitti_status.fillna('None', inplace=True)
#df_test.grafitti_status.fillna('None', inplace=True)

df_train = df_train[df_train.compliance.isnull() == False]

df_train.lat.fillna(method='pad', inplace=True)
df_train.lon.fillna(method='pad', inplace=True)
df_train.state.fillna(method='pad', inplace=True)

df_test.lat.fillna(method='pad', inplace=True)
df_test.lon.fillna(method='pad', inplace=True)
df_test.state.fillna(method='pad', inplace=True)




# So remove city and states...

one_hot_encode_columns = ['agency_name', 'state', 'disposition']

df_train = pd.get_dummies(df_train, columns=one_hot_encode_columns)
df_test = pd.get_dummies(df_test, columns=one_hot_encode_columns)


from sklearn.model_selection import train_test_split
train_features = df_train.columns.drop('compliance')

X_data, X_keep, y_data, y_keep = train_test_split(df_train[train_features], 
                                                    df_train.compliance, 
                                                    random_state=0,
                                                    test_size=0.05)

print(X_data.shape, X_keep.shape)


X_train, X_test, y_train, y_test = train_test_split(X_data[train_features], 
                                                    y_data, 
                                                    random_state=0,
                                                    test_size=0.2)


print(X_train.shape, X_test.shape)                                                                                          





