const carts = [
  { id: 'cart-1', title: '經典白T', price: 399, quantity: 2 },
  { id: 'cart-2', title: '帆布鞋', price: 1299, quantity: 1 },
  { id: 'cart-3', title: '運動外套', price: 1599, quantity: 1 }
];

// 請在此處撰寫 reduce 邏輯
const totalAmount = carts.reduce(function(acc, cur) {
  /* 程式碼撰寫處 */
  return acc + (acc.price * cur.quantity)
}, 0);

console.log(totalAmount); 
// 預期輸出: 3696 (399*2 + 1299*1 + 1599*1)
