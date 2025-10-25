import allure
import psycopg2

def execute_and_log(cursor: psycopg2.extensions.cursor, query: str):
    with allure.step(f"SQL: {query[:50]}..."):
        allure.attach(query, name="SQL Query", attachment_type=allure.attachment_type.TEXT)
        try:
            cursor.execute(query)
            result = cursor.fetchall()
            allure.attach(str(result), name="Query Result", attachment_type=allure.attachment_type.TEXT)
            return result
        except psycopg2.Error as e:
            allure.attach(str(e), name="SQL Error", attachment_type=allure.attachment_type.TEXT)
            raise
