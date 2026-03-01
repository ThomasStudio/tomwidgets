import customtkinter as ctk
from tomwidgets.widget.CodeWin import CodeWin
from ..widget.Theme import Mode


def createCodeWinExample():
    """Create and display a CodeWin example."""
    # Set appearance mode
    ctk.set_appearance_mode("dark")  # Start with dark theme

    # Create the main application window
    root = ctk.CTk()
    root.title("CodeWin Example")
    root.geometry("800x600")

    # Create CodeWin instance
    codeWin = CodeWin(root, title="Code Editor",
                      language="python", asWin=False)
    codeWin.pack(fill="both", expand=True, padx=10, pady=10)

    # Sample code for different languages
    pythonCode = '''# Python example code
def fibonacci(n):
    """Calculate the nth Fibonacci number."""
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

class MathOperations:
    """A class for mathematical operations."""
    
    def __init__(self):
        self.result = 0
    
    def add(self, a, b):
        """Add two numbers."""
        self.result = a + b
        return self.result
    
    def multiply(self, a, b):
        """Multiply two numbers."""
        self.result = a * b
        return self.result

# Test the functions
if __name__ == "__main__":
    fib_result = fibonacci(10)
    print(f"Fibonacci(10) = {fib_result}")
    
    math_ops = MathOperations()
    sum_result = math_ops.add(5, 3)
    product_result = math_ops.multiply(4, 7)
    print(f"5 + 3 = {sum_result}")
    print(f"4 * 7 = {product_result}")
'''

    javaCode = '''// Java example code
public class Calculator {
    private double result;
    
    public Calculator() {
        this.result = 0.0;
    }
    
    public double add(double a, double b) {
        result = a + b;
        return result;
    }
    
    public double subtract(double a, double b) {
        result = a - b;
        return result;
    }
    
    public double multiply(double a, double b) {
        result = a * b;
        return result;
    }
    
    public double divide(double a, double b) {
        if (b != 0) {
            result = a / b;
            return result;
        } else {
            throw new ArithmeticException("Cannot divide by zero");
        }
    }
    
    public static void main(String[] args) {
        Calculator calc = new Calculator();
        System.out.println("5 + 3 = " + calc.add(5, 3));
        System.out.println("10 - 4 = " + calc.subtract(10, 4));
    }
}
'''

    kotlinCode = '''// Kotlin example code
class Calculator(private var result: Double = 0.0) {
    
    fun add(a: Double, b: Double): Double {
        result = a + b
        return result
    }
    
    fun subtract(a: Double, b: Double): Double {
        result = a - b
        return result
    }
    
    fun multiply(a: Double, b: Double): Double {
        result = a * b
        return result
    }
    
    fun divide(a: Double, b: Double): Double {
        require(b != 0.0) { "Cannot divide by zero" }
        result = a / b
        return result
    }
    
    companion object {
        @JvmStatic
        fun main(args: Array<String>) {
            val calc = Calculator()
            println("5 + 3 = ${calc.add(5.0, 3.0)}")
            println("10 - 4 = ${calc.subtract(10.0, 4.0)}")
        }
    }
}
'''

    javascriptCode = '''// JavaScript example code
class Calculator {
    constructor() {
        this.result = 0;
    }
    
    add(a, b) {
        this.result = a + b;
        return this.result;
    }
    
    subtract(a, b) {
        this.result = a - b;
        return this.result;
    }
    
    multiply(a, b) {
        this.result = a * b;
        return this.result;
    }
    
    divide(a, b) {
        if (b !== 0) {
            this.result = a / b;
            return this.result;
        } else {
            throw new Error("Cannot divide by zero");
        }
    }
}

// Test the calculator
const calc = new Calculator();
console.log("5 + 3 = " + calc.add(5, 3));
console.log("10 - 4 = " + calc.subtract(10, 4));

// Function example
function fibonacci(n) {
    if (n <= 1) return n;
    return fibonacci(n - 1) + fibonacci(n - 2);
}

console.log("Fibonacci(10) = " + fibonacci(10));
'''

    typescriptCode = '''// TypeScript example code
interface CalculatorInterface {
    add(a: number, b: number): number;
    subtract(a: number, b: number): number;
    multiply(a: number, b: number): number;
    divide(a: number, b: number): number;
}

class Calculator implements CalculatorInterface {
    private result: number;
    
    constructor() {
        this.result = 0;
    }
    
    add(a: number, b: number): number {
        this.result = a + b;
        return this.result;
    }
    
    subtract(a: number, b: number): number {
        this.result = a - b;
        return this.result;
    }
    
    multiply(a: number, b: number): number {
        this.result = a * b;
        return this.result;
    }
    
    divide(a: number, b: number): number {
        if (b !== 0) {
            this.result = a / b;
            return this.result;
        } else {
            throw new Error("Cannot divide by zero");
        }
    }
}

// Generic function example
function identity<T>(arg: T): T {
    return arg;
}

// Test the calculator
const calc = new Calculator();
console.log("5 + 3 = " + calc.add(5, 3));
console.log("10 - 4 = " + calc.subtract(10, 4));

// Type assertion
let someValue: any = "this is a string";
let strLength: number = (someValue as string).length;
'''

    # Set initial code
    codeWin.setCode(pythonCode, "python")

    # Add some buttons for demonstration
    buttonFrame = ctk.CTkFrame(root)
    buttonFrame.pack(fill="x", padx=10, pady=5)

    # Language selection buttons
    ctk.CTkButton(buttonFrame, text="Python",
                  command=lambda: codeWin.setCode(pythonCode, "python")).pack(side="left", padx=5)
    ctk.CTkButton(buttonFrame, text="Java",
                  command=lambda: codeWin.setCode(javaCode, "java")).pack(side="left", padx=5)
    ctk.CTkButton(buttonFrame, text="Kotlin",
                  command=lambda: codeWin.setCode(kotlinCode, "kotlin")).pack(side="left", padx=5)
    ctk.CTkButton(buttonFrame, text="JavaScript",
                  command=lambda: codeWin.setCode(javascriptCode, "javascript")).pack(side="left", padx=5)
    ctk.CTkButton(buttonFrame, text="TypeScript",
                  command=lambda: codeWin.setCode(typescriptCode, "typescript")).pack(side="left", padx=5)

    # Theme toggle button
    ctk.CTkButton(buttonFrame, text="Toggle Theme",
                  command=lambda: codeWin.setLightMode() if codeWin.currentMode == Mode.Dark else codeWin.setDarkMode()).pack(side="right", padx=5)

    # Search toggle button
    ctk.CTkButton(buttonFrame, text="Toggle Search",
                  command=codeWin.toggleSearchBar).pack(side="right", padx=5)

    return root


def main():
    app = createCodeWinExample()
    app.mainloop()


if __name__ == "__main__":
    main()
