import paramiko

def sftp_connection(host, username, private_key, port_number):

    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(host
                        ,port=port_number
                        ,username=username
                        ,key_filename=private_key)
    ftp_client = ssh_client.open_sftp()
    print("connected to sftp server")
    return ftp_client
