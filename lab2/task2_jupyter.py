from keystoneauth1 import loading
from keystoneauth1 import session
from novaclient import client
from os import environ as env

loader = loading.get_plugin_loader('password')

auth = loader.load_from_options(auth_url=env['OS_AUTH_URL'],
				username=env['OS_USERNAME'],
				password=env['OS_PASSWORD'],
				project_id=env['OS_PROJECT_ID'],
				project_domain_name=env['OS_USER_DOMAIN_NAME'],
                           	user_domain_name=env['OS_USER_DOMAIN_NAME'],
                           	)

sess = session.Session(auth=auth)

nova = client.Client("2", session=sess)

servers =  nova.servers.list()
for s in servers:
	print s
