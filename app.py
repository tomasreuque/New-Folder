from fastapi import FastAPI, HTTPException
from sympy import symbols, sympify, Eq, solve, lambdify, diff
import matplotlib.pyplot as plt
import numpy as np
from fastapi.responses import FileResponse
import os

app = FastAPI()

# Define la ubicación donde se guardarán las imágenes
IMAGE_FOLDER = "static"

@app.post("/calculate/")
async def calculate(expression: str, x_range: str):
    try:
        # Parse la expresión matemática
        x = symbols('x')
        expr = sympify(expression)

        # Parse el rango de valores de x
        x_start, x_end = map(float, x_range.split(","))

        # Crear una función lambda a partir de la expresión
        func = lambdify(x, expr, 'numpy')

        # Generar valores para x
        x_values = np.linspace(x_start, x_end, 100)
        y_values = func(x_values)

        # Graficar la función
        plt.figure(figsize=(8, 6))
        plt.plot(x_values, y_values, label=f'y = {expression}')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.legend()
        plt.grid(True)

        # Guardar la gráfica en un archivo
        graph_file = os.path.join(IMAGE_FOLDER, 'plot.png')
        plt.savefig(graph_file)

        # Devolver la gráfica como un archivo descargable
        return FileResponse(graph_file, headers={"Content-Disposition": "attachment; filename=plot.png"})
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/calculate/roots/")
async def calculate_roots(expression: str):
    try:
        # Parse la expresión matemática
        x = symbols('x')
        expr = sympify(expression)

        # Encuentra las raíces de la expresión
        equation = Eq(expr, 0)
        roots = solve(equation, x)

        # Crear una función lambda a partir de la expresión
        func = lambdify(x, expr, 'numpy')

        # Generar valores para x
        x_values = np.linspace(-10, 10, 400)
        y_values = func(x_values)

        # Graficar la función
        plt.figure(figsize=(8, 6))
        plt.plot(x_values, y_values, label=f'y = {expression}')
        
        # Resaltar las raíces en el gráfico
        for root in roots:
            plt.scatter(root, 0, color='red', marker='o', label=f'Root x={root}')

        plt.xlabel('x')
        plt.ylabel('y')
        plt.legend()
        plt.grid(True)

        # Guardar la gráfica en un archivo
        graph_file = os.path.join(IMAGE_FOLDER, 'plot.png')
        plt.savefig(graph_file)

        # Devolver la gráfica como un archivo descargable
        return FileResponse(graph_file, headers={"Content-Disposition": "attachment; filename=plot.png"})
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/calculate/roots_and_growth/")
async def calculate_roots_and_growth(expression: str):
    try:
        # Parse la expresión matemática
        x = symbols('x')
        expr = sympify(expression)

        # Encuentra las raíces de la expresión
        equation = Eq(expr, 0)
        roots = solve(equation, x)

        # Crear una función lambda a partir de la expresión
        func = lambdify(x, expr, 'numpy')
        # Crear una función lambda para la derivada
        deriv = lambdify(x, diff(expr, x), 'numpy')

        # Generar valores para x
        x_values = np.linspace(-10, 10, 400)
        y_values = func(x_values)
        derivative_values = deriv(x_values)

        # Graficar la función
        plt.figure(figsize=(8, 6))
        plt.plot(x_values, y_values, label=f'y = {expression}')
        
        # Sombrea las regiones crecientes y decrecientes
        increasing = derivative_values > 0
        decreasing = derivative_values < 0
        plt.fill_between(x_values, y_values, color='green', alpha=0.3, where=increasing)
        plt.fill_between(x_values, y_values, color='red', alpha=0.3, where=decreasing)

        # Resaltar las raíces en el gráfico
        for root in roots:
            plt.scatter(root, 0, color='blue', marker='o', label=f'Root x={root}')

        plt.xlabel('x')
        plt.ylabel('y')
        plt.legend()
        plt.grid(True)

        # Guardar la gráfica en un archivo
        graph_file = os.path.join(IMAGE_FOLDER, 'plot.png')
        plt.savefig(graph_file)

        # Devolver la gráfica como un archivo descargable
        return FileResponse(graph_file, headers={"Content-Disposition": "attachment; filename=plot.png"})
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@app.post("/calculate/derivative/")
async def calculate_derivative(expression: str):
    try:
        # Parse la expresión matemática
        x = symbols('x')
        expr = sympify(expression)

        # Calcula la derivada de la expresión
        derivative = diff(expr, x)

        return {"derivative": str(derivative), "message": "Success"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))