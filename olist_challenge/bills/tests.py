from django.test import TestCase
from bills.models import *
from calls.models import *
import datetime

class BillTestCase(TestCase):
    def setUp(self):
        bill = Bill.objects.create(subscriber="4899999999", period=datetime.timedelta(days=10))
        end_call = EndCall.objects.create(call_id="40", timestamp="123")
        bill_call = BillCall.objects.create(
            call= end_call,
            destination = '4899999999',
            start_date = datetime.date.today(),
            start_time = datetime.time(),
            duration = datetime.timedelta(days=10),
            price = 3.86
        )
        bill.calls.add(bill_call)

    def test_relation_is_right(self):
        bill = Bill.objects.first()
        end_call = BillCall.objects.first()
        self.assertEqual(bill.calls.first(), end_call)
