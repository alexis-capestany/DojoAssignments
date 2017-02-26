function slList(){
  this.head = null;
  this.num = 0;
  this.removeFromFront = fucntion(num){
    console.log(num);
  }
}

var myList1 = new slList()
var myList2 = new slList()
var myList3 = new slList()

myList1.removeFromFront(5)
myList2.removeFromFront(10)
myList3.removeFromFront(20)

console.log("from list 1",  myList1.num);
console.log("from list 2", myList2.num);
console.log("from list 3", myList3.num);
