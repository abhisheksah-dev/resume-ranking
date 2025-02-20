# train_model.py
import pickle
from dummy_model import DummyModel  # Import DummyModel from dummy_model.py

dummy_model = DummyModel()

# Save the model to model.pkl
with open("model.pkl", "wb") as f:
    pickle.dump(dummy_model, f)

print("Dummy model has been saved to model.pkl")
