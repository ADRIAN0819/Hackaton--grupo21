# src/calculator.py

def calculate(expression):
    try:
        # Limpieza de la expresión: elimina espacios innecesarios
        expression = expression.strip()
        
        # Verificación para evitar entrada vacía o solo espacios
        if not expression:
            raise ValueError("La expresión no puede estar vacía o contener solo espacios.")
        
        # Verificación para evitar caracteres no permitidos
        for char in expression:
            if not (char.isdigit() or char in '+-*/(). ' or char == '.'):
                raise ValueError("La expresión contiene caracteres no permitidos.")
        
        # Evaluación de la expresión usando eval de forma segura
        result = eval(expression, {"__builtins__": None}, {})
        
        # Verificación para evitar división por cero
        if isinstance(result, float) and (result == float('inf') or result == float('-inf')):
            raise ZeroDivisionError("División por cero.")
        
        # Redondear solo si el resultado es flotante y en operaciones específicas
        if isinstance(result, float) and expression.count('/') == 0:  # Redondeo solo si no hay división
            result = round(result, 1)
        
        return result

    except ZeroDivisionError as e:
        raise ZeroDivisionError("División por cero.") from e
    except SyntaxError as e:
        raise SyntaxError("Error de sintaxis en la expresión.") from e
    except Exception as e:
        raise ValueError("Error en la expresión.") from e
