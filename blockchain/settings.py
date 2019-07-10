from django.conf import settings

GENESIS_BLOCK_DATA = getattr(settings, 'GENESIS_BLOCK_DATA', 'This is a genesis block.')
GENESIS_BLOCK_TIMESTAMP = getattr(settings, 'GENESIS_BLOCK_TIMESTAMP', 1562132041)
