#!/usr/bin/env bash

DEVENV_USER=ubuntu
DEVENV_HOST=mizzychan.org

# Add ssh key if not present
if [[ `ssh-add -l | grep mizzychan_prod.pem | wc -l` != 1 ]]; then
    ssh-add mizzychan_prod.pem
fi

ssh $DEVENV_USER@$DEVENV_HOST sudo supervisorctl stop gunicorn
ssh $DEVENV_USER@$DEVENV_HOST sudo supervisorctl stop celery

ssh $DEVENV_USER@$DEVENV_HOST sudo chown ubuntu /var/www/gimphub -R
ssh $DEVENV_USER@$DEVENV_HOST sudo chmod 777 /var/www/gimphub -R

echo "Copying new files..."


rsync -r --info=progress2 ~/Desktop/MizzyChan/mizzychan/ ssh $DEVENV_USER@$DEVENV_HOST:/var/www/mizzychan --exclude 'config.py'

ssh $DEVENV_USER@$DEVENV_HOST sudo chown ubuntu /var/www/gimphub -R
ssh $DEVENV_USER@$DEVENV_HOST sudo chmod 777 /var/www/gimphub -R

#ssh $DEVENV_USER@$DEVENV_HOST sudo supervisorctl start gunicorn
#ssh $DEVENV_USER@$DEVENV_HOST sudo supervisorctl start celery

echo "Deploy Complete"