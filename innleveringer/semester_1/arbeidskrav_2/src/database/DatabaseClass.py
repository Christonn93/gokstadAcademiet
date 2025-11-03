import os
from mysql.connector import connect, Error
from dotenv import load_dotenv


class Database:
    """A comprehensive database management class with integrated configuration"""

    def __init__(self, database_name=None, config=None):
        """
        Initialize the database connection

        Args:
            database_name (str): Optional database name to use
            config (dict): Optional custom configuration. Uses environment variables by default
        """
        # Load environment variables
        load_dotenv()

        # Set configuration
        if config:
            self.config = config
        else:
            self.config = {
                "host": os.getenv("DB_HOST", "localhost"),
                "user": os.getenv("DB_USER", "root"),
                "password": os.getenv("DB_PASSWORD", ""),
                "port": int(os.getenv("DB_PORT", 3306)),
                "database": database_name or os.getenv("DB_NAME", "")
            }

        self.database_name = self.config.get('database')
        self.conn = None
        self.cursor = None
        self.connected = False

    def _get_config_without_db(self):
        """Get configuration without database name for server-level connections"""
        config = self.config.copy()
        config.pop('database', None)
        return config

    def connect(self, use_database=True):
        """
        Establish database connection

        Args:
            use_database (bool): Whether to connect to a specific database or just the server

        Returns:
            bool: True if connection successful, False otherwise
        """
        try:
            if use_database and self.database_name:
                # Connect to specific database
                self.conn = connect(**self.config)
                self.cursor = self.conn.cursor(dictionary=True)
                print(f"Connected to database: {self.database_name}")
            else:
                # Connect to MySQL server without specific database
                config_without_db = self._get_config_without_db()
                self.conn = connect(**config_without_db)
                self.cursor = self.conn.cursor(dictionary=True)
                print("Connected to MySQL server")

            self.connected = True
            return True

        except Error as e:
            print(f"MySQL connection error: {e}")
            self.connected = False
            return False

    def disconnect(self):
        """Close database cursor and connection"""
        try:
            if self.cursor is not None:
                self.cursor.close()
                print("Database cursor closed")

            if self.conn is not None and self.conn.is_connected():
                self.conn.close()
                print("Database connection closed")

            self.connected = False
            print("Database resources cleaned up\n")

        except Error as e:
            print(f"Error during disconnect: {e}")

    def execute_query(self, sql_query, params=None, fetch=True):
        """
        Execute a SQL query and return results

        Args:
            sql_query (str): SQL query to execute
            params (tuple): Parameters for parameterized queries
            fetch (bool): Whether to fetch results (for SELECT queries)

        Returns:
            list/dict/int: Query results or rowcount for non-SELECT queries
        """
        if not self.connected:
            if not self.connect():
                return None

        try:
            # Execute the query
            self.cursor.execute(sql_query, params or ())

            # If it's a SELECT query, fetch the results
            if fetch:
                results = self.cursor.fetchall()
                return list(results) if results else []

            # For INSERT, UPDATE, DELETE - commit and return rowcount
            else:
                self.conn.commit()
                return self.cursor.rowcount

        except Error as e:
            print(f"MySQL error in query execution: {e}")
            return None
        except Exception as e:
            print(f"Unexpected error in query execution: {e}")
            return None

    def create_database(self, db_name=None):
        """
        Create a new database

        Args:
            db_name (str): Database name to create. Uses config database if not provided

        Returns:
            bool: True if successful, False otherwise
        """
        target_db = db_name or self.database_name
        if not target_db:
            print("No database name specified")
            return False

        try:
            # Connect without specific database
            if not self.connect(use_database=False):
                return False

            # Create database
            self.cursor.execute(f"CREATE DATABASE IF NOT EXISTS {target_db}")
            print(f"Database '{target_db}' created successfully")

            # Update config and reconnect to the new database
            self.database_name = target_db
            self.config['database'] = target_db
            self.disconnect()
            return self.connect(use_database=True)

        except Error as e:
            print(f"Error creating database: {e}")
            return False

    def drop_database(self, db_name=None):
        """
        Remove (drop) database and all its tables

        Args:
            db_name (str): Database name to drop. Uses config database if not provided

        Returns:
            bool: True if successful, False otherwise
        """
        target_db = db_name or self.database_name
        if not target_db:
            print("No database name specified")
            return False

        try:
            # Connect without specific database
            if not self.connect(use_database=False):
                return False

            # Drop database
            self.cursor.execute(f"DROP DATABASE IF EXISTS {target_db}")
            print(f"Database '{target_db}' dropped successfully")

            # Update state if we dropped the current database
            if db_name == self.database_name or (not db_name and target_db == self.database_name):
                self.database_name = None
                self.config.pop('database', None)
                self.connected = False

            return True

        except Error as e:
            print(f"Error dropping database: {e}")
            return False

    def create_tables_from_files(self, sql_files):
        """
        Create database tables from SQL files

        Args:
            sql_files (list): List of paths to SQL files

        Returns:
            tuple: (success_count, error_count)
        """
        if not sql_files:
            print("No SQL files provided")
            return 0, 0

        if not self.connected:
            if not self.connect():
                return 0, len(sql_files)

        success_count = 0
        error_count = 0

        try:
            for file_path in sql_files:
                print(f"Creating tables from: {file_path}")

                # Validate file existence
                if not os.path.exists(file_path):
                    print(f"File not found: {file_path}")
                    error_count += 1
                    continue

                # Read SQL file
                with open(file_path, "r", encoding="utf-8") as f:
                    sql_script = f.read()

                # Split and execute statements
                statements = [stmt.strip() for stmt in sql_script.split(";") if stmt.strip()]
                print(f"Found {len(statements)} statements to execute")

                file_success = True
                for i, statement in enumerate(statements, 1):
                    if statement.strip():
                        try:
                            self.cursor.execute(statement)
                            print(f"✓ Statement {i} executed successfully")
                        except Error as e:
                            print(f"✗ Error in statement {i}: {e}")
                            file_success = False
                            error_count += 1
                            break

                if file_success:
                    success_count += 1
                    print(f"Finished creating tables from {file_path}\n")

            # Commit all changes
            self.conn.commit()
            print(f"Table creation completed: {success_count} successful, {error_count} failed")
            return success_count, error_count

        except Error as e:
            print(f"MySQL error during table creation: {e}")
            self.conn.rollback()
            return success_count, error_count + (len(sql_files) - success_count)

    def seed_database(self, sql_file_path):
        """
        Populate database with data from SQL seed file

        Args:
            sql_file_path (str): Path to SQL seed file

        Returns:
            tuple: (successful_statements, failed_statements)
        """
        if not sql_file_path or not os.path.exists(sql_file_path):
            print(f"Invalid or missing SQL file: {sql_file_path}")
            return 0, 0

        if not self.connected:
            if not self.connect():
                return 0, 0

        try:
            # Read and parse SQL file
            with open(sql_file_path, "r", encoding="utf-8") as f:
                sql_script = f.read()

            statements = [stmt.strip() for stmt in sql_script.split(";") if stmt.strip()]
            print(f"Starting database seeding with {len(statements)} statements...")

            successful_statements = 0
            failed_statements = 0

            for statement in statements:
                try:
                    self.cursor.execute(statement)
                    successful_statements += 1
                except Error as e:
                    print(f"Error executing statement: {e}")
                    failed_statements += 1

            # Commit changes
            self.conn.commit()
            print(f"Database seeding completed: {successful_statements} successful, {failed_statements} failed")

            return successful_statements, failed_statements

        except Error as e:
            print(f"MySQL error during seeding: {e}")
            self.conn.rollback()
            return 0, len(statements) if 'statements' in locals() else 0
        except Exception as e:
            print(f"Unexpected error during seeding: {e}")
            self.conn.rollback()
            return 0, len(statements) if 'statements' in locals() else 0

    def database_exists(self, db_name=None):
        """
        Check if database exists

        Args:
            db_name (str): Database name to check. Uses config database if not provided

        Returns:
            bool: True if database exists, False otherwise
        """
        target_db = db_name or self.database_name
        if not target_db:
            return False

        try:
            # Connect without specific database to check existence
            was_connected = self.connected
            if not self.connected:
                if not self.connect(use_database=False):
                    return False

            self.cursor.execute("SHOW DATABASES LIKE %s", (target_db,))
            exists = self.cursor.fetchone() is not None

            # Reconnect to original database if we were connected before
            if was_connected and self.database_name:
                self.disconnect()
                self.connect(use_database=True)

            return exists

        except Error as e:
            print(f"Error checking database existence: {e}")
            return False

    def get_connection_info(self):
        """Return current connection information"""
        return {
            'connected': self.connected,
            'database': self.database_name,
            'host': self.config.get('host'),
            'user': self.config.get('user'),
            'port': self.config.get('port')
        }

    def commit(self):
        """Commit the current transaction"""
        if self.conn and self.connected:
            self.conn.commit()

    def rollback(self):
        """Rollback the current transaction"""
        if self.conn and self.connected:
            self.conn.rollback()

    def __enter__(self):
        """Context manager entry"""
        self.connect()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit"""
        self.disconnect()