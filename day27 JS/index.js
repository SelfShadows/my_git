// alert('我是来自星星的你')


// 申明变量
var name='xiaoli';
var age=18;
var $=18;

console.log('name',name);
console.log('age',age);
console.log('$',$);
console.log('---------------JSON-----------------');
var persen={name:'xiaoli',age:21};
console.log(persen);
console.log(typeof(persen));
console.log(persen.name,persen.age);
// JSON.stringify()转化为字符串
var s=JSON.stringify(persen);
console.log(s);
console.log(typeof(s));
// JSON.parse()转化为对象
var obj=JSON.parse(s);
console.log(obj);
console.log(typeof(obj));
console.log('--------------Date------------------');
var d1= new Date();
console.log(d1);
console.log(d1.toLocaleString()); //本地时间
console.log(d1.toUTCString());    //utc时间(相差8小时)
console.log(d1.getFullYear()+'-'+(d1.getMonth()+1)+'-'+d1.getDate()+' '+d1.getHours()+':'+d1.getMinutes());
console.log(d1.getMonth()+1);
console.log('-------ReExp ==> python re(正则)--------');
/alex/.test(alex)