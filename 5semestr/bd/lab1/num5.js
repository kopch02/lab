var shkolnik ={
    name:"Пётр",
    lastname:"Петров",
    patronymic:"Петрович",
    "year of birth":"2010",
    klass:"5",
    "favorite subject":["английский","информатика","фра"],
    "duration of training":9,
    registration : {
        country:"Россия",
        sity:"Кемерово",
        "number house":5,
        "number apartament":10
    },
    "place of residence" : {
        country:"Россия",
        sity:"Кемерово",
        "number house":5,
        "number apartament":10
    }
};
shkolnik.print_all=function(){
    for (let key in shkolnik){
        if (typeof(shkolnik[key])=="function"){
        }
        else if (typeof(shkolnik[key])=="object"){
            for (let k in shkolnik[key]){
                document.write(k,": ")
                document.write(shkolnik[key][k],"<br>");
            }
        }
        else{
            document.write(key,": ")
            document.write(shkolnik[key],"<br>")
        }
    }
};
shkolnik.swap_yearOfBirth=function(){
    const input = prompt("введите год рождения:");
    let year=new Date().getFullYear()
    if (input<year&&input>(year-200)){
        shkolnik["year of birth"]=input;
    }
};
shkolnik.next_class=function(){
    if (Number(shkolnik["klass"])+1>Number(shkolnik["duration of training"])){
        alert("максимальный класс достигнут");
    }
    else{
        shkolnik["klass"]=Number(shkolnik["klass"])+1;
        alert("вы перешли в "+shkolnik["klass"]+" класс");
    }
};
shkolnik.print_all();
shkolnik.swap_yearOfBirth();
shkolnik.next_class();
shkolnik.print_all();

var myjson = JSON.stringify(shkolnik);

console.log(myjson)

