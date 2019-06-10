
import os
import lxml
import requests
import bs4
# this file logindata.py contains loginAddress, address and payload variables
import logindata
# you must create this file yourself
# if you dont want extra file, you can uncoment and modify those variables bellow
#
# This URL will be the URL that your login form points to with the "action" tag.
# loginAddress = 'https://projects.studioweb.com/login'
# This URL is the page you actually want to pull down with requests.
# address = 'https://projects.studioweb.com/course/introduction-to-twitter-bootstrap'
# payload = {'email': 'myemail@gmail.com', 'password': 'verylongpassword'}


with requests.Session() as session:
    post = session.post(logindata.loginAddress, data=logindata.payload)
    res = session.get(logindata.address)
    res.raise_for_status()


iwdSoup = bs4.BeautifulSoup(res.text, 'html.parser')
elems2 = iwdSoup.select('.course_link a')
videoFileName = iwdSoup.title.string           # get the webpage Title
videoFileName = videoFileName.split("|", 1)[0]  # keep the first part
print('Course name: ', videoFileName)
videoFileName = videoFileName.replace(" ", "")  # remove spaces


numElems2 = len(elems2)
coursePartElemVideo = []
#os.makedirs('videos', exist_ok=True)
folderName = videoFileName
os.makedirs(folderName, exist_ok=True)  # create folder for videos

for i in range(numElems2):
    print()
#   print('element number: ', i+1)
    linkElems2 = elems2[i].get('href')
    print('Course lesson:', linkElems2)
    vmes = session.get(linkElems2)
    vmes.raise_for_status()
    vmes = bs4.BeautifulSoup(vmes.text, 'html.parser')
    vmes = vmes.select('source[src]')
    coursePartElemVideo.append(vmes[0].get('src'))
    videoUrl = coursePartElemVideo[i]
#   print('Video of this lesson:', videoUrl)

    # Download the video
    # leave everything after '?' in the url otherwise download fails
    res = requests.get(videoUrl)
    res.raise_for_status()

    # Save the video to folder./videos in the current directory
    # use Title for filename
    # add numbering and filename extension
    tmpVideoFileName = videoFileName + '-' + \
        str(i+1) + '.mp4'
    tmpVideoFileName = os.path.join(folderName, tmpVideoFileName)
    print('Downloading video to: %s' % (tmpVideoFileName))
    print('#Downloading ', end='')
    videoFile = open(tmpVideoFileName, 'wb')
    for chunk in res.iter_content(100000):
        print('=', end='')
        videoFile.write(chunk)
    videoFile.close()
    print(' Finished', end='\n')

print('\n' + '----------- ALL DONE -----------' + '\n')
