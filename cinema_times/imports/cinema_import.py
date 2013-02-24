from cinema_times.models import CinemaCompany, Cinema
import requests

class CinemaImport(object):
    def __init__(self):
        self.company_id = None
        self.company_name = None

    def create_cinema_company(self, company_name, url):
        try:
            cinema_company = CinemaCompany(
                company_name=company_name,
                company_website=url
            )
            cinema_company.save()
        except Exception:
            cinema_company = CinemaCompany.objects.get(company_name=company_name)
        return cinema_company

    def check_cinema_exists(self, company_id, cinema_id):
        cinema = Cinema.objects.get(company_cinema_id=cinema_id, company_id=company_id)
        return True if cinema else False

    @staticmethod
    def get_url(url):
        req = requests.get(url)
        return req.content
