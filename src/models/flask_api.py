from flask import Flask, request, jsonify
import pandas as pd
import numpy as np
import os
import joblib


model = joblib.load("model/model.joblib")


