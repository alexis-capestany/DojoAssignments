function LinkedList(){
  this.head = null;
}
function Node(data){
  if(!(this instanceof Node)){
  return new Node(data):
  };
  this.data = data;
  this.next = null;
}
LinkedList.prototype.add = function (node){
  if(!(node instanceof Node)){
    node = Node(node)
  }
  node.next = this.head;
  this.head = node;
  return this;
}
LinkedList.prototype.length = function(){
  var count =0;
  var current =this.head;
  while(current){
    count ++;
    current = this.next;
  }
  return count;
}
LinkedLists.prototype.reverse = function(){
  var current = this.head;
  var previous = null;
  var next = null;
  while (current){
    next = current. next;
    current.next = previous;
    previous = current;
    current = next;
  }
  this
}
