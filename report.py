# imports
from questions import question_1, question_2, question_3
from queries import query_1, query_2, query_3
import psycopg2

# Database Name
DBNAME = "news"


# function to execute the given Queries
def execute_query(questionString, query, connection):
    # counter
    count = 0
    print(questionString + '\n')

    # creating cursor
    cursor = connection.cursor()

    # executing query
    cursor.execute(query)

    # fetching the results
    results = cursor.fetchall()

    # loop to extract individual results
    for result in results:

        # incrementing counter
        count += 1

        # condition
        if questionString != question_3:
            print(str(count) + ")  " + str(result[0]) + '  -- ' + str(
                result[1]) + ' views')
        else:
            print(str(count) + ")  " + str(result[0]) + '  -- ' + str(
                result[1]) + '%')
    print("\n\n")


# Main function
def main():
    print("connecting to database -->%s\n") % DBNAME

    # connecting to database
    connection = psycopg2.connect(database=DBNAME)

    # condition to check
    if connection.status == 1:
        print("connected successfully\n")
        print("executing queries\n")

        # method call to execute queries
        execute_query(question_1, query_1, connection)
        execute_query(question_2, query_2, connection)
        execute_query(question_3, query_3, connection)

        # execute_query(question_3, connection)
        connection.close()
    else:
        print("connection failed")


# Indicates that main function should be called on execution
if __name__ == '__main__':
    main()
