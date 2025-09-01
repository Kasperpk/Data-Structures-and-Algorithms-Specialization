def maximum_product_of_two_sequences(prices, clicks):
    # Sort both sequences descending
    prices_sorted = sorted(prices, reverse=True)
    clicks_sorted = sorted(clicks, reverse=True)
    # Compute dot product
    return sum(p * c for p, c in zip(prices_sorted, clicks_sorted))

if __name__ == "__main__":
    prices = list(map(int, input().split()))
    clicks = list(map(int, input().split()))
    result = maximum_product_of_two_sequences(prices, clicks)
    print(result)