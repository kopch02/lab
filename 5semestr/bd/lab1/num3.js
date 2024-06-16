function factorial(foo) {
    var fact = 1;
    for(let i=1;i<=foo;i++){
        fact*=i;
    }
    document.write(fact,"<br>")
  }

function arifm(foo){
    var sred = 0;
    var summ = 0;
    for(let i=1;i<=foo;i++){
        summ+=i;
    }
    sred=summ/foo
    document.write(sred)
}

const input = prompt("введите число:");

if (input%2==0){
    factorial(input)
}
else{
    arifm(input)
}



