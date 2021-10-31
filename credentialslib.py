class CredentialsDB:
    """Store database credentials
    """
    
    def __init__(self, hostname, username, password, port, service_name): 
        """Instantiate a CredentialsDB object to store database credentials

        Args:
            hostname (str): The hostname address of the database
            username (str): The username of the database
            password (str): The password of the database
            port (str): The port of the database
            service_name (str): The service name of the database
        """
        
        # Set the hostname attribute
        self.hostname = hostname 
        
        # Set the username attribute
        self.username = username
        
        # Set the password attribute
        self.password = password 
        
        # Set the port attribute
        self.port = port 
        
        # Set the service name attribute
        self.service_name = service_name



class CredentialsElastic:
    """Store ElasticSearch credentials
    """
    
    def __init__(self, hostname, port, username, password):
        """Instantiate a CredentialsElastic object to store the credentials of 
        an ElasticSearch cluster 

        Args:
            ip (str): The IP of the logstash
            port (str): The port number of the logstash
            username (str): The username of the logstash
            password (str): The password of the logstash
        """
        
        self.hostname = hostname
        self.port = port 
        self.username = username 
        self.password = password 
        

class CredentialsOpenShift:
    """Store OpenShift credentials
    """
    
    def __init__(self, hostname, port, username, password):
        """Instantiate a CredentialsOpenShift object to store the credentials of 
        OpenShift.

        Args:
            ip (str): The IP of OpenShift
            port (str): The port number of OpenShift
            username (str): The username of OpenShift
            password (str): The password of OpenShift
        """
        
        self.hostname = hostname
        self.port = port 
        self.username = username 
        self.password = password 