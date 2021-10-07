from scrapy.http import FormRequest
import scrapy

# starts_urls = ('')

def start_requests(self):
   return [FormRequest(formdata={"user":"pizzeriabambi@hotmail.com",
           "pass":"Santaclara123"}, "https://loyverse.com/en/login", callback=self.parse)]
def parse(self,response):
    pass