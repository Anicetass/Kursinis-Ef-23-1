# Coursework report

## 1. Introduction

### My topic

The goal of my course work was to progam a classic two-player game called “Connect Four”

"Connect Four" is a classic two-player board game where players take turns dropping colored discs into a vertically suspended grid. The objective is to be the first to form a horizontal, vertical, or diagonal line of four discs of the same color.

### What is your program?

My program is a functional implementation of "Connect Four"

### Running the Program

To run the program, you need to have Python installed on your system along with the Pygame and NumPy libraries. Simply execute the Python script `connectFour.py` in your Python environment.

### Using the Program

Before running the program, you can change the presets of the game in the `connectFour.setup.txt` file.

Upon running the program, you will be presented with the Connect Four game board. Players take turns placing their colored discs on the board by pressing corresponding keys (1-7) on the keyboard. The game ends when one player achieves a winning combination or when the board is full resulting in a draw.

## 2. Body/Analysis

### Object-Oriented Programming (OOP) Pillars

- **Encapsulation**
  - Meaning: Encapsulation refers to the bundling of data and methods into a single unit, known as a class. It hides the internal state of an object and only exposes the necessary functionalities through methods.
  - Usage in the code: I used encapsulation by creating different classes like `BoardGame`, `ConnectFour`, `Display`, `Logger`, and `FileSetup`. Each class encapsulates related data and functions within itself. For example, `ConnectFour` class encapsulates the game logic, `Logger` class encapsulates game logs, ect.
  - Overall usage: Encapsulation helps in organizing code, and reducing complexity.
  - ![image](https://github.com/Anicetass/Kursinis_PRIVATE/assets/144654014/69232f53-d57b-414e-bda3-1f039c8a7973)
  
- **Abstraction**
  - Meaning: Abstraction focuses on hiding the complex implementation details and showing only the essential features of an object.
  - Usage in the code: Abstraction is employed in methods like `valid_move`, `place_piece`, and `check_win` which provide abstractions of the game mechanics without exposing the entire logic behind them.
  - Overall usage: Abstraction  enhances readability, reduces complexity, and facilitates code maintenance.
  - ![image](https://github.com/Anicetass/Kursinis_PRIVATE/assets/144654014/156cb15e-980a-4943-9783-ea861fb66fce)
  
- **Inheritance**:
  - Meaning: Inheritance is a mechanism where a class (subclass) inherits properties and methods from an existing class (superclass). It allows the subclass to use methods of the superclass.
  - Usage in the code: Inheritance is demonstrated in the relationship between the `ConnectFour` class and its parent class `BoardGame`. `ConnectFour` inherits properties and methods from `BoardGame`, such as the game board representation (which was mainly used for program development) and game state properties.
  - Overall usage: Inheritance establishes a hierarchy among classes and promotes code reuse.
  - ![image](https://github.com/Anicetass/Kursinis_PRIVATE/assets/144654014/c771a81a-5640-4a75-922e-f15f5e208eb0)

- **Polymorphism**:
  - Meaning: Polymorphism allows objects of different classes to be treated as objects of a common superclass.
  - Usage in the code: In the `Display` class, the `board_top_text` method can accept and render different messages. It can also accecpt different display colors. While not a strict example of polymorphism, this flexibility still promotes polymorphism, allowing the method to handle different messages.
  - Overall usage: Polymorphism promotes code reuse, enhances flexibility, and simplifies code maintenance.
  - ![image](https://github.com/Anicetass/Kursinis_PRIVATE/assets/144654014/8f0a07ba-8931-4820-b081-b98ca9b3b476)

### Design Patterns

- **Singleton**
  - How it's used: The Singleton design pattern is implemented in the `Logger` class. The `Logger` class is used to create logs of the game and export it once it finishes.
  - How it works: The Singleton pattern ensures that the `Logger` class has a private constructor to prevent direct instantiation of the class. Instead, it provides a static method `(__new__)` to create and return the single instance of the class. Whenever the `Logger` class is instantiated, it checks if an instance already exists. If it does, it returns the existing instance; otherwise, it creates a new instance.
  - Why it's suitable: The Singleton pattern is most suitable because you want to ensure that there's only one `Logger` instance throughout the application. This way you when you log events from different parts of the code you ensure that it will all be directed to the same place.
  - ![image](https://github.com/Anicetass/Kursinis_PRIVATE/assets/144654014/6184810f-4cae-4ce0-81ed-84476cde06f3)

- **Decorator**
  - How it's used: The Decorator pattern is used in the `runtime_decorator` function. This pattern allows behavior to be added to individual objects dynamically, without affecting the behavior of other objects of the same class.
  - How it works: The `runtime_decorator` function takes a function as input and returns a wrapper function that measures the execution time of the input function. This wrapper function adds behavior (measuring execution time) to the original function without modifying its code directly.
  - Why it's suitable: The Decorator pattern is suitable here because it allows you to add functionality to functions without modifying their code directly. It's a really convenient way to measure game runtime and you can reuse it for other parts of the program if needed.
  - ![image](https://github.com/Anicetass/Kursinis_PRIVATE/assets/144654014/3f3a43e9-7602-46fd-85c6-c77c70b95cdc)

### Reading from file and writing to file

- **Reading from file**
  - The `FileSetup` class reads from the setup file (text file) using the `setup_from_file` method.
  - It checks if the file exists using the __check_file_exists method before attempting to read from it.
  - If the file exists, it iterates through each line, extracts the configuration data, and updates the corresponding constants.
  - ![image](https://github.com/Anicetass/Kursinis_PRIVATE/assets/144654014/80df782e-a8be-45af-99e0-d0da3a215719)

- **Writing to file**
  - The `Logger` class logs events during the game using the `log_event` method.
  - It maintains a list `_log_list` to store the logged events.
  - When the game ends, the `export_log_to_txt` method is called to export the logged events to a text file.
  - It opens the log file in write mode and iterates through the _log_list, writing each log entry to the file.
  - ![image](https://github.com/Anicetass/Kursinis_PRIVATE/assets/144654014/7977e8c6-caca-458c-b8dd-9a0a65a9d5c1)

## 3. Results and Summary

### Results

- The program successfully implements the Connect Four game with a graphic interface
- The main challenges I faced mainly regarded the implementation of a grapic interface.
- The program's abstraction allows users to interact with the game using simplified interfaces, hiding complex implementation details.

### Summary

- The Connect Four game implementation has achieved a functional and interactive gameplay experience.
- The program demonstrates effective utilization of OOP principles and design patterns for modularity, extensibility, and maintainability.
- Future prospects could include improving and putting the program online for multiplayer gameplay.

### Application Extension
- Extension of the application can be achieved by adding features such as:
  - Network multiplayer functionality to enable online gameplay.
  - AI algorithms for single-player mode, providing challenging opponents with different strategies.
  - Enhanced graphics and animations to improve the visual appeal and clarity.
