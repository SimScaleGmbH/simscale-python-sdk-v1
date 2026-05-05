from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class UserSignupRequest(SimScaleModel):
    email: str
    firstname: str
    lastname: str
    consent_terms_conditions_privacy: bool = Field(
        validation_alias="consentTermsConditionsPrivacy",
        serialization_alias="consentTermsConditionsPrivacy",
        description="I agree to the End User License Terms and the Privacy Policy",
    )
    consent_to_be_contacted: bool = Field(
        validation_alias="consentToBeContacted",
        serialization_alias="consentToBeContacted",
        description="SimScale may occasionally contact you via e-mail to present you with similar goods and services of SimScale unless you have objected to such use of your e-mail address.",
    )
