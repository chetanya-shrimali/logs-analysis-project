# logs-analysis-project
A project to connect to PostgreSql database using the `psycopg2` library and executing complex Queries on the data provided
by `news` database
### Requirements
- Download `newsdata.sql` from the following link
`https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip'`
- Project is built in Python. So, `python 2.7+` is required
- Install `PostgreSQL`
- Install library `psycopg2` using command 'sudo pip install psycopg2' for linux
- For window users `sudo pip install psycopg2`

### How to run
- Open terminal in the project directory
- Create the database `news` in PostgreSQL and execute the `newsdata.sql` using following commands
`sudo -u postgres psql`
- In the psql shell type
`create database news`
`\q`
- In the directory containing newsdata.sql open terminal and type following
`sudo -u postgres psql news -f newsdata.sql`
- Type `\q` to exit psql shell
- In ternminal type following
`python report.py`