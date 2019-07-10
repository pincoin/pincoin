import logging

from . import settings as blockchain_settings
from .block import Block


class Blockchain:
    logger = logging.getLogger(__name__)

    def __init__(self):
        self.chain = [self.genesis_block, ]

    def new_block(self, data, difficulty=2, nonce=0):
        block = Block(self.last_block.index + 1,
                      self.last_block.hash,
                      data,
                      difficulty=difficulty,
                      nonce=nonce)

        if block.validate(self.last_block):
            self.chain.append(block)
            return block

        return False

    @property
    def genesis_block(self):
        return Block(index=0,
                     previous_block_hash=None,
                     data=blockchain_settings.GENESIS_BLOCK_DATA,
                     difficulty=2,
                     nonce=0,
                     timestamp=blockchain_settings.GENESIS_BLOCK_TIMESTAMP)

    @property
    def last_block(self):
        return self.chain[-1]

    def validate(self, chain):
        """ Check if new candidate chain is valid

        :param chain: the new candidate chain
        :return: True if valid, False otherwise
        """
        if self.genesis_block != chain[0]:
            self.logger.error('genesis block is invalid.')
            return False

        for i in range(1, len(self.chain)):
            if not chain[i].validate(chain[i - 1]):
                self.logger.error('chain is broken.')
                return False

        return True

    def replace(self, chain):
        """ Update chain with the newer and longer chain

        :param chain: the new candidate chain
        :return: True if valid, False otherwise
        """
        if chain.validate() and len(chain) > len(self.chain):
            self.chain = chain
            return True

        return False
