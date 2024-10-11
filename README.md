# Math Expression Solver API

This project is a FastAPI-based service that performs calculations on mathematical expressions, including solving equations, finding roots, calculating derivatives, and generating function plots. It uses symbolic computation (via `sympy`) and provides a simple API for interacting with the service.

## Features

- **Calculate and Plot Functions**: Input a mathematical expression and generate a plot of the function over a given range.
- **Find Roots**: Calculate the roots of a mathematical expression and visualize them on a graph.
- **Analyze Function Growth**: Detect and visualize regions where a function is increasing or decreasing.
- **Calculate Derivatives**: Symbolically compute the derivative of a given expression.

## API Endpoints

### 1. `POST /calculate/`
Generates and returns a plot of a given mathematical expression over a specified range.

**Request Body:**
```json
{
  "expression": "x**2 - 4",
  "x_range": "-10,10"
}


to be honest this readme file was made using ChatGPT
