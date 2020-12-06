import pandas as pd
import pickle

def process_data(json_data):
    try:
        # Transform data to dictionary
        dict_data = pd.DataFrame.from_dict(json_data)
        # Load model
        model = pickle.load(open('final_model.pkl', 'rb'))
        features = ['bedrooms','bathrooms','sqft_living','sqft_lot','floors','waterfront','view',
                'condition','grade','sqft_above','sqft_basement','yr_built','yr_renovated',
                'zipcode','lat','long','sqft_living15','sqft_lot15']
        # Predict price
        x_pred = model.predict(dict_data[features])[0]
        
        retval = {
            'status': 200,
            'message': 'predicting price succeed',
            'result': {
                'price': 'USD ' + str(round(x_pred,3)),
                'house_details': json_data,
            }
        }
        return retval
    except KeyError as e:
        retval = {
            'status': 400,
            'message': str(e),
            'result': None,
        }
        return retval
    except Exception as e:
        retval = {
            'status': 500,
            'message': str(e),
            'result': None,
        }