var Newarr=[];
var arr= ["bob",5,"wyatt",4,"blue","waaazup",.85];
for(i=0; i<arr.length; i++){
    if(typeof arr[i]==="number"){
      Newarr.push(arr[i]);
    }
}
  console.log(Newarr);
