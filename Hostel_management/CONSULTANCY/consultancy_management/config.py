import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key-change-in-production'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI') or 'sqlite:///consultancy.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOAD_FOLDER = 'static/uploads'
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB max file size
    ALLOWED_EXTENSIONS = {'xlsx', 'xls'}
    
    # Payment Gateway Configuration (Razorpay example)
    RAZORPAY_KEY_ID = os.environ.get('RAZORPAY_KEY_ID') or 'test_key'
    RAZORPAY_KEY_SECRET = os.environ.get('RAZORPAY_KEY_SECRET') or 'test_secret'