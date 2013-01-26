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
            self.cinema_company = CinemaCompany(
                company_name=self.company_name,
                company_website="http://www.cineworld.co.uk"
            )
            self.cinema_company.save()
        except Exception as e:
            self.cinema_company = CinemaCompany.objects.filter(company_name=self.company_name)
        return self.cinema_company.company_id

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
            lat, long = self.get_coords(url)

    def try_get_attrib(self, e, key):
        try:
            return e.attrib[key]
        except Exception:
            return ""

    def get_coords(self, url):
        # Check DB to see if we have coords already
        contents = self.load_cinema_page(url)
        coords = contents.xpath("//div[contains(@class,'map')]/@data-coordinates")[0]
        return coords.split(',')

    def load_cinema_page(self, url):
        req = requests.get(url)
        return html.fromstring(req.content)
