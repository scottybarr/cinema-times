from lxml import objectify, html
from cinema_times.models import Cinema
from cinema_import import CinemaImport


class CineworldImport(CinemaImport):
    def __init__(self, config):
        self.url = config.CINEWORLD_SYNDICATION_URL + "listings.xml"
        self.company_id = self.create_cinema_company("Cineworld", "http://www.cineworld.co.uk")
        xml = self.get_url(self.url)
        self.parse_xml(xml)


    def parse_xml(self, xml):
        root = objectify.fromstring(xml)
        for e in root.iterchildren():
            name = e.attrib['name']
            phone = self.try_get_attrib(e, 'phone')
            address = self.try_get_attrib(e, 'address')
            cinema_id = e.attrib['id']
            url = e.attrib['root'] + e.attrib['url']
            if not self.check_cinema_exists(self.company_id, cinema_id):
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

    @staticmethod
    def get_coords(url):
        contents = get_url(url)
        contents = html.fromstring(contents)
        coords = contents.xpath("//div[contains(@class,'map')]/@data-coordinates")[0]
        return coords.split(',')
