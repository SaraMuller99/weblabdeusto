# Installation 

In this section we will be following the WebLab documentation, but taking care in the particularities due to the use of Python2.7 in a much more modern system.

*In order to simplify the information given below, the bash commands will be show using a $ before*

## Obtaining WebLab-Deusto
 
We will download it from github using git, which is the recommended way according to WebLab because that allows you to upgrade WebLab-Deusto automatically in the future, and even contribute easily..

### Installing the requirements 

First of all we will install a few packages necessaries to run weblab

#### 1. Install Python 2.7: 

Python 2.7 must be installed, the OS installed in the Raspberry Pi 400 is Raspbian Bullseye which is pretty new, so the default python is 3.8 
 

#### 2. Install setuptools

    $ sudo apt-get install python-pip in Ubuntu/Debian 

#### 3. Install virtualenv and virtualenvwrapper. 

To be sure that you are using Python2.7 yo can do 

    $ python2.7 -m pip install virtualenv virtualenvwrapper 

To check if the installation was correct we do: 
 
    $ pip --version 
    pip 20.3.4 from /home/sara/.local/lib/python2.7/site-packages/pip (python 2.7) 

    $ virtualenv --version 
    WARNING: The script virtualenv is installed in '/home/sara/.local/bin' which is not on PATH.
    Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.

    $ mkvirtualenv --version 
    mkvirtualenv command not found 

At this point we will see that virtualenv and mkvitualenv are malfunctioning this is because we need to modify the `bashrc` file by writting at the end of it this:

    export PATH="$HOME/.local/bin:$PATH"
    export WORKON_HOME=$HOME/.virtualenvs
    export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python2.7
    source /home/sara/.local/bin/virtualenvwrapper.sh

Now is we execute the command before them will show:
 
    $ pip --version 
    pip 20.3.4 from /home/sara/.local/lib/python2.7/site-packages/pip (python 2.7) 

    $ virtualenv --version 
    virtualenv 20.15.1 from /home/sara/.local/lib/python2.7/site-packages/virtualenv/__init__.pyc 

    $ mkvirtualenv --version 
    virtualenv 20.15.1 from /home/sara/.local/lib/python2.7/site-packages/virtualenv/__init__.pyc
### Installing WebLab-Deusto 

Now we have to create a virtualenv, this is where we are going to work from now on: 

    $ cd WHEREVER-IS-WEBLAB 

To create the virtualenv we have to specify that Python2.7 must be used: 

    $ mkvirtualenv --python=/usr/bin/python2.7 weblab 

And we will see that we are on the virtualenv: 

    (weblab) user@machine $ 

Now we make sure that we're running the latest versions of setuptools and pip: 

    (weblab) $ pip install --upgrade setuptools 
    (weblab) $ pip install --upgrade pip 

And then, we install WebLab-Deusto: 

    $ python setup.py install 
    [...] 
    Finished processing dependencies for weblabdeusto==5.0 

Once the process is over, we test the installation by running: 

    $ weblab-admin --version 
    5.0 - 1ac2e2b03048cf89c8df36c838130212f4ac63d3 (Sunday, October 18, 2015) 

From now on every time we use a new terminal, we will have to specify the virtualenv where we want to work, in this case 

    $ workon weblab  

## Further Steps

Now we should install some external components. According to the official WebLab-Documentation there's two different ways to do the backend scheduling: MySQL and Redis. Due to the information given followed by the fact that finding a MySQL functional library have been almost inpossible, Redis is the backend for scheduling chosen. To install them we should:

    $ sudo apt-get install apache2  redis-server 

According to our objetives PHP is not necessary because we aren't going to implement external systems bases in PHP as Moodle, so `mpm_worker` will be use. If PHP where necessary, it can be installed in the future. This package is not available anymore so is necessary to do it using the new modular way: 

    $ sudo apt-get install apache2 
    $ sudo a2dismod mpm_prefork 
    $ sudo a2dismod mpm_event 
    $ sudo a2enmod mpm_worker 
    $ sudo systemctl restart apache2  

We have to take into account that redis performs all the operations in memory but from time to time it stores everything in disk, adding latency. It is recommended to avoid this. In the `/etc/redis/redis`.conf file, comment the following lines: 

    #save 900 1 
    #save 300 10 
    #save 60 10000 

Now we should install some native libraries that makes the system works more efficiently:

    # Python 
    $ sudo apt-get install build-essential python-dev 
    # LDAP 
    $ sudo apt-get install libldap2-dev 
    # SASL, SSL for supporting LDAP 
    $ sudo apt-get install libsasl2-dev libsasl2-dev libssl-dev 
    # XML libraries for validating the configuration files 
    $ sudo apt-get install libxml2-dev libxslt1-dev 
    # Avoid problems with freetype: 
    $ sudo ln -s /usr/include/freetype2 /usr/include/freetyp

Once installed is possible to install more optimized python libraries, but before this we're going to modify the `requirements_suggested.txt` by commenting the lines related with MySQL and Numpy, then we do:

    $ cd weblab/server/src
    $ pip install -r requirements_suggested.txt

