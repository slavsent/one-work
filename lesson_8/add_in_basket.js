'use strict';

const basketCounterEl = document.querySelector('.cartIconWrap span');
const basketTotalEl = document.querySelector('.basketTotal');
const basketTotalValueEl = document.querySelector('.basketTotalValue');
const basketEl = document.querySelector('.basket');

/**
 * Обработчик открытия корзины при клике на ее значок.
 */
document.querySelector('.cartIconWrap').addEventListener('click', () => {
  basketEl.classList.toggle('hidden');
});

class BasketProducts {
  basketProds = {};

  addToBasket(id, name, price) {
    console.log(this.basketProds);
    if (!(id in this.basketProds)) {
      this.basketProds[id] = { id: id, name: name, price: price, count: 0 };
    }
    this.basketProds[id].count++;

  }

  getAllBasketCount() {
    return Object.values(this.basketProds).reduce((acc, product) => acc + product.count, 0);
  }

  getAllBasketPrice() {
    return Object.values(this.basketProds).reduce((acc, product) => acc + product.price * product.count, 0);
  }

  renderProductInBasket(productId) {
    const basketRowEl = basketEl.querySelector(`.basketRow[data-id="${productId}"]`);
    if (!basketRowEl) {
      this.renderNewProductInBasket(productId);
      return;
    }

    const product = this.basketProds[productId];
    basketRowEl.querySelector('.productCount').textContent = product.count;
    basketRowEl.querySelector('.productTotalRow')
      .textContent = (product.price * product.count).toFixed(2);
  }

  renderNewProductInBasket(productId) {
    const productRow = `
      <div class="basketRow" data-id="${productId}">
        <div>${this.basketProds[productId].name}</div>
        <div>
          <span class="productCount">${this.basketProds[productId].count}</span> шт.
        </div>
        <div>$${this.basketProds[productId].price}</div>
        <div>
          $<span class="productTotalRow">${(this.basketProds[productId].price *
        this.basketProds[productId].count).toFixed(2)}</span>
        </div>
      </div>
      `;
    basketTotalEl.insertAdjacentHTML("beforebegin", productRow);
  }
}

const newBasket = new BasketProducts();

document.querySelector('.featuredItems').addEventListener('click', event => {
  if (!event.target.closest('.addToCart')) {
    return;
  }
  const featuredItemEl = event.target.closest('.featuredItem');
  const id = +featuredItemEl.dataset.id;
  const name = featuredItemEl.dataset.name;
  const price = +featuredItemEl.dataset.price;

  // Добавляем в корзину продукт.
  newBasket.addToBasket(id, name, price);
  basketCounterEl.textContent = newBasket.getAllBasketCount().toString();
  basketTotalValueEl.textContent = newBasket.getAllBasketPrice().toFixed(2);
  newBasket.renderProductInBasket(id);
});





