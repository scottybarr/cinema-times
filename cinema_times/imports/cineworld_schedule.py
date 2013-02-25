from cinema_times.models import Film, Schedule
from cinema_import import CinemaImport
from cinema_times import config
from lxml import objectify

class CineworldSchedule(CinemaImport):
    def __init__(self):
        url = config.CINEWORLD_SYNDICATION_URL + "listings.xml"
        url = "http://localhost/~scott/cache/listings.xml"
        xml = self.get_url(url)
        self.parse_xml(xml)

    def parse_xml(self, xml):
        root = objectify.fromstring(xml)
        for cinema in root.iterchildren():
            cinema_id = cinema.attrib.get('id', None)
            for listing in cinema.iterchildren():
                for film in listing.iterchildren():
                    title = film.attrib.get('title', None)
                    rating = film.attrib.get('rating', None)
                    film_url = film.attrib.get('url', '')
                    edi = film.attrib.get('edi', None)
                    for shows in film.iterchildren():
                        for show in shows.iterchildren():
                            time = show.get('time', None)
                            show_url = show.get('url', '')
                            video_type = show.get('videoType', None)
                            audio_type = show.get('audio_type', None)
                            subtitled = show.get('subtitled', None)
                            session_type = show.get('sessionType', None)
                            print cinema_id, title, rating, film_url, edi, time, show_url, video_type
