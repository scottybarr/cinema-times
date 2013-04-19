from cinema_times.models import CinemaCompany, Cinema, Film, VideoType, AudioType
from django.core.exceptions import ObjectDoesNotExist
import requests

class CinemaImport(object):
    def __init__(self):
        self.company_id = None
        self.company_name = None

    def create_cinema_company(self, company_name, url):
        try:
            return CinemaCompany.objects.get(company_name=company_name)
        except Exception:
            cinema_company = CinemaCompany(
                company_name=company_name,
                company_website=url
            )
            cinema_company.save()
        return cinema_company

    def check_cinema_exists(self, company_id, cinema_id):
        try:
            cinema = Cinema.objects.get(company_cinema_id=cinema_id, company_id=company_id)
            return True if cinema else False
        except ObjectDoesNotExist:
            return False

    def get_all_cinemas(self, company_id):
        return Cinema.objects.filter(company_id=company_id)

    def get_all_films(self, title):
        return Film.objects.filter(title=title)

    def get_all_video_types(self, video_type):
        return VideoType.objects.filter(video_type=video_type)

    def get_all_audio_types(self, audio_type):
        return AudioType.objects.filter(video_type=audio_type)

    @staticmethod
    def get_url(url):
        req = requests.get(url)
        return req.content
