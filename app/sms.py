import requests
from django.conf import settings


ARKESEL_SMS_URL = "https://sms.arkesel.com/api/v2/sms/send"


def send_booking_sms(appointment):

    print("\n==============================")
    print("STARTING ARKESEL SMS")
    print("==============================")

    api_key = getattr(settings, "ARKESEL_API_KEY", )
    sender_id = getattr(settings, "ARKESEL_SENDER_ID", )
    owner_phone = getattr(settings, "SALON_OWNER_PHONE", )

    print("API KEY FOUND:", bool(api_key))
    print("SENDER ID:", sender_id)
    print("OWNER PHONE:", owner_phone)

    if not api_key:
        print("ERROR: ARKESEL_API_KEY is missing.")
        return False, "Arkesel API key is missing."

    if not owner_phone:
        print("ERROR: SALON_OWNER_PHONE is missing.")
        return False, "Salon owner's phone number is missing."

    # Clean phone number
    owner_phone = "".join(
        character
        for character in str(owner_phone)
        if character.isdigit()
    )

    print("CLEANED OWNER PHONE:", owner_phone)

    if len(owner_phone) < 10:
        print("ERROR: Invalid phone number.")
        return False, "Invalid salon owner's phone number."

    # Date
    appointment_date = appointment.appointment_date.strftime(
        "%d %B %Y"
    )

    # Time
    if appointment.appointment_time:
        appointment_time = appointment.appointment_time.strftime(
            "%I:%M %p"
        )
    else:
        appointment_time = "Not specified"

    # SMS message
    message = (
        "NEW SALON APPOINTMENT\n"
        f"Customer: {appointment.full_name}\n"
        f"Email: {appointment.email or 'Not provided'}\n\n"
        f"Phone: {appointment.phone}\n"
        f"Service: {appointment.service}\n"
        f"Date: {appointment_date}\n"
        f"Time: {appointment_time}\n"
        f"Message: {appointment.message or 'No message'}\n\n"
        f"Status: {appointment.status}\n"
        "Please check your salon dashboard."
    )

    print("\nSMS MESSAGE:")
    print(message)

    headers = {
        "api-key": api_key,
        "Content-Type": "application/json",
        "Accept": "application/json",
    }

    data = {
        "sender": sender_id,
        "message": message,
        "recipients": [
            owner_phone
        ],
    }

    print("\nSENDING REQUEST TO ARKESEL...")
    print("URL:", ARKESEL_SMS_URL)
    print("RECIPIENT:", owner_phone)

    try:

        response = requests.post(
            ARKESEL_SMS_URL,
            headers=headers,
            json=data,
            timeout=30,
        )

        print("\n==============================")
        print("ARKESEL RESPONSE")
        print("==============================")

        print("HTTP STATUS:", response.status_code)
        print("RESPONSE:", response.text)

        try:
            result = response.json()
        except ValueError:

            print("ERROR: Arkesel did not return JSON.")

            return False, response.text

        # Don't rely only on response.ok.
        # Print the complete response so we can see Arkesel's result.
        if response.ok:

            print("REQUEST ACCEPTED BY ARKESEL.")

            return True, result

        print("ARKESEL REQUEST FAILED.")

        return False, result

    except requests.RequestException as error:

        print("\n==============================")
        print("CONNECTION ERROR")
        print("==============================")

        print(error)

        return False, str(error)