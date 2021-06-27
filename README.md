# Hypothesis testing error parameters calculator(error_param_cal)

Link to pypi: https://pypi.org/project/error-param-cal/

Calculate any of the 6 parameters of the power of a test iteratively.
The function will ask the user to specify the parameter to calulate and the user can terminate the current session with a simple y/n(i.e yes/no).

This error calculator function calculates the different parameter with the given data. The parameters include:

1. Sample Size(n)
2. Type I Error(alpha)
3. Type II Error(beta)
4. Population Mean
5. Sample Mean
6. Population Standard Deviation
 
## How does it work?

1. Select the error parameter number from above list.
2. Enter the asked required data.
3. Get the calculated output of the required parameter.
4. Repeat steps 1,2,3 for different parameters to be calculated continuing the code.
5. When you wish to quit type "n".


## Installation

Run the following to install:

```python
pip install error_param
```

## Usage

```python
import error_parameters_calculator

# function usage
error_parameters_calculator.error_param()

```
