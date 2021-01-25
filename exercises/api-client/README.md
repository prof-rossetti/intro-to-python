# "API Client" Exercise

## Prerequisites

  + [APIs](/notes/software/apis.md)
  + ["Web Requests" Exercise](/exercises/web-requests/README.md)

## Business Prompt

In previous "grocery store" exercises, we have been processing grocery product data from a local CSV file. This allowed managers at different locations to keep their own inventory of products. But to improve consistency of record-keeping across stores, the store owner now wants managers at all stores to share the same inventory of products.

As a lead developer on your team, the professor has deployed the "Groceries API" web service to a public server available at https://groceries-api-csv.herokuapp.com. He explains, each store can use its own "API Client" application to issue HTTP requests to the API, and the API will perform the corresponding operations on a shared CSV inventory of products stored on the server.

## Objective

Your objective is to write a command-line Python application that will allow users in any store to create, read, update, and destroy products from this shared inventory.

## Challenges

First, read the [API Documentation](https://github.com/prof-rossetti/products-api-flask/blob/csv/DOCS.md), which describes how to make requests to perform certain CRUD operations.

> NOTE: You'll see some `curl` examples in there, but that is a command-line utility, and there aren't actually any Python code examples in there. The parts of the documentation you should focus on for each operation are: "what kind of request do I need to make?" (e.g. GET, POST, etc.), and "which URL do I make the request to?"

After consulting the docs, issue an appropriate HTTP request in Python to satisfy each of the challenges below.

### List Products

API Documentation: [List Products](https://github.com/prof-rossetti/products-api-flask/blob/csv/DOCS.md#list-products)

Request information about all products, then loop through and print the "id" and "name" of each.

### Show a Product

API Documentation: [Show Product](https://github.com/prof-rossetti/products-api-flask/blob/csv/DOCS.md#show-product)

Choose a product identifier from the list, then request information about that specific product, then print all the product's attributes.

### Destroy a Product

API Documentation: [Destroy Product](https://github.com/prof-rossetti/products-api-flask/blob/csv/DOCS.md#destroy-product)

Request to delete the previously-selected product from the inventory.

### Create a new Product

API Documentation: [Create Product](https://github.com/prof-rossetti/products-api-flask/blob/csv/DOCS.md#create-product)

Request to create a new product in the inventory.

### Update a Product

API Documentation: [Update Product](https://github.com/prof-rossetti/products-api-flask/blob/csv/DOCS.md#update-product)

Request to update the new product you recently created.

## [Solutions](solution.py)
