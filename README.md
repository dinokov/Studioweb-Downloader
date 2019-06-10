# Killersites Projects Downloader
Download your projects/courses to local disk so you can watch them anytime.

I bought the "Interactive Web Developer course" package from Stefan Mischook on https://www.killersites.com .

The link to discounted package I bought: https://www.killersites.com/blog/buy-iwd-course-package-with-paypal/

I have limited internet access and wanted to have all videos from the course saved on disk so I can access them anytime.

This python project does exactly that.
It downloads all the videos from the links on the course website to a local folder.
You have to put your username and password and link to individual course in the file.
Without password the program will download only free files.

1. download file iwd-dl.py
2. download file test-logindata.py and rename it to logindata.py
3. edit username and password in logindata.py
4. in logindata.py uncoment only one URL of the page you actually want to scrape videos from

```
### This URL is the page you actually want to pull down with requests.
address = 'https://projects.studioweb.com/course/introduction-to-twitter-bootstrap'
#address = 'https://projects.studioweb.com/course/web-foundations'
#address = 'https://projects.studioweb.com/course/beginners-jquery'
```
5. run iwd-dl.py , 
it will create a new folder and start downloading videos in that folder.

