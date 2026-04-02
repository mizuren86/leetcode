const rawUsers = [
  { id: 1, name: '卡斯伯', account: 'casper123', password: 'password123', email: 'casper@example.com' },
  { id: 2, name: '小杰', account: 'jay456', password: 'secretpassword', email: 'jay@example.com' },
  { id: 3, name: '怜怜', account: 'lin789', password: 'mypassword', email: 'lin@example.com' }
];

// 請在此處撰寫 map 邏輯
const formattedUsers = rawUsers.map(function(item) {
  /* 程式碼撰寫處 */
  return {
    name: item.name,
    account: item.account
  }
});

console.log(formattedUsers);
/* 預期輸出: 
[
  { name: '卡斯伯', account: 'casper123' },
  { name: '小杰', account: 'jay456' },
  { name: '怜怜', account: 'lin789' }
]
*/
