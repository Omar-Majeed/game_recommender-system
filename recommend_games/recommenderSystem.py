import joblib
import pandas as pd
import os

# Get the absolute path to the current directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Load the model and the data
model = joblib.load(os.path.join(BASE_DIR, 'model/knn_model.pkl'))
df = joblib.load(os.path.join(BASE_DIR, 'model/df_data.pkl'))
df_game_name = joblib.load(os.path.join(BASE_DIR, 'model/df_game_name.pkl'))
# Function to get game recommendations
def GameRecommended(gamename: str, recommended_games: int = 6):
    distances, neighbors = model.kneighbors(df.loc[[gamename]], n_neighbors=recommended_games)
    similar_game = []
    similar_distance = []
    for i in range(1, len(neighbors[0])):
        similar_game.append(df_game_name.loc[neighbors[0][i], 'Game'])
        similar_distance.append(f"{round(100 - distances[0][i], 2)}%")
    return pd.DataFrame(data={"Game": similar_game, "Similarity": similar_distance})