# cdb
This is a program use python to connect ot MySQL database

## steps to install mariadb on centos7 and use python connect to db.

*    1. yum install -y mysql 
*    2. yum install -y mariadb-server
*    3. yum install -y mysql-devel
*    4. python 
`	import MySQLdb
	db =  MySQLdb.connect("localhost","root","","")
	cursor =  db.cursor()
	cursor.execute("SELECT VERSION()")
	data = cursor.fetchone()
	print "Database version : %s"%data
	db.close()
`
## jenkins.sh
* used for pull  the code to lib