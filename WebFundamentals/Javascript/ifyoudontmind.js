function ifYouDontMind(hour,minute,period){
  var part1=" ";
  var part2=" ";
  var modtime=0;

  if(minute>= 30){
    part1= "It's almost ";
    modtime=hour+1;
  }
  if(period=="AM"){
    part2=" in the evening";
  }
  console.log(part1+modtime+part2);
}
ifYouDontMind(8,45,"AM");
