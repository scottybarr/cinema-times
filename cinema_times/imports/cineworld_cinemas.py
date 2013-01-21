import requests
from lxml import objectify
from cinema_times.models import Cinema, CinemaCompany


class CineworldImport:
    def __init__(self, config):
        self.url = config.CINEWORLD_SYNDICATION_URL + "listings.xml"
        xml = self.get_xml()
        self.parse_xml(xml)

    def get_xml(self):
        req = requests.get(self.url)
        return req.content

    def parse_xml(self, xml):
        root = objectify.fromstring(xml)
        for e in root.iterchildren():
            print e.attrib
            name = e.attrib['name']
            phone = self.try_get_attrib(e, 'phone')
            address = self.try_get_attrib(e, 'address')
            cinema_id = e.attrib['id']

    def try_get_attrib(self, e, key):
        try:
            return e.attrib[key]
        except Exception:
            return ""
