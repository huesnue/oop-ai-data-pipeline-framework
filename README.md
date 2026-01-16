# Advanced Python: Object-Oriented Programming — Portfolio Project

This repository is part of my 9‑week program to deepen advanced object‑oriented programming skills in Python.  
It is inspired by the LinkedIn Learning course *Advanced Python: Object-Oriented Programming*, but structured and implemented as a **professional, extensible portfolio project**.

---

## 🎯 Project Goals

- Apply advanced OOP concepts in real-world Python code  
- Implement and document key design patterns  
- Use modern Python idioms (type hints, dataclasses, pathlib, packaging)  
- Build a clean, modular, production‑grade architecture  
- Add unit tests, logging, and a CLI interface  
- Create a visible, recruiter‑ready engineering project  

---

## 🧱 Project Structure

```text
src/
  oop_training/
    models/
    patterns/
    utils/
    cli/
examples/
tests/
docs/
.github/workflows/

src/ → Production code

examples/ → Recreated course examples

tests/ → Unit tests

docs/ → Architecture, UML diagrams, design decisions

.github/ → CI/CD workflows

---

🧠 Learning Focus Areas
1. OOP Fundamentals (Chapter 1)
Classes & objects

Attributes & methods

Encapsulation

Magic methods

2. Inheritance & Polymorphism (Chapter 2)
Single & multiple inheritance

Method overriding

Mixins

3. Advanced Concepts (Chapter 3)
Abstract base classes

Interfaces

Composition vs. inheritance

4. Design Patterns (Chapter 4)
Strategy

Observer

Factory

Singleton

Template Method

### Class Creation Utilities

This module contains helper functions and utility classes that support the creation, configuration, and management of Python classes.  
The goal is to demonstrate how reusable utilities can simplify class construction, enforce consistent initialization logic, and reduce boilerplate across a larger codebase.

Key topics covered include:

- Utility functions for building and initializing classes  
- Reusable constructors and factory helpers  
- Encapsulating complex setup logic outside of the class itself  
- Improving maintainability by centralizing class‑creation patterns  
- Demonstrating when to prefer utilities over inheritance or mixins  

These utilities illustrate how larger Python systems benefit from clean separation between *what* a class represents and *how* it is created.

---

🧪 Testing
Unit tests are implemented using pytest.

```bash
pytest -q
```

---

🛠️ Installation & Setup

```bash
git clone <your-repo-url>
cd advanced-python-oop
pip install -e .
```

---

🚀 CLI (Optional)
The project includes an optional CLI to run selected examples or pattern demonstrations.

```bash
python -m oop_training.cli

```

---

📚 Documentation
The docs/ directory contains:

Architecture overview

UML diagrams

Design decisions

Pattern summaries

---

🗺️ Roadmap
[ ] Recreate examples from Chapter 1

[ ] Extend models from Chapter 2

[ ] Implement patterns from Chapter 3 and 4

[ ] Add unit tests for all modules

[ ] Add logging and configuration management

[ ] Expand CLI functionality

[ ] Add UML diagrams

[ ] Finalize CI/CD workflow

---

📄 License
MIT License

---

👤 Author
Hüsnü Türkac
Senior Quality Manager → AI/MLOps Engineer (in transition)

