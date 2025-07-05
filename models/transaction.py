import time

class Transaction:
    @staticmethod
    def create(amount, category, trans_type):
        return {
            "id": int(time.time()),
            "amount": amount,
            "category": category,
            "type": trans_type,
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
        }
