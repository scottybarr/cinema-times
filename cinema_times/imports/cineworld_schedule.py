from cinema_import import CinemaImport
from cinema_times import config
from cinema_times.models import CinemaCompany, Schedule, Film, VideoType, AudioType
import xmltodict
import dateutil.parser


class CineworldSchedule(CinemaImport):
    def __init__(self):
        url = config.CINEWORLD_SYNDICATION_URL + "listings.xml"
        xml = self.get_url(url)
        self.cinema_company_id = CinemaCompany.objects.get(company_name='Cineworld').company_id
        self.sched = xmltodict.parse(xml)

    def get_sched(self):
        cinemas = self.get_all_cinemas(self.cinema_company_id)
        schedules = []

        for cinema in self.sched['cinemas']['cinema']:
            cinema_id = cinemas.get(cinema['@id'])
            for film in cinema.get('listing', {}).get('film', []):
                title = film['@title']
                edi = film['@edi']
                url = film['@url']
                rating = film['@rating']
                film_id = Film.objects.get_or_create(title=title, rating=rating)[0]
                for show in film.get('shows', {}).get('show', []):
                    try:
                        audio = show.get('@audioType', None)
                        video = show.get('@videoType', None)
                        audio = AudioType.objects.get_or_create(audio_type=audio)[0] if audio else None
                        video = VideoType.objects.get_or_create(video_type=video)[0] if video else None

                        schedules.append(Schedule(
                            film_id=film_id,
                            cinema_id=cinema_id,
                            film_internal_id=edi,
                            datetime=dateutil.parser.parse(show.get('@time', None)),
                            subtitled=True if show.get('@subtitled', False) else False,
                            video_type_id=video,
                            audio_type_id=audio,
                            booking_url=show.get('@url', ''),
                            session_type=show.get('@sessionType', None)
                        ))
                    except Exception as e:
                        pass
        Schedule.objects.bulk_create(schedules)