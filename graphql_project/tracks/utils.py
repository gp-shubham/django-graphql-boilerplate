import time
from graphql_project.tracks.models import *
from random import randint
from faker import Faker

fake = Faker('en_US')


class SampleData():
    def insert_user(self, count):
        starttime = time.time()
        for _ in range(0, count):
            user = User()
            user.name = fake.name()
            user.username = ".".join(user.name.lower().split(" "))
            user.email = f'{user.username}@example.com'
            user.set_password('12a34567890')
            user.save()
            print(f'Obj took {time.time() - starttime} seconds to create {_} Data')
        print(f'Total time took {time.time() - starttime} seconds to create {count} Data')

    def insert_tracks(self, count):
        starttime = time.time()
        user = User.objects.all().values_list('id', flat=True)
        for _ in range(0, count):
            track = Track.objects.create(
                posted_by_id=fake.word(ext_word_list=user),
                title=fake.sentence(),
                description=fake.paragraph(nb_sentences=10),
                url=fake.url()
            )
            track.created_at = fake.date_time_between(start_date='-1y', end_date='now', tzinfo=None)
            track.save()
            print(f'Obj took {time.time() - starttime} seconds to create {_} Data')
        print(f'Total time took {time.time() - starttime} seconds to create {count} Data')
