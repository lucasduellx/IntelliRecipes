import string
import random
#import urllib.parse 

#params = urllib.parse.quote_plus("Driver={ODBC Driver 18 for SQL Server};Server=tcp:intellirecipes.database.windows.net,1433;Database=intellirecipes;Uid=intellirecipes;Pwd=Intelli123;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;")


random_str = string.ascii_letters + string.digits + string.ascii_uppercase
key = ''.join(random.choice(random_str) for i in range(12))
DEBUG = True
SQLALCHEMY_DATABASE_URI = 'mysql://root:admin@localhost:3306/intellirecipes'
#SQLALCHEMY_DATABASE_URI = "mssql+pyodbc:///?odbc_connect=%s" % params
#SQLALCHEMY_COMMIT_ON_TEARDOWN = True
#SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = key
#SQLAZURECONNSTR_WWIF="<your-connection-string>"