import pymysql
import yaml
import os
from dotenv import load_dotenv

# Завантаження ENV (.env)
load_dotenv()

def resolve_env(value: str):
    """
    Підміняє ${VAR} у YAML на реальне ENV значення.
    """
    if isinstance(value, str) and value.startswith("${") and value.endswith("}"):
        env_var = value[2:-1]
        return os.getenv(env_var)
    return value


class DatabaseConnection:
    """
    Singleton-клас для створення єдиного підключення до MySQL/RDS.
    """
    _instance = None
    _connection = None
    _config_loaded = False
    config = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def load_config(self):
        """
        Завантажує YAML один раз.
        """
        if not self._config_loaded:
            config_path = os.path.join(os.path.dirname(__file__), "..", "..", "config", "app.yml")

            with open(config_path, "r", encoding="utf-8") as file:
                self.config = yaml.safe_load(file)

            self._config_loaded = True

    def get_connection(self):
        """
        Повертає існуюче підключення або створює нове.
        """
        # Якщо вже є з’єднання → повертаємо
        if self._connection and self._connection.open:
            return self._connection

        # Завантажуємо YAML конфіг
        self.load_config()

        db_cfg = self.config["database"]

        # Підставляємо ENV-змінні
        host = resolve_env(db_cfg["host"])
        port = int(resolve_env(db_cfg["port"]))
        user = resolve_env(db_cfg["user"])
        password = resolve_env(db_cfg["password"])
        database = resolve_env(db_cfg["database"])
        charset = resolve_env(db_cfg["charset"])

        try:
            # Підключення до MySQL / AWS RDS
            self._connection = pymysql.connect(
                host=host,
                port=port,
                user=user,
                password=password,
                database=database,
                charset=charset,
                autocommit=True,
                cursorclass=pymysql.cursors.DictCursor,
                ssl={"ca": None}  # для AWS RDS SSL не обов'язковий
            )
            return self._connection

        except Exception as e:
            print(f"[DB ERROR] Cannot connect to database: {e}")
            raise e

    def show_tables(self):
        """
        Повертає список таблиць у поточній базі.
        """
        conn = self.get_connection()

        try:
            with conn.cursor() as cursor:
                cursor.execute("SHOW TABLES;")
                result = cursor.fetchall()

                return [list(row.values())[0] for row in result]

        except Exception as e:
            print(f"[DB ERROR] Cannot fetch tables: {e}")
            return []

    def close_connection(self):
        """
        Закриває з’єднання.
        """
        if self._connection and self._connection.open:
            self._connection.close()
            self._connection = None
