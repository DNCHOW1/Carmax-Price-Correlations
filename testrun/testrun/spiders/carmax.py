import scrapy

base = "https://www.carmax.com/cars/api/search/run?uri=/cars/all&skip={}&take=100&zipCode=75201&radius=90&shipping=0&sort=20&scoringProfile=BestMatchScoreVariant3&visitorID=b0496ce4-1fa2-4150-a6c2-c1476f696025"

class CarmaxSpider(scrapy.Spider):
    name = 'carmax'
    allowed_domains = ['carmax.com']
    def start_requests(self):
        for i in range(400):
            yield scrapy.Request(url=base.format(i*100), callback=self.parse)
        

    def parse(self, response):
        for carInfo in response.json()["items"]:
            try:
                numTypes = len(carInfo["types"])
                numFeatures = len(carInfo["features"])
                yield {
                    'make': carInfo["make"],
                    'model': carInfo["model"],
                    'year': carInfo["year"],
                    'driveTrain': carInfo["driveTrain"],
                    "cylinders": carInfo["cylinders"],
                    "engineTorque": carInfo["engineTorque"],
                    "engineType": carInfo["engineType"],
                    "interiorColor": carInfo["interiorColor"],
                    "exteriorColor": carInfo["exteriorColor"],
                    "horsepower": carInfo["horsepower"],
                    "mileage": carInfo["mileage"],
                    "mpgHighway": carInfo["mpgHighway"],
                    "mpgCity": carInfo["mpgCity"],
                    "state": carInfo["state"],
                    "transmission": carInfo["transmission"],
                    "vehicleSize": carInfo["vehicleSize"],
                    'basePrice': carInfo["basePrice"],
                    "body": carInfo["body"],
                    "features": numFeatures,
                    "types": numTypes,
                }
            except:
                yield {"make": None}
