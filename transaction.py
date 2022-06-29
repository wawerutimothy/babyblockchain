class Transaction:
    def __init__(self, version, txIn, txOut, lockTime):
        self.version = version
        self.txIn = txIn
        self.txOut = txOut
        self.lockTime = lockTime


class TxIn:
    def __init__(self, prev_tx, prev_index, scriptSig=None):
        self.prev_tx = prev_tx
        self.prev_index = prev_index
        if scriptSig is None:
            self.scriptSig = Script()
        else:
            self.scriptSig = scriptSig


class Script:
    def __init__(self, cmd=None):
        if cmd is None:
            self.cmd = []
        else:
            self.cmd = cmd


class TxOut:
    def __init__(self, amount, scriptPubkey):
        self.amount = amount
        self.scriptPubKey = scriptPubkey

