from relatorio_04.ProductAnalyser import ProductAnalyzer

analyzer = ProductAnalyzer("mongodb://localhost:27017", "mydb", "sales")

total_sales = analyzer.total_sales_per_day()
print("Total de vendas por dia:")
for entry in total_sales:
    print(f"Data: {entry['_id']}, Total de Vendas: {entry['total_sales']}")

produto_mais_vendido = analyzer.most_sold_product()
print("Produto mais vendido:")
print(produto_mais_vendido)


cliente_mais_comprou = analyzer.customer_with_highest_single_purchase()
print("Cliente que mais gastou em uma única compra:")
print(cliente_mais_comprou)


quantity_threshold = 1
products_above_threshold = analyzer.products_sold_above_quantity(quantity_threshold)
print(f"Produtos vendidos acima de {quantity_threshold} unidades:")
print(products_above_threshold)

analyzer.close_connection()
