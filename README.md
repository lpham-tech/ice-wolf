# wolf_blog

##1. Setup blog
 in config.py file
 - set your secret key
 `SECRET_KEY = 'your secret key'`
 
 - set uri to your database, 
 `SQLALCHEMY_DATABASE_URI = 'uri to your db'`
 
 **example**:
 `SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'`
 
 - Set your mail info:
 # email server
    ```python
    MAIL_SERVER = 'your mail host' #'smtp.googlemail.com'
    MAIL_PORT = 587 # your mail port on server
    MAIL_USE_TLS = True # using TLS ?
    MAIL_USE_SSL = False # using SSL ?
    MAIL_USERNAME = 'your user name'#os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = "your password"#os.environ.get('MAIL_PASSWORD')
    
    #administrator list
    ADMINS = ['abc@example.com']
    ```