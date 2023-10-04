const Products = ({ products }) => (
    <div>
        <h1>Products</h1>
        <ul>
            {products.map((product) => (
                <li key={product.id}>{product.name}</li>
            ))}
        </ul>
    </div>
)

// ServerSide rendering full HTML and returns it (PHP days)
// returns:
{
    products: [
        { id: "1", name: "Blue Sneakers" },
        { id: "2", name: "Leather Boots" },
    ]
}

// Then use products as the prop for the Products component/turns into this:
<div>
    <h1>Products</h1>
    <ul>
        <li>Blue Sneakers</li>
        <li>Leather Boots</li>
    </ul>
</div>