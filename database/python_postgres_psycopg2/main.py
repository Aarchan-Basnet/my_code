import pandas as pd
import psycopg2  
import psycopg2.extras as extras 
import matplotlib.pyplot as plt

def unpivot_nepal_gdp(path):
    df = pd.read_csv(path)
    #print(df.head(10))
    #print(df.columns)
    nepal_data = df[df['Country Name'] == 'Nepal']
    #print(nepal_data)

    unpivot = pd.melt(
        nepal_data,
        id_vars=['Country Name', 'Country Code','Indicator Name', 'Indicator Code'],
        var_name='Year',
        value_name='GDP')
    #print(unpivot)
    #print(unpivot['GDP'].round(2))
    unpivot['rounded_GDP']=unpivot['GDP'].apply(lambda x: '%.2f' % x)
    print(unpivot)

    # save to csv file
    unpivot.to_csv('nepal_gdp_data.csv', sep = ',', index=False)
    
def insert_df_into_table(conn, df, table): 
	list_tuples = [tuple(x) for x in df.to_numpy()]

	cols = ','.join(list(df.columns))
	# SQL query to execute 
	query = "INSERT INTO %s(%s) VALUES %%s" % (table, cols) 
	cursor = conn.cursor() 
	try: 
		extras.execute_values(cursor, query, list_tuples) 
		conn.commit() 
	except (Exception, psycopg2.DatabaseError) as error: 
		print("Error: %s" % error) 
		conn.rollback() 
		cursor.close() 
		return 1
	print("the dataframe is inserted") 
	cursor.close() 
    
def connect_to_database(csv_file):
	#connect to your postgres database
	db_config = {
		"host": "localhost",
		"database": "postgres",
		"user": "postgres",
		"password": "1234",
	}

	df = pd.read_csv(csv_file)

	# Connect to the PostgreSQL database
	conn = psycopg2.connect(**db_config)
	cur = conn.cursor()

	# Define the CREATE TABLE statement based on the DataFrame columns
	create_table_sql = f"""
		DROP TABLE IF EXISTS nepal_gdp;
		CREATE TABLE nepal_gdp (
			{", ".join([f"{column} VARCHAR(255)" for column in df.columns])}
		)
	"""

	# Execute the CREATE TABLE statement
	cur.execute(create_table_sql)
	conn.commit()

	#insert dataframe into table
	insert_df_into_table(conn, df, 'nepal_gdp') 

	# Close the database connection
	cur.close()
	conn.close()

def plot_gdp(csv_file):
	df = pd.read_csv(csv_file)
	x = (df['Year'])
	y = (df['GDP'])
	x_ticks = x[::5]
	plt.plot(x,y)
	plt.xticks(x_ticks)
	plt.title('GDP of Nepal')
	plt.xlabel('Year')
	plt.ylabel('GDP Value')
	plt.legend(['GDP Score'])
	plt.show()

if __name__ == "__main__":
    path = 'world_gdp_data.csv'
    unpivot_nepal_gdp(path)
    
    csv_file = 'nepal_gdp_data.csv'
    connect_to_database(csv_file)
    
    plot_gdp(csv_file)