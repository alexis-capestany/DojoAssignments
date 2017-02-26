function WhileYouWait(){
  var num= 60;
  while (num>=0){
    console.log(num)
    num--;
    if(num>30){
      console.log("saddddd")
    }
    if(num<30){
      console.log("soooo soon")
    }
    if(num==0){
      console.log("YAAAS")
    }
  }
}

WhileYouWait()
