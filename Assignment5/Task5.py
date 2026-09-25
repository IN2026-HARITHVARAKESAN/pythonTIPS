"""Understanding scope of variables in Python."""
    
def scope_function() -> None:
    """Demonstrate the scope of variables in Python."""
    local_variable = "local variable"
    print(f"Inside function - Global variable: {global_variable}, Local variable: {local_variable}")

if __name__ == "__main__":
    
    global_variable = "global variable"
    
    scope_function()
    
    print(f"Outside function - Global variable: {global_variable}, Local variable: {local_variable}")