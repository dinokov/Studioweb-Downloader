#
#
###


import lxml
import requests
import bs4

address = 'https://projects.studioweb.com/course/introduction-to-twitter-bootstrap'
res = requests.get(address)
res.raise_for_status()

#iwdSoup = bs4.BeautifulSoup(res.text, features="lxml")
iwdSoup = bs4.BeautifulSoup(res.text, 'html.parser')


elems1 = iwdSoup.select('.course_link')
elems2 = iwdSoup.select('.course_link a')

#print (len(elems))
# elems[0].getText()

#numElems1 = len(elems1)
# for i in range(numElems1):
#    print (elems1[i].getText())

#numElems2 = len(elems2)
# for i in range(numElems2):
#    print(elems2[i].get('href'))

getCoursePart = requests.get(elems2[0].get('href'))
getCoursePart.raise_for_status()
coursePart = bs4.BeautifulSoup(getCoursePart.text, 'html.parser')

coursePartElemVideo = coursePart.select('source')
print(coursePartElemVideo[0].get('src'))

coursePartElemText = coursePart.select('#current_lesson a')
print(coursePartElemText[0].getText())


# <tr id="current_lesson">
#                                            <td class="course_position">1</td>
#                        <td class="course_link">
#                            <a href="https://projects.studioweb.com/course/introduction-to-twitter-bootstrap/1">Introduction</a>
#                        </td>
#                        <td class="course_length">01:13</td>
#                                                    <td class="course_status"><span class="label label-success">complete</span></td>
#                                            </tr>
#
#
