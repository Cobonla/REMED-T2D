import numpy as np
import os
import pickle

def model_prediction_5features(Ndata):
    name = list(Ndata.keys())
    features = list(Ndata.values())
    features = np.array(features)

    nprob_list = []

    MODEL_PATHS = [
        "./models/Data_5features/B1",
        "./models/Data_5features/B2",
        "./models/Data_5features/B3",
        "./models/Data_5features/B4",
        "./models/Data_5features/B5"
    ]

    for model_path in MODEL_PATHS:
        for model_file in os.listdir(model_path):
            if model_file.endswith('.pkl'):
                model = pickle.load(open(os.path.join(model_path, model_file), 'rb'))
                nprob_pred = model.predict_proba(features)
                nprob = nprob_pred[:, 1]
                nprob_list.append(nprob)

    #Print len nprob_list
    print(len(nprob_list))
    prob_average = np.mean(nprob_list, axis=0)
    threshold = 0.5
    predicted_outcome = np.where(prob_average >= threshold, 1, 0)
    
    prob_average, predicted_outcome = list(prob_average), list(predicted_outcome)

    results = {}
    for i in range(len(name)):
        results[name[i]] = [prob_average[i], predicted_outcome[i]]
    
    return results

def model_prediction_7features(Ndata):
    name = list(Ndata.keys())
    features = list(Ndata.values())
    features = np.array(features)

    nprob_list = []

    MODEL_PATHS = [
        "./models/Data_7features/B1",
        "./models/Data_7features/B2",
        "./models/Data_7features/B3",
        "./models/Data_7features/B4",
        "./models/Data_7features/B5"
    ]

    for model_path in MODEL_PATHS:
        for model_file in os.listdir(model_path):
            if model_file.endswith('.pkl'):
                model = pickle.load(open(os.path.join(model_path, model_file), 'rb'))
                nprob_pred = model.predict_proba(features)
                nprob = nprob_pred[:, 1]
                nprob_list.append(nprob)

    #Print len nprob_list
    print(len(nprob_list))
    prob_average = np.mean(nprob_list, axis=0)
    threshold = 0.5
    predicted_outcome = np.where(prob_average >= threshold, 1, 0)
    
    prob_average, predicted_outcome = list(prob_average), list(predicted_outcome)

    results = {}
    for i in range(len(name)):
        results[name[i]] = [prob_average[i], predicted_outcome[i]]
    
    return results
    
def model_prediction_8features(Ndata):
    name = list(Ndata.keys())
    features = list(Ndata.values())
    features = np.array(features)

    nprob_list = []

    MODEL_PATHS = [
        "./models/Data_8features/B1",
        "./models/Data_8features/B2",
        "./models/Data_8features/B3",
        "./models/Data_8features/B4",
        "./models/Data_8features/B5"
    ]

    for model_path in MODEL_PATHS:
        for model_file in os.listdir(model_path):
            if model_file.endswith('.pkl'):
                model = pickle.load(open(os.path.join(model_path, model_file), 'rb'))
                nprob_pred = model.predict_proba(features)
                nprob = nprob_pred[:, 1]
                nprob_list.append(nprob)

    #Print len nprob_list
    print(len(nprob_list))
    prob_average = np.mean(nprob_list, axis=0)
    threshold = 0.5
    predicted_outcome = np.where(prob_average >= threshold, 1, 0)
    
    prob_average, predicted_outcome = list(prob_average), list(predicted_outcome)

    results = {}
    for i in range(len(name)):
        results[name[i]] = [prob_average[i], predicted_outcome[i]]
    
    return results

if __name__ == "__main__":
    # F5_features     
    Ndata5 = {
        'Sample_1': [2, 106.2, 77, 26.63, 30],  
        'Sample_2': [1, 108, 92, 22.99, 21]   
    }

    # F7_features 
    Ndata7 = {
        'Sample_1': [5, 88.2, 106, 4.8, 169.9, 14.8, 50],  
        'Sample_2': [6, 73.8, 74, 7.5, 156.4, 24.9, 50]   
    }

    # F8_features 
    Ndata8 = {
        'Sample_1': [9, 156, 86, 28, 155, 34.3, 1.189, 42],  
        'Sample_2': [4, 136, 70, 29, 120, 31.2, 1.182, 22]   
    }

    results5 = model_prediction_5features(Ndata5)
    results7 = model_prediction_7features(Ndata7)
    results8 = model_prediction_8features(Ndata8)

    for sample_name, (prob, prediction) in results5.items():
        print(f"Sample: {sample_name}, Average Probability: {prob:.4f}, Predicted Outcome: {prediction}")
    
    for sample_name, (prob, prediction) in results7.items():
        print(f"Sample: {sample_name}, Average Probability: {prob:.4f}, Predicted Outcome: {prediction}")
    
    for sample_name, (prob, prediction) in results8.items():
        print(f"Sample: {sample_name}, Average Probability: {prob:.4f}, Predicted Outcome: {prediction}")

