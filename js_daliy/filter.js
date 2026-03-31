const products = [
  { id: 'prod-1', title: '經典白T', category: '衣服', price: 399 },
  { id: 'prod-2', title: '牛仔褲', category: '褲子', price: 899 },
  { id: 'prod-3', title: '帆布鞋', category: '鞋子', price: 1299 },
  { id: 'prod-4', title: '棒球帽', category: '配件', price: 299 },
  { id: 'prod-5', title: '運動外套', category: '衣服', price: 1599 }
];

// 請在此處撰寫篩選邏輯
const filteredProducts = products.filter(function(item) {
  /* 程式碼撰寫處 */
  return item.category === '衣服' && item.price > 400
});

console.log(filteredProducts);
