from ProductAnalyzer import ProductAnalyzer

def main():
    # Conecte-se ao banco de dados MongoDB
    analyzer = ProductAnalyzer("mongodb://localhost:27017", "mydb", "sales")

    # Exemplo 1: Total de vendas por dia
    total_sales = analyzer.total_sales_per_day()
    print("Total de vendas por dia:")
    for entry in total_sales:
        print(f"Data: {entry['_id']}, Total de Vendas: {entry['total_sales']}")

    # Exemplo 2: Produto mais vendido
    most_sold_product = analyzer.most_sold_product()
    print("Produto mais vendido:")
    print(most_sold_product)

    # Exemplo 3: Cliente que mais gastou em uma única compra
    customer_highest_purchase = analyzer.customer_with_highest_single_purchase()
    print("Cliente que mais gastou em uma única compra:")
    print(customer_highest_purchase)

    # Exemplo 4: Produtos vendidos acima de uma quantidade específica
    quantity_threshold = 1
    products_above_threshold = analyzer.products_sold_above_quantity(quantity_threshold)
    print(f"Produtos vendidos acima de {quantity_threshold} unidades:")
    print(products_above_threshold)

    # Feche a conexão com o MongoDB quando terminar
    analyzer.close_connection()

if __name__ == "__main__":
    main()
