#!/bin/bash
#
#       description: manages Jenkins as a service
#       processname: jenkins
#       pidfile: /var/run/jenkins.pid
#       author:mahu
#       email:mahu@royole.com

Jenkins_Home=/usr/local/jenkins
startup=$Jenkin_Home/bin/startup.sh
shutdown=$Jenkins_Home/bin/shutdown.sh

start_jenkins() {
        echo "Starting Service"
        su - jenkins -c "sh $startup"
        # Do start things here.
}

stop_jenkins() {
        echo "Stoping Service"
        su - jenkins -c "sh $shutdown"
        # Do stop things here
}

restart_jenkins() {
        echo "Restarting Service..."
        stop_jenkins
        start_jenkins
}

status_jenkins() {
        # Check for any other procecss containing jenkins.war
        # This could be improved upon (see script below)
        numproc=$(ps -ef|grep [j]enkins.war|wc-l)
        if[$numproc -ne 0]; then
                echo "Jenkins is running..."
        else
                echo "Jenkins is NOT running..."
}


case "$1" in

        start)
        start_jenkins
        ;;

        stop)
        stop_jenkins
        ;;

        restart)
        start_jenkins
        stop_jenkins
        ;;

        status)
        status_jenkins
        ;;

        *)
        echo "jenkins usage {start|restart|stop|status}" 

