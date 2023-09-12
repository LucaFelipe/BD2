import pymongo

class ProductAnalyzer:
    def __init__(self, db_url, db_name, collection_name):
        self.client = pymongo.MongoClient(db_url)
        self.db = self.client[db_name]
        self.collection = self.db[collection_name]

    def total_sales_per_day(self):
        pipeline = [
            {"$group": {"_id": {"$dateToString": {"format": "%Y-%m-%d", "date": "$date"}}, "total_sales": {"$sum": "$quantity"}}},
            {"$sort": {"_id": 1}}
        ]
        result = list(self.collection.aggregate(pipeline))
        return result

    def most_sold_product(self):
        pipeline = [
            {"$group": {"_id": "$product_id", "total_sold": {"$sum": "$quantity"}}},
            {"$sort": {"total_sold": -1}},
            {"$limit": 1}
        ]
        result = list(self.collection.aggregate(pipeline))
        if result:
            most_sold_product_id = result[0]["_id"]
            return self.collection.find_one({"product_id": most_sold_product_id})
        else:
            return None

    def customer_with_highest_single_purchase(self):
        pipeline = [
            {"$group": {"_id": "$customer_id", "total_purchase": {"$sum": {"$multiply": ["$quantity", "$price"]}}}},
            {"$sort": {"total_purchase": -1}},
            {"$limit": 1}
        ]
        result = list(self.collection.aggregate(pipeline))
        if result:
            customer_id = result[0]["_id"]
            return self.collection.find_one({"customer_id": customer_id})
        else:
            return None

    def products_sold_above_quantity(self, quantity_threshold):
        pipeline = [
            {"$match": {"quantity": {"$gt": quantity_threshold}}},
            {"$group": {"_id": "$product_id"}},
            {"$project": {"_id": 0, "product_id": 1}}
        ]
        result = list(self.collection.aggregate(pipeline))
        product_ids = [record["product_id"] for record in result]
        return product_ids

    def close_connection(self):
        self.client.close()
