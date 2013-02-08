import requests
from lxml import objectify, html
from cinema_times.models import Cinema, CinemaCompany


class CineworldImport:
    def __init__(self, config):
        self.company_name = "Cineworld"
        self.url = config.CINEWORLD_SYNDICATION_URL + "listings.xml"
        self.company_id = self.create_cinema_company()
        xml = self.get_xml()
        self.parse_xml(xml)

    def create_cinema_company(self):
        try:
            cinema_company = CinemaCompany(
                company_name=self.company_name,
                company_website="http://www.cineworld.co.uk"
            )
            cinema_company.save()
        except Exception as e:
            cinema_company = CinemaCompany.objects.get(company_name=self.company_name)
        return cinema_company

    def get_xml(self):
        req = requests.get(self.url)
        return req.content

    def parse_xml(self, xml):
        root = objectify.fromstring(xml)
        for e in root.iterchildren():
            name = e.attrib['name']
            phone = self.try_get_attrib(e, 'phone')
            address = self.try_get_attrib(e, 'address')
            cinema_id = e.attrib['id']
            url = e.attrib['root'] + e.attrib['url']
            if not self.check_cinema_exists(cinema_id):
                lat, long = self.get_coords(url)
                c = Cinema(
                    cinema_name=name,
                    company_id=self.company_id,
                    company_cinema_id=cinema_id,
                    address=address,
                    phone="",
                    latitude=lat,
                    longitude=long
                )
                c.save()

    def try_get_attrib(self, e, key):
        try:
            return e.attrib[key]
        except Exception:
            return ""

    def get_coords(self, url):
        contents = self.load_cinema_page(url)
        contents = html.fromstring(contents)
        coords = contents.xpath("//div[contains(@class,'map')]/@data-coordinates")[0]
        return coords.split(',')

    def load_cinema_page(self, url):
       req = requests.get(url)
       return req.content

    def check_cinema_exists(self, cinema_id):
        cinema = Cinema.objects.get(company_cinema_id=cinema_id, company_id=self.company_id)
        return True if cinema else False
