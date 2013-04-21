from lxml import html
from cinema_times.models import Cinema
from cinema_import import CinemaImport
import xmltodict


class CineworldCinemas(CinemaImport):
    def __init__(self, config):
        self.company_id = self.create_cinema_company("Cineworld", "http://www.cineworld.co.uk")
        self.xml = self.get_url(config.CINEWORLD_SYNDICATION_URL + "cinemas.xml")

    def parse_cinemas(self):
        all_cinemas = []
        root = xmltodict.parse(self.xml)
        for cinema in root.get('cinemas', {}).get('cinema', []):
            cinema_data = {
                'name': cinema.get('@name', None),
                'phone': cinema.get('@phone', None),
                'address': self.build_address(cinema.get('@address', None), cinema.get('@postcode', None)),
                'id': cinema.get('@id', None),
                'url': cinema.get('@root', '') + cinema.get('@url', '')
            }
            if not self.check_cinema_exists(self.company_id, cinema_data['id']):
                lat, long = self.get_coords(cinema_data['url'])
                all_cinemas.append(Cinema(
                    cinema_name=cinema_data['name'],
                    company=self.company_id,
                    company_cinema_id=cinema_data['id'],
                    address=cinema_data['address'],
                    phone=cinema_data['phone'],
                    latitude=lat,
                    longitude=long
                ))
        Cinema.objects.bulk_create(all_cinemas)
        return {}

    @staticmethod
    def build_address(add, postcode):
        if postcode:
            return "{add}, {postcode}".format(**locals())
        return add

    def get_coords(self, url):
        contents = self.get_url(url)
        contents = html.fromstring(contents)
        coords = contents.xpath("//div[contains(@class,'map')]/@data-coordinates")[0]
        return coords.split(',')
