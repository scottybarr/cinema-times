from lxml import objectify, html
from cinema_times.models import Cinema
from cinema_import import CinemaImport


class CineworldCinemas(CinemaImport):
    def __init__(self, config):
        self.company_id = self.create_cinema_company("Cineworld", "http://www.cineworld.co.uk")
        xml = self.get_url(config.CINEWORLD_SYNDICATION_URL + "listings.xml")
        self.parse_xml(xml)

    def parse_xml(self, xml):
        root = objectify.fromstring(xml)
        for e in root.iterchildren():
            cinema_data = {
                'name': e.attrib.get('name', None),
                'phone': e.attrib.get('phone', None),
                'address': e.attrib.get('address', None),
                'id': e.attrib.get('id', None),
                'url': e.attrib.get('root', '') + e.attrib.get('url', '')
            }
            if not self.check_cinema_exists(self.company_id, cinema_data['id']):
                lat, long = self.get_coords(cinema_data['url'])
                cinema = Cinema(
                    cinema_name=cinema_data['name'],
                    company_id=self.company_id,
                    company_cinema_id=cinema_data['id'],
                    address=cinema_data['address'],
                    phone=cinema_data['phone'],
                    latitude=lat,
                    longitude=long
                )
                cinema.save()

    def get_coords(self, url):
        contents = self.get_url(url)
        contents = html.fromstring(contents)
        coords = contents.xpath("//div[contains(@class,'map')]/@data-coordinates")[0]
        return coords.split(',')
