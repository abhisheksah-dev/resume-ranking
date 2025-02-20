# dummy_model.py
class DummyModel:
    def predict(self, X):
        # For each input text, return a dummy score (e.g., length modulo 100)
        return [len(text) % 100 for text in X]
