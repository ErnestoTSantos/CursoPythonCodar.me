from django.core import mail
from django.test import TestCase
from schedule.tasks import generate_report_provider


class EmailTest(TestCase):
    def test_send_mail(self):
        generate_report_provider()

        assert mail.outbox[0].subject == "Marked -> Provider report"

    def test_receiver_email(self):
        generate_report_provider()

        assert mail.outbox[0].to[0] == "ernesto.terra2003@gmail.com"

    def test_have_attachment(self):
        generate_report_provider()

        assert mail.outbox[0].attachments

    def test_attachment_has_expected_values(self):
        generate_report_provider()

        attachments = mail.outbox[0].attachments[0]

        name, headers, type = attachments

        assert name == "report.csv"
        assert (
            headers
            == "provider,client_name,client_email,client_phone,confirmed,states\r\n"
        )
        assert type == "text/csv"
