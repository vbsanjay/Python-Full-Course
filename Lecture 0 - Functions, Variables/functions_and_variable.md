# Cli
CLI stands for Command Line Interface. It's a text-based interface used to interact with a computer program or operating system by typing commands into a terminal or console.

# Interpreted Language
## C and C++
C and C++ are typically classified as compiled languages. In C and C++, code is translated into machine code, which consists of binary instructions tailored to the specific hardware architecture and operating system. This process is facilitated by a compiler. As a result, executables produced from C and C++ source code are platform-specific and may require recompilation to run on different platforms. Once compiled, the machine code is directly executed by the CPU without additional translation steps. Therefore, C and C++ programs are precompiled into executable files before being executed.
## No Compilation Step
In Python, there's no need for a separate compilation step like in languages such as C and C++. Instead, Python code is executed directly without explicit compilation. This means that as each line of Python code is encountered, it's executed immediately, and the effects of that line, such as variable assignments, function calls, or changes in control flow, take effect right away. This line-by-line execution approach makes Python code execution more interactive and flexible.
## Python Interpreter
Python code is executed by the Python interpreter, which reads and interprets the code line by line. The Python interpreter is a program that translates Python code into machine-readable bytecode and executes it on the fly.
## Dynamic Typing
Python is dynamically typed, meaning you don't need to declare the data type of variables explicitly. Variables are dynamically assigned data types based on the values they hold at runtime. This dynamic typing feature allows for greater flexibility and ease of use but requires interpretation of variable types during execution
## Late Binding
Python employs late binding, also known as dynamic binding or runtime binding. In languages like C++, the binding of a function to its implementation occurs at compile time. However, in Python, the binding of a function to its implementation happens at runtime. This means that the specific function implementation to be called is determined dynamically during program execution based on the object type.
## Portability and Platform Independence
Since Python code is executed by the interpreter rather than directly by the underlying hardware, Python programs are highly portable and platform-independent. The same Python code can run on different operating systems without modification, as long as the appropriate Python interpreter is available for each platform.


