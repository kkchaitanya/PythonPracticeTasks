from flask import Flask, jsonify
import numpy as np

# 1. Initialize the Flask application
app = Flask(__name__)

## Numbers 1–50 ##
arr = np.arange(1, 51)

@app.get("/numbers")
def get_numbers():
    return {'numbers': arr.tolist()}

@app.get("/mean")
def get_mean():
    return {'mean': arr.mean()}

@app.get("/median")
def get_median():
    return {'median': np.median(arr)}

@app.get("/std")
def get_std():
    return {'std': arr.std()}

@app.get("/variance")
def get_variance():
    return {'variance': arr.var()}

@app.get("/maximum")
def get_maximum():
    return {'max': int(np.max(arr))}

@app.get("/minimum")
def get_minimum():
    return {'min': int(np.min(arr))}

@app.get("/sum")
def get_sum():
    return {'sum': int(arr.sum())}

@app.get("/even")
def get_even():
    return {'even': arr[arr % 2 == 0].tolist()}

@app.get("/odd")
def get_odd():
    return {'odd': arr[arr % 2 != 0].tolist()}

@app.get("/stats") 
def get_stats(): 
    return { 
        "mean": float(np.mean(arr)), 
        "median": float(np.median(arr)),
        "standard_deviation": float(np.std(arr)),
        "variance": float(np.var(arr)),
        "maximum": int(np.max(arr)),
        "minimum": int(np.min(arr)) 
    }

# Flask path parameter syntax: <type:variable_name>
@app.get("/table/<int:number>") 
def multiplication_table(number): 
    multipliers = np.arange(1, 11) 
    table = number * multipliers 
    return { 
        "number": number, 
        "table": table.tolist() 
    }

if __name__ == '__main__':
    app.run(debug=True)
