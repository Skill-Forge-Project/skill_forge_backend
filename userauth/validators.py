import re
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _

class CustomPasswordValidator:
    def validate(self, password, user=None):

        if len(password) < 8:
            raise ValidationError(_("Password must be at least 8 characters long."))

        elif not re.search(r"[A-Z]", password):
            raise ValidationError(_("Password must contain at least one uppercase letter."))

        elif not re.search(r"[a-z]", password):
            raise ValidationError(_("Password must contain at least one lowercase letter."))

        elif not re.search(r"\d", password):
            raise ValidationError(_("Password must contain at least one digit."))


