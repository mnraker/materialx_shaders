#!/bin/bash
cat shaders.py.util > shaders.py
../cmd/generate_python_create_functions/generate_python_create_functions >> shaders.py
