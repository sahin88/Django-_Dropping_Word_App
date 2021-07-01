from django.test import TestCase, Client
from django.urls import  reverse, resolve
from UploadApp.views import  uploadForm, saveUpload,reOrder
from UploadApp.models import Document
from django.contrib.staticfiles.testing import StaticLiveServerTestCase

# class TestFunctions(StaticLiveServerTestCase):


#     def SetUP(self):
#         self.driver = webdriver.Chrome()

#     def get_live_server_url(self):
#         self.driver.get(self.get_live_server_url)

class TestUrl(TestCase):
    def test_list_url_is_resolved(self):
        url=reverse('upload')
        self.assertEquals(resolve(url).func,uploadForm)


    def test_list_url_save_upload_resolved(self):
        url=reverse('save_upload')
        self.assertEquals(resolve(url).func,saveUpload)


    def test_list_url_re_order_resolved(self):
        url=reverse('re_order' ,kwargs={'pk':1})
        self.assertEquals(resolve(url).func,reOrder)

    def  test_project_get_list_GET(self):
        client=Client()
        response=client.get(reverse('upload'))
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,  'uploadForm.html')

    # def  test_project_download_template_GET(self):
    #     client=Client()
    #     response=client.get(reverse('save_upload'))
    #     self.assertEquals(response.status_code,200)
    #     self.assertTemplateUsed(response,  'uploadForm.html')

       

    def test_document_model(self):
        new_doc = Document.objects.create(keywords= "John Doe", docfile = 'python.pdf')
        self.assertEquals(new_doc.keywords,"John Doe")

