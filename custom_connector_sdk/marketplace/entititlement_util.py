import logging
import boto3
import uuid

LOGGER = logging.getLogger()
LOGGER.setLevel(logging.INFO)

THE_KEY_FINGERPRINT = 'aws:294406891311:AWS/Marketplace:issuer-fingerprint'
CHECKOUT_TYPE = "PROVISIONAL"
MARKETPLACE_ENTITLEMENT_NAME = 'AWS::Marketplace::Usage'


def check_entitlement(product_sku: str) -> bool:
    """Checks if the Connector subscribed from Marketplace has entitlement to use or not for an AWS account."""
    client = boto3.client('license-manager')
    try:
        res = client.checkout_license(
            ProductSKU=product_sku,
            CheckoutType=CHECKOUT_TYPE,
            KeyFingerprint=THE_KEY_FINGERPRINT,
            Entitlements=[{'Name': MARKETPLACE_ENTITLEMENT_NAME, 'Unit': 'None'}],
            ClientToken=str(uuid.uuid4())
        )
        for entitlement in res['EntitlementsAllowed']:
            if MARKETPLACE_ENTITLEMENT_NAME == entitlement['Name']:
                return True
    except Exception as e:
        LOGGER.error('Entitlement check failed with exception ' + str(e))
    return False
