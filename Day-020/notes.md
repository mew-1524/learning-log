# Day 020 - Virtual Environment & Package Management

## What is pip?

pip is Python's package manager.

Example:

pip install requests

---

## What is a Virtual Environment?

A virtual environment creates an isolated Python environment for a project.

Command:

python -m venv myenv

---

## Activate

Windows:

myenv\Scripts\activate

Linux/macOS:

source myenv/bin/activate

---

## Deactivate

deactivate

---

## requirements.txt

Stores all project dependencies.

Install:

pip install -r requirements.txt

Create:

pip freeze > requirements.txt

---

## Advantages

- Keeps projects isolated
- Avoids package conflicts
- Easy collaboration
- Reproducible environments

---

## What I Learned

Today I learned about pip, virtual environments, package installation, and requirements.txt.