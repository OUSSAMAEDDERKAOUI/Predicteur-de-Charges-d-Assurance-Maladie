import joblib
import pandas as pd
import numpy as np

modele_charge = joblib.load("./models/modele_final.pkl")

age = int(input("Entrez l'âge : "))
sex = input("Entrez le sexe (male/female) : ")
bmi = float(input("Entrez le BMI : "))
children = int(input("Nombre d'enfants : "))
smoker = input("Fumeur ? (yes/no) : ")
region = input("Région (northwest/northeast/southeast/southwest) : ")

nouvelle_donnee = pd.DataFrame([{
    "age": age,
    "sex": sex,
    "bmi": bmi,
    "children": children,
    "smoker": smoker,
    "region": region
}])



pred_log = modele_charge.predict(nouvelle_donnee)
pred = np.expm1(pred_log)

print(f"Estimation des charges : {pred[0]:.2f} $")
