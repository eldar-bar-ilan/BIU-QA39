const API_BASE = '/api/products';

function fetchProducts() {
    axios.get(API_BASE)
        .then(res => renderTable(res.data))
        .catch(err => console.error(err));
}

// <td><img src="/static/uploads/${product.image}" alt="Image" width="50"></td>
function renderTable(products) {
    const table = document.getElementById('product-table');
    table.innerHTML = '';
    products.forEach(product => {
        const row = document.createElement('tr');
        row.innerHTML = `
      <td>${product.product_id}</td>
      <td>${product.name}</td>
      <td>$${product.price.toFixed(2)}</td>
      <td><img src="/static/uploads/product.png" alt="Image" height="30"></td>
      <td>
        <button onclick="loadProduct(${product.product_id})">Details</button>
        <button onclick="editProduct(${product.product_id})">Edit</button>
        <button class="delete-bt" onclick="deleteProduct(${product.product_id})">Delete</button>
      </td>`;
        table.appendChild(row);
    });
}

// <img src="${product.image}" alt="${product.name}" width="100">
function loadProduct(id) {
    axios.get(`${API_BASE}/${id}`)
        .then(res => {
            const product = res.data;
            const details = document.getElementById('product-details');
            details.innerHTML = `
        <h3>${product.name}</h3>
        <p>Price: $${product.price}</p>
        <img src="/static/uploads/product.png" alt="${product.name}" width="100">
      `;
        });
}

function editProduct(id) {
    axios.get(`${API_BASE}/${id}`)
        .then(res => {
            const p = res.data;
            document.getElementById('product-id').value = p.product_id;
            document.getElementById('name').value = p.name;
            document.getElementById('price').value = p.price;
            document.getElementById('image').value = p.image;
        });
}

function deleteProduct(id) {
    if (confirm(`Delete this product id ${id}?`)) {
        axios.delete(`${API_BASE}/${id}`)
            .then(() => fetchProducts());
    }
}

document.getElementById('product-form').addEventListener('submit', function (e) {
    e.preventDefault();
    const id = document.getElementById('product-id').value;
    const name = document.getElementById('name').value;
    const price = parseFloat(document.getElementById('price').value);
    const image = document.getElementById('image').value;

    const product = { name, price, image };

    if (id) {
        product.product_id = parseInt(id);
        axios.put(`${API_BASE}/${id}`, product)
            .then(() => {
                fetchProducts();
                this.reset();
            });
    } else {
        axios.post(API_BASE, product)
            .then(() => {
                fetchProducts();
                this.reset();
            });
    }
});

fetchProducts();
