dspace-utils
============

http://royopa.github.io/dspace-utils

Various examples of code and scripts to manage DSpace repositories

##See log tomcat7

```bash
$ tail -f /var/lib/tomcat7/logs/catalina.out
```

##Change parameters JAVA_OPTS

In **/etc/default/tomcat7**:

```config
JAVA_OPTS              -Xmx1024 -Xms512m -XX:MaxPermSize=512m
```

##Change owner dspace folder recursively to tomcat7

```bash
$ sudo chown tomcat:7:tomcat7 /dspace -R
```

##Find file by name

```bash
$ sudo find / -name "nameToFind"
```

