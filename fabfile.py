import fabric
from fabric import api
from fabric.api import local

def rin(i='grmetodos'):
    local("python tblmet/manage.py sqlall %s" % i)
    local("python tblmet/manage.py syncdb")
    local("python tblmet/manage.py migrate %s" % i)

def deploy(i=1):
#    local('git add .gitignore')
#     local('git commit -m \'alteracao %d\'' %i)
	local('git add .')
	local('git commit -m \'test %s\''%i)
	local('git push origin master')
	local("ssh -A koblitz@github.com -A 'cd tblmet; git pull -v'")
#	local('git push heroku master')
#	local('git push origin master')
#	local('git push origin master')
#	local('git push origin master')
#def back():
#	 local('heroku pgbackups:capture')
#	 local('heroku pgbackups:url b004')
 #    local('heroku pgbackups:destroy b003')
#     local('')
#$ fab hello:name=Jeff
#def restore()
#	 local('heroku pgbackups:restore DATABASE b007')

#download de qq lugar:
#PGPASSWORD=mypassword pg_dump -Fc --no-acl --no-owner -h myhost -U myuser mydb > mydb.dump

