<?php 

	class db{
		//properties
			private $dbhost = "localhost";
			private $dbuser = "root";
			private $dbpass = "";
			private $dbname = "slimblog";
			
		

		//connect to db
		public function connect() {
			$mysql_conn_string = "mysql:host=$this->dbhost;dbname=$this->dbname;";
			$dbConnection = new PDO($mysql_conn_string, $this->dbuser, $this->dbpass);
			$dbConnection->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
			return $dbConnection;
		}

	}