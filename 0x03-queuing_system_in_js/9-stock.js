const express = require('express');
const redis = require('redis');
import { promisify } from "util";


// data
const listProducts = [
  {
    id: 1,
    name: 'Suitcase 250',
    price: 50,
    stock: 4,
  },
  {
    id: 2,
    name: 'Suitcase 450',
    price: 100,
    stock: 10,
  },
  {
    id: 3,
    name: 'Suitcase 650',
    price: 350,
    stock: 2,
  },
  {
    id: 4,
    name: 'Suitcase 1050',
    price: 550,
    stock: 5,
  },
];

// data access
function getItemById(id) {
  for (const item of listProducts) {
    if (item.id === parseInt(id)) {
      return item;
    }
  }
  return null;
}


// server
const app = express();
const bodyParser = require('body-parser');
const port = '1245';
app.listen(port, () => {
  console.log('server running on port ', port);
});
app.use(bodyParser.json())

// products

app.get('/list_products', (req, res) => {
  res.json(listProducts)
});

// in stock in redis
const client = redis.createClient();
const asyncData = promisify(client.get).bind(client);

function reserveStockById(itemId, stock) {
  const item = getItemById(itemId);
  client.incrby(item.id, stock, () => {
    console.log(`reserved stock for item with itemId ${item.id}`);
  });
}

async function getCurrentReservedStockById(itemId) {
    const stock = await asyncData(itemId);
    if (!stock) {
      return 0;
    }
    return stock;
}

// Product detail

app.get('/list_products/:itemId', (req, res) => {
  const { itemId } = req.params;

  getCurrentReservedStockById(itemId)
  .then((data) => {
    const reservedStock = data;
    const item = getItemById(itemId);
    if (item) {
      const data = {
        itemId: item.id,
        itemName: item.name,
        price: item.price,
        initialAvailableQuantity: item.stock,
        currentQuantity: item.stock - reservedStock,
      }
      res.json(data);
    } else {
      res.json({status: 'Product not found'});
    }
  })
  .catch((error) => {
    res.status(500).json({ status: 'Internal Server Error' });
  });
});


// reserve a product
app.get('/reserve_product/:itemId', (req, res) => {
  const { itemId } = req.params;
  const item = getItemById(itemId);
  getCurrentReservedStockById(itemId)
  .then((data) => {
    const reservedStock = data;
    if (item) {
      if (item.stock - reservedStock < 1) {
        res.json({'status':'Not enough stock available', 'itemId': itemId});
      } else if (item.stock - reservedStock > 0) {
        reserveStockById(itemId, 1);
        res.json({'status':'Reservation confirmed','itemId':itemId});
      }
    } else {
      res.json({status: 'Product not found'});
    }
  })
  .catch((error) => {
    res.statusCode(500).json(error);
  });
});
