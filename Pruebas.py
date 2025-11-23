#Solo prubeas: 
import pickle

with open("grafo_libros.pkl", "rb") as f:
    data = pickle.load(f)

print(data)
print(type(data))