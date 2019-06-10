#
#
###


import lxml
import requests
import bs4
import logindata

# This URL will be the URL that your login form points to with the "action" tag.
#loginAddress = 'https://projects.studioweb.com/login'
# This URL is the page you actually want to pull down with requests.
#address = 'https://projects.studioweb.com/course/introduction-to-twitter-bootstrap'
#payload = {'email': 'myemail@gmail.com', 'password': 'verylongpassword'}


with requests.Session() as session:
    post = session.post(logindata.loginAddress, data=logindata.payload)
    res = session.get(logindata.address)
    res.raise_for_status()


print('\n\n\n')
print('\n\n\n')
iwdSoup = bs4.BeautifulSoup(res.text, 'html.parser')
elems2 = iwdSoup.select('.course_link a')

numElems2 = len(elems2)
#getCoursePart = []
#coursePart = []
coursePartElemVideo = []

for i in range(numElems2):
    print('element number: ', i)
    linkElems2 = elems2[i].get('href')
    print('part:', linkElems2)
    vmes = session.get(linkElems2)
    vmes.raise_for_status()
    vmes = bs4.BeautifulSoup(vmes.text, 'html.parser')
    vmes = vmes.select('source')
    coursePartElemVideo.append(vmes[0].get('src'))
    print('video:', coursePartElemVideo[i])
    print('\n')
