from datetime import datetime
from factory import DjangoModelFactory, lazy_attribute, Sequence
from guestboard.models import Posting


class PostingFactory(DjangoModelFactory):
    class Meta:
        model = Posting

    name = Sequence(lambda n: "name #{seq}".format(seq=n))
    message = Sequence(lambda n: "message #{seq}".format(seq=n))
    created_at = lazy_attribute(lambda o: datetime.now())
