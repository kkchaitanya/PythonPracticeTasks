from fastapi import FastAPI
import numpy as np

# 1. Initialize the FastAPI application
app = FastAPI()

## Numbers 1–50 ##
arr= np.arange(1,51)

@app.get("/numbers")
def read_root():
    return {'numbers':arr.tolist()}


@app.get("/mean")
def read_root():
    return {'mean':arr.mean()}

@app.get("/median")
def read_root():
    return {'median':np.median(arr)}

@app.get("/std")
def read_root():
    return {'std':arr.std()}

@app.get("/variance")
def read_root():
    return {'variance':arr.var()}

@app.get("/maximum")
def read_root():
    return {'max':int(np.max(arr))}

@app.get("/minimum")
def read_root():
    return {'min':int(np.min(arr))}

@app.get("/sum")
def read_root():
    return {'sum':int(arr.sum())}

@app.get("/even")
def read_root():
    return{'even': arr[arr%2==0].tolist()}

@app.get("/odd")
def read_root():
    return {'odd':arr[arr%2!=0].tolist()}

@app.get("/stats") 
def get_stats(): 
    return { "mean": float(np.mean(arr)), 
             "median": float(np.median(arr)),
             "standard_deviation": float(np.std(arr)),
             "variance": float(np.var(arr)),
              "maximum": int(np.max(arr)),
              "minimum": int(np.min(arr)) }

@app.get("/table/{number}") 
def multiplication_table(number: int): 
    multipliers = np.arange(1, 11) 
    table = number * multipliers 
    return { "number": number, 
            "table": table.tolist() }
