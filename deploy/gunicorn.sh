#!/bin/bash

NAME="Vital"
DJANGODIR=$(dirname $(cd `dirname $0` && pwd))
SOCKFILE=/tmp/gunicorn-vital.sock
LOGDIR=${DJANGODIR}/logs/gunicorn.log
USER=ti9r
GROUP=ti9r
NUM_WORKERS=5
DJANGO_WSGI_MODULE=Vital.wsgi

rm -frv $SOCKFILE

echo $DJANGODIR

cd $DJANGODIR

exec ${DJANGODIR}/venv/bin/gunicorn ${DJANGO_WSGI_MODULE}:application \
  --name $NAME \
  --workers $NUM_WORKERS \
  --user=$USER --group=$GROUP \
  --bind=unix:$SOCKFILE \
  --log-level=debug \
  --log-file=$LOGDIR
