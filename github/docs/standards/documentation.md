# Documentation Standards
Documentation is divided into project and coding documentation. Project documentation
is intended for non-technical consumers like managers and coding documentation is 
intended for technical users like programmers.

# Project Documentation
Project documentation should go under `docs/project`

# Coding Documentation
All blocks of code should be commented with [docstrings](https://peps.python.org/pep-0257/), 
including modules, functions, classes, and methods. Comment in the body of a block on 
an as-needed basis. If you need to comment a given line in a body of a block, consider whether it can be refactored.

Comments should include a summary of the block and any parameters, returned values,
notes, and warnings related to the code.

Comments can be enhanced with the `Better Comments` VSCode extension, which adds 
coloring for warnings, questions, TODO anchors, and parameters.

![Alt text](static/image.png)