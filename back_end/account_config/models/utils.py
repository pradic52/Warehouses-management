from django.forms import ValidationError
import phonenumbers


def validate_phone_number(phone_number):
    """ Valide le numéro de téléphone en utilisant phonenumbers. """
    try:
        parsed_number = phonenumbers.parse(phone_number)
        if not phonenumbers.is_valid_number(parsed_number):
            raise ValidationError(_("Invalid phone number"))
        return True
    except phonenumbers.NumberParseException:
        raise ValidationError(_("Invalid phone number format"))