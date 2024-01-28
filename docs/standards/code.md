# Coding Standards

This document is coding standards for the Comfort Airlines application. 
The standards used are an extension of the 
[Python PEP 8 Coding Standards](https://peps.python.org/pep-0619/). Below is a summary of the important parts of the document:
- Use 4 spaces for indentation. Do not use tabs. You can [configure VSCode to automatically transform tabs into 4 spaces](https://bobbyhadz.com/blog/vscode-change-indentation#change-the-indentation-in-vs-code-2-or-4-spaces-tab-size) in the settings
- Lines of code should not exceed the size of the screen (default: 80 characters). Use [line continuations](https://stackoverflow.com/questions/53162/how-can-i-do-a-line-break-line-continuation-in-python-split-up-a-long-line-of) to break up long statements into multiple lines
- Strings should use double quotes. Characters should use single quotes. Note that this is a conventional difference and the language does not distinguish between the two.
- Comment all modules, functions, classes, and methods.
- Comment format should comply with [PEP 257 - Docstring Conventions](https://peps.python.org/pep-0257/)
- Always use should [snake_case](https://en.wikipedia.org/wiki/Snake_case) for variable and function names. Constants should be named in [CAPITAL_SNAKE_CASE](https://en.wikipedia.org/wiki/Snake_case)
- Use descriptive variable names. Do not abbreviate.
- Do not use global variables. If you need a global variable, use [dependency injection](https://en.wikipedia.org/wiki/Dependency_injection) with a [singleton](https://en.wikipedia.org/wiki/Singleton_pattern)
- All variables and functions should have type annotations