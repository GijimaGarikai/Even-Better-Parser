# Mathematical Expression Evaluator

This Python code implements a mathematical expression evaluator using the Shunting Yard algorithm. The evaluator supports a wide range of mathematical operators, functions, and constants. The goal is to provide a flexible and extensible tool for parsing and evaluating mathematical expressions. 

## Files

### 1. **Parser.py:**
   - Main code file that includes the implementation of the Shunting Yard algorithm for parsing and evaluating mathematical expressions.
   - Supports operators like +, -, *, /, ^, (, ), and various mathematical functions and constants.
   - Note: Refer to the code comments for detailed information on usage and features.

### 2. **Helper_Functions.py:**
   - Module providing utility functions used in the expression parser.
   - Functions include checking if a word is an integer or decimal, finding matching parentheses, and checking elements for stack addition.

### 3. **Math_Functions.py:**
   - Module containing dictionaries for operator precedence, mathematical operators, functions, and constants.
   - Precedence dictionary is used in the Shunting Yard algorithm.
   - Operators, functions, and constants dictionaries provide the necessary mathematical operations and values for evaluation.

### 4. **Operator_Functions.py:**
   - Module containing basic operator functions (addition, subtraction, multiplication, division) used in the expression parser.
   - These functions are utilized in the Math_Functions module for mathematical operations.


## Features

### Supported Operators

- Addition (`+`)
- Subtraction (`-`)
- Multiplication (`*`)
- Division (`/`)
- Exponentiation (`^`)

### Supported Functions

##### Functions:
- Exponential: `exp`, `sqrt`
- Logarithmic: `ln`, `log`
- Trigonometric: `sin`, `cos`, `tan`, `asin`, `acos`, `atan`
- Hyperbolic: `sinh`, `cosh`, `tanh`, `asinh`, `acosh`, `atanh`

##### Constants:
- `e` (Euler's number)
- `pi` (Pi)

### Code Organization for Parser.py:
#### Modules
#### Math_Functions:
  Contains dictionaries for operator precedence (precedence), mathematical functions (functions), and constants (constants).
#### Helper_Functions:
  Provides utility functions for checking integers or decimals, matching brackets, evaluating expressions, and checking elements.


#### Code Structure:

1. **Tokenization (make_infix):**
   - Splits the input expression into individual tokens, handling functions, parentheses, operators, and constants.

2. **Infix Adjustment (good_infix):**
   - Further polishes the infix expression to address issues with subtraction and prepares it for postfix conversion.

3. **Postfix Conversion (make_postfix):**
   - Converts the infix expression into postfix notation using the Shunting Yard algorithm.

4. **Expression Evaluation (evaluator):**
   - Evaluates a postfix expression, considering functions, constants, and basic mathematical operations.

5. **Function and Bracket Evaluation (func_eval, bracket_eval):**
   - Handles the evaluation of functions and expressions enclosed in brackets.

  
## Usage

To use the expression evaluator, follow these steps:

1. **Install Dependencies:**
   - Make sure you have Python installed on your system.

2. **Run the Code:**
   - Execute the provided Python script, making sure to adjust any input expressions within the `example` function.

   ```python
   expr = "2+cos(pi/4)*tan( pi / 4 )+sin(3+pi-2-1-0- pi ) -10-2-1+ ln( e ) - log( 1  0 . 0 ^ 1 0 . 0)"
   example(expr)
   ```

3. **Review Output:**
   - The script will output the intermediate steps of expression evaluation, including tokenization, infix adjustment, postfix conversion, and the final result.

## Notes

1. **Implicit Multiplication:**
   - Ensure that multiplication is explicitly indicated with '*' in expressions.

2. **Whitespace Handling:**
   - The parser ignores whitespace within expressions but may produce errors with functions having similar names and whitespace in between characters.

3. **Function and Constant Naming:**
   - Be cautious with whitespace when using functions and constants, as similar names may lead to errors.

## Example

Consider the following example expression:

```python
expr = "2+cos(pi/4)*tan( pi / 4 )+sin(3+pi-2-1-0- pi ) -10-2-1+ ln( e ) - log( 1  0 . 0 ^ 1 0 . 0)"
example(expr)
```

The output will demonstrate how the expression is tokenized, converted to infix notation, adjusted for subtraction, converted to postfix notation, and finally evaluated, providing the result of the expression.

Feel free to modify the provided example or integrate the code into your project for mathematical expression evaluation.
