#!/bin/bash

rm -r build dist nlp_annotations.egg-info
python3 setup.py sdist bdist_wheel
