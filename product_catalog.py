from product_data import products

# Print first few products to understand the structure
print("Sample Products:")
for product in products[:3]:
    print(product)

# Collect customer preferences
customer_preferences = []

while True:
    preference = input("Input a preference: ").strip().lower()
    customer_preferences.append(preference)

    more = input("Do you want to add another preference? (Y/N): ").strip().upper()
    if more == "N":
        break

# Convert preferences list to a set to remove duplicates
customer_preferences_set = set(customer_preferences)

# Convert product tags to sets
products_with_sets = []
for product in products:
    products_with_sets.append({"name": product["name"], "tags": set(product["tags"])})


# Count matching tags
def count_matches(product_tags, customer_preferences):
    return len(product_tags.intersection(customer_preferences))


# Recommend products
def recommend_products(products, customer_preferences):
    recommendations = []

    for product in products:
        matches = count_matches(product["tags"], customer_preferences)
        if matches > 0:
            recommendations.append((product["name"], matches))

    # Sort by highest match count
    recommendations.sort(key=lambda x: x[1], reverse=True)
    return recommendations


# TODO: Step 7 - Call your function and print the results

# Print results
recommended_products = recommend_products(products_with_sets, customer_preferences_set)

print("\nRecommended Products:")
for name, match_count in recommended_products:
    print(f"- {name} ({match_count} match(es))")


# DESIGN MEMO (write below in a comment):
"""
In this project, I used core data structures such as lists and sets to build a basic product recommendation tool. Lists were used to store the initial product catalog and to collect customer preferences because they preserve order and are easy to iterate through. After collecting the users preferences, the list was converted into a set to remove duplicate entries and improve lookup efficiency. This decision helped ensure that repeated preferences did not affect the accuracy of the recommendation results.

A key operation used in this implementation was set intersection. By converting each products tags and the customers preferences into sets, I was able to efficiently compare shared values and count how many tags matched. This approach simplified the logic and made the comparison process faster and more readable than manually checking each value in a list. Loops were used to iterate through the product catalog, calculate match counts, and build a list of recommended products based on relevance. The final recommendations were sorted by match count so that the most relevant products appeared first.

If this system needed to support one thousand or more products, the current approach would still function, but performance considerations would become more important. Additional optimizations could include indexing products by tag or using dictionaries to map tags to product names, reducing the need to scan the entire catalog for each recommendation. In a larger production system, a database or more advanced recommendation techniques could also be introduced. For this prototype, however, lists and sets provide a clear and effective solution that demonstrates foundational data manipulation, logical reasoning, and thoughtful data structure selection.
"""
