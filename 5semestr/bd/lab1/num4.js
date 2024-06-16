let students = [
    ["Петров","Пётр","2","211"],
    ["Иванов","Андрей","2","211"],
    ["Сидоров","Нколай","3","204"],
    ["Кузнецов","Дмитрий","3","204"],
    ["Ларионов","Сергей","4","194"],
    ["Образиов","Иван","4","194"],
];
const input = prompt("введите направление:");

for (var i = 0; i < students.length; ++i) {
    if (input==students[i][3]){
        document.write(students[i],"<br>")
    }
    else{
        console.log(students[i])
    }
}
