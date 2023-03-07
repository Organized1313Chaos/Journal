### guicorn, nginx

Link: [digitalocean](https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu-20-04)

Why??
- development to production
- nginx (security and high performance connection handling mechanism) `-->` reverse proxy to Gunicorn
- securing traffic to the server using SSL/TLS

**gunicorn installation**
- create a virtual environment
- pip install django gunicorn psycopg2-binary

- gunicorn to load the project's WSGI module
- `gunicorn --bind 0.0.0.0:8000 myproject.wsgi`
- gunicorn socket will listen for connections

**nginx installation**
- sudo apt-get install gunicorn nginx
- Test your Nginx configuration for syntax errors by typing: `sudo nginx -t`

- If no errors are reported, go ahead and restart Nginx by typing: `sudo systemctl restart nginx`

Finally, we need to open up our firewall to normal traffic on port 80. Since we no longer need access to the development server, we can remove the rule to open port 8000 as well:
- `sudo ufw delete allow 8000`
- `sudo ufw allow 'Nginx Full'`

- `Check the Nginx process logs by typing:` `sudo journalctl -u nginx`
- `Check the Nginx access logs by typing:` `sudo less /var/log/nginx/access.log`
- `Check the Nginx error logs by typing:` `sudo less /var/log/nginx/error.log`
- `Check the Gunicorn application logs by typing:` `sudo journalctl -u gunicorn`
- `Check the Gunicorn socket logs by typing:` `sudo journalctl -u gunicorn.socket`


<br>

- If you update your Django application, you can restart the Gunicorn process to pick up the changes by typing:

    `sudo systemctl restart gunicorn`

- If you change Gunicorn socket or service files, reload the daemon and restart the process by typing:

    
    `sudo systemctl daemon-reload`
    
    
    `sudo systemctl restart gunicorn.socket gunicorn.service`
    
- If you change the Nginx server block configuration, test the configuration and then Nginx by typing:

    `sudo nginx -t && sudo systemctl restart nginx`


- These commands are helpful for picking up changes as you adjust your configuration.

**CHAT-GPT**

- Test Gunicorn: Start Gunicorn and test that it is working by running the command 
`gunicorn myproject.wsgi`

- Configure Gunicorn: Create a configuration file for Gunicorn to specify the number of worker processes and other settings. 
Here is an example configuration file:

```
    bind = "127.0.0.1:8000"
    workers = 3
    errorlog = '/var/log/gunicorn/error.log'
    accesslog = '/var/log/gunicorn/access.log'
```

- Configure Nginx: Create a configuration file for Nginx to act as a reverse proxy for Gunicorn.
Here is an example configuration file:
    ```
    server {
        listen 80;
        server_name example.com;

        location / {
            proxy_pass http://127.0.0.1:8000;
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
        }
    }
    ```
- Step 7: Restart Nginx and Gunicorn

- To apply the changes, restart Nginx and Gunicorn by running the following commands:
    ```
    sudo systemctl restart nginx
    sudo systemctl restart gunicorn
    ```

---
**Step by Step Guide**

- Step 1: Install Gunicorn and Nginx on your server

    If you are using Ubuntu or Debian, you can use the following command to install Gunicorn and Nginx:

    `sudo apt-get install gunicorn nginx`

- Step 2: Create a virtual environment

To create a virtual environment using virtualenv, run the following command:

    `source myenv/bin/activate`
- Step 3: Install Django and other dependencies

    `pip install -r requirements.txt`

- Step 4: Test Gunicorn

    To start Gunicorn, navigate to your Django project's root directory and run the following command:

        `gunicorn myproject.wsgi`
    This should start Gunicorn, and you should be able to access your Django application at    `http://localhost:8000` in your web browser.

- Step 5: Configure Gunicorn

    To configure Gunicorn, create a configuration file in your Django project's root directory, for example `gunicorn_config.py`. Here is an example configuration file:

    ```
    bind = "127.0.0.1:8000"
    workers = 3
    errorlog = '/var/log/gunicorn/error.log'
    accesslog = '/var/log/gunicorn/access.log'
    ```
    This configuration file specifies that Gunicorn should bind to `127.0.0.1:8000`, use three worker processes, and write error and access logs to `/var/log/gunicorn/error.log` and `/var/log/gunicorn/access.log` respectively.

- Step 6: Configure Nginx

    To configure Nginx, create a new configuration file in the `/etc/nginx/sites-available/ ` directory. You can name the file whatever you want, for example myproject. Here is an example configuration file:

    ```
    server {
        listen 80;
        server_name example.com;

        location / {
            proxy_pass http://127.0.0.1:8000;
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
        }
    }
    ```
    This configuration file specifies that Nginx should listen on port 80, use `example.com` as the server name, and proxy requests to `http://127.0.0.1:8000` where Gunicorn is running.

    To enable the new configuration file, create a symbolic link in the `/etc/nginx/sites-enabled/` directory:

    `sudo ln -s /etc/nginx/sites-available/myproject /etc/nginx/sites-enabled/`

- Step 7: Restart Nginx and Gunicorn
  
    To apply the changes, restart Nginx and Gunicorn by running the following commands:

    ```
    sudo systemctl restart nginx
    sudo systemctl restart gunicorn
    ```

    Now your Django project should be accessible via Nginx, 
    and Gunicorn should be serving the Django application. 
    You can test it by visiting your server's IP address or domain name in a web browser.

---
- nginx logs error:
    `sudo journalctl -u nginx`

---


- bindings 
    `gunicorn --bind 0.0.0.0:8000 myproject.wsgi`