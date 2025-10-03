#  Prédiction des Charges d'Assurance Maladie

Ce projet développe un **modèle de régression** capable de prédire avec haute précision les **charges médicales** que chaque assuré devra payer.  
L’objectif est de fournir une solution **rapide, fiable et accessible** pour aider les particuliers à **anticiper leurs dépenses de santé** et **mieux planifier leur budget**, tout en permettant à l’entreprise d’ajuster ses politiques tarifaires.

---

##  Contexte

En tant que **développeur IA junior** au sein d’une compagnie d’assurance santé, j’ai mis en place un système intelligent d’estimation des coûts médicaux à partir de données clients anonymisées.

### Données utilisées (`assurance_maladie.csv`)
Le jeu de données contient les variables suivantes :
- `Age` : âge de l’assuré  
- `Sex` : sexe (`male` / `female`)  
- `BMI` : indice de masse corporelle  
- `Children` : nombre d’enfants à charge  
- `Smoker` : fumeur ou non (`yes` / `no`)  
- `Region` : région géographique (`southeast`, `southwest`, `northeast`, `northwest`)  
- `Charges` : **variable cible** – coûts médicaux estimés (en dollars)

---

##  Feature Stories

Le projet a été structuré en 6 étapes clés :

1. **Analyse et Préparation des Données**  
   - Chargement, exploration (EDA), nettoyage (valeurs manquantes, doublons, outliers), encodage, normalisation, et division train/test.

2. **Entraînement de Modèles de Régression**  
   - Comparaison de 4 modèles : `LinearRegression`, `RandomForestRegressor`, `XGBRegressor`, `SVR`.

3. **Tuning des Hyperparamètres**  
   - Optimisation via `RandomizedSearchCV` (5 folds) pour Random Forest et XGBoost.

4. **Évaluation et Comparaison des Modèles**  
   - Visualisations (résidus, prédictions vs réelles), tableau comparatif des métriques (RMSE, MAE, R²).

5. **Test et Téléchargement du Modèle**  
   - Sauvegarde du modèle final (`joblib`), démonstration de prédiction interactive.

6. **Documentation et Reproductibilité**  
   - Code commenté, notebook auto-documenté, et ce fichier `README.md`.


