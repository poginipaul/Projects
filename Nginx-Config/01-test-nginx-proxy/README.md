1. install nginx

2. install python prerequisites
   - sudo apt install python3-pip python3-dev build-essential libssl-dev libffi-dev python3-setuptools

3. create a virtual env
   - sudo apt install python3-venv -y

4. create a folder 
   - mkdir /home/paul/web-proj
   - cd /home/paul/web-proj

5. activate virtualenv
   - python3 -m venv web-proj-env
   - source web-proj-env/bin/activate

6. install flask and gunicorn
   - pip3 install flask gunicorn

7. create a flask app (in my case I create webserver.py)

8. test the flask app, allow port 5000
   - ufw enable
   - ufw allow 5000

9. check the flask app by running python3/python webserver.py

10. create a wsgi.py file
   - nano wsgi.py
   import the flask app to the wsgi

11. config gunicorn to create an entry point and double check if wsgi flask app can run
   - cd /home/web-proj
   - gunicorn --bind 0.0.0.0:5000 wsgi:app (bind any ip)

12. deactivate the virtualnv and create a service
   - (see webserver.service file for reference)
   - systemctl enable webserver (to start the service during boot)
   - systemctl start webserver

13. configure proxy 
   - (see web-proj file for sample config)

14. nginx -t
    nginx -s reload

15. if accessing the site gives you 502 bad gateway
    - chmod -R 0775 /home/paul/web-proj 
