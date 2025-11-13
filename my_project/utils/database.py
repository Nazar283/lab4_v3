import pymysql
import yaml
import os

class DatabaseConnection:
    _instance = None
    _connection = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DatabaseConnection, cls).__new__(cls)
        return cls._instance
    
    def get_connection(self):
        if self._connection is None or not self._connection.open:
            try:
                # Завантажуємо конфігурацію
                config_path = os.path.join(os.path.dirname(__file__), '..', '..', 'config', 'app.yml')
                with open(config_path, 'r', encoding='utf-8') as file:
                    config = yaml.safe_load(file)
                
                db_config = config['database']
                
                self._connection = pymysql.connect(
                    host=db_config['host'],
                    port=db_config['port'],
                    user=db_config['user'],
                    password=str(db_config['password']),
                    database=db_config['database'],
                    charset=db_config['charset'],
                    autocommit=True,
                    cursorclass=pymysql.cursors.DictCursor
                )
            except Exception as e:
                print(f"Database connection error: {e}")
                raise e
        
        return self._connection
    
    def close_connection(self):
        if self._connection and self._connection.open:
            self._connection.close()
            self._connection = None
