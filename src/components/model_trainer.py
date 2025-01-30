import os
import sys
from dataclasses import dataclass

from src.exception import CustomException
from src.logger import logging

from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
from sklearn.metrics import f1_score

from src.utils import save_object, evaluate_models

@dataclass
class ModelTrainerConfig:
    trained_model_file_path=os.path.join('artifacts', 'model.pkl')

class ModelTrainer:
    def __init__(self):
        self.model_trainer_config=ModelTrainerConfig()
    
    def initiate_model_trainer(self, train_array, test_array):
        try:
            logging.info("Splitting train and test input data")
            X_train, y_train, X_test, y_test=(
                train_array[:, :-1], 
                train_array[:, -1],
                test_array[:, :-1],
                test_array[:, -1]
            )

            models = {
            "Logistic Regression": LogisticRegression(max_iter=1000),
            "SVC": SVC(),
            "RandomForestClassifier": RandomForestClassifier(),
            "XGBClassifier": XGBClassifier(objective="multi:softmax", num_class=6, random_state=42), 
            }

            params = {
                "Logistic Regression": {
                    'C': [0.1, 1, 10],  # Regularization strength. Smaller values apply stronger regularization.

                    'solver': ['lbfgs', 'liblinear'],  # Optimization algorithms. 
                },
                
                "SVC": {
                    'C': [0.1, 1, 10],  # Regularization strength. Larger values make the decision boundary more complex, smaller values create a smoother boundary.

                    'kernel': ['linear', 'rbf'],  # Types of kernels. 
                },

                "RandomForestClassifier": {
                    'n_estimators': [100, 200],  # Number of trees in the forest. More trees generally lead to better performance but increase computation time.

                    'max_depth': [None, 10, 20],  # Maximum depth of trees. 
                },

                "XGBClassifier": {
                    'n_estimators': [100, 200],  # Number of boosting rounds. More rounds improve performance but can lead to overfitting.

                    'learning_rate': [0.01, 0.1],  # Step size for each boosting round. 

                    'max_depth': [3, 6],  # Maximum depth of each tree. 
                }
            }

            
            model_report:dict=evaluate_models(X_train=X_train, y_train=y_train, X_test=X_test, y_test=y_test, models=models, params=params)

            # To get best model score from dict
            best_model_score = max(sorted(model_report.values()))
            print(best_model_score)

            # To get best model name from dict
            best_model_name=list(model_report.keys())[list(model_report.values()).index(best_model_score)]

            best_model=models[best_model_name]

            if best_model_score < 0.6:
                raise CustomException("No best model found")

            logging.info(f"Best found model on both training and testing dataset")

            save_object(
                file_path=self.model_trainer_config.trained_model_file_path,
                obj=best_model
            )

            predicted=best_model.predict(X_test)

            F1_score = f1_score(y_test, predicted, average='weighted')
            return F1_score
            
        except Exception as e:
            raise CustomException(e,sys)