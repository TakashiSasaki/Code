import xor
import sqlite3

if __name__ == "__main__":
    print(xor.xorUtf8Sha1All(["hello", "world"]))

    connection = sqlite3.connect("test.sqlite3")
    cursor = connection.cursor()

    cursor.execute("CREATE TABLE IF NOT EXISTS test (col1, col2, col3)")
    connection.commit()
