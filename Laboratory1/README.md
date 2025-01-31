# Lab 1: Factorial API

This is a simple FastAPI application that calculates the factorial of a given number. The API provides a single endpoint to compute the factorial and handles edge cases such as the input `0`.

## Features
- **Endpoint**: `/factorial/{starting_number}`
  - Accepts an integer input (`starting_number`).
  - Computes the factorial of the input using a `while` loop.
  - Returns the result in JSON format.

## Example Usage
- Request: `GET /factorial/5`
- Response:
  ```json
  {
    "starting_number": 5,
    "factorial": 120
  }