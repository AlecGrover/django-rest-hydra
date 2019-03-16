from django.core.management.base import BaseCommand, CommandError
from hydra_python_core import doc_maker
from django.conf import settings

class Command(BaseCommand):
    help = "Generates apidoc object and inserts all classes and properties "

    def add_arguments(self, parser):
        # Optional argument to specify doc path
        parser.add_argument('--path', nargs='+', type=str)

        def handle(self, *args, **options):

            hydra_settings = settings.REST_HDYRA

            PORT = hydra_settings["PORT"]
            API_NAME = hydra_settings["API_NAME"]
            ENTRY_POINT = hydra_settings["ENTRY_POINT"]
            HYDRUS_SERVER_URL = hydra_settings["HYDRUS_SERVER_URL"]

            if options["path"]:
                # Load file from the specified path
                pass
            else:
                # Load the example file
                pass

            apidoc = doc_maker.create_doc(APIDOC_OBJ, HYDRUS_SERVER_URL, API_NAME)
            classes = doc_parse.get_classes(apidoc.generate())
            # Get all the properties from the classes
            properties = doc_parse.get_all_properties(classes)
            # Insert them into the database
            doc_parse.insert_classes(classes, session)
            doc_parse.insert_properties(properties, session)
